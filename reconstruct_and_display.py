import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import argparse

# Fixed metadata
ORIGINAL_WIDTH = 14456
ORIGINAL_HEIGHT = 1800
PATCH_SIZE = 384
RESIZED_PATCH_SIZE = 192

def reconstruct_image(predictions):
    num_patches_x = ORIGINAL_WIDTH // PATCH_SIZE
    num_patches_y = ORIGINAL_HEIGHT // PATCH_SIZE

    # Initialize arrays for reconstruction
    cloud_mask_full = np.zeros((ORIGINAL_HEIGHT, ORIGINAL_WIDTH), dtype=np.float32)
    count_map = np.zeros((ORIGINAL_HEIGHT, ORIGINAL_WIDTH), dtype=np.float32)

    # Reconstruct the full image
    for i in range(num_patches_y):
        for j in range(num_patches_x):
            start_y = i * PATCH_SIZE
            start_x = j * PATCH_SIZE
            end_y = start_y + RESIZED_PATCH_SIZE
            end_x = start_x + RESIZED_PATCH_SIZE

            # Ensure the end indices do not exceed the image dimensions
            if end_y > ORIGINAL_HEIGHT:
                end_y = ORIGINAL_HEIGHT
            if end_x > ORIGINAL_WIDTH:
                end_x = ORIGINAL_WIDTH

            # Calculate patch indices in predictions
            patch_idx = i * num_patches_x + j
            patch = predictions[patch_idx, :, :, 0]

            # Add patch to full image and update count map
            cloud_mask_full[start_y:end_y, start_x:end_x] += patch
            count_map[start_y:end_x, start_x:end_x] += 1

    # Normalize the full cloud mask
    cloud_mask_full /= np.maximum(count_map, 1)
    return cloud_mask_full

def save_and_display(original_image_path, cloud_mask_full, output_mask_path):
    # Load the original image
    original_image = Image.open(original_image_path)

    # Normalize the image to the [0, 255] range for saving
    cloud_mask_normalized = (cloud_mask_full - cloud_mask_full.min()) / (cloud_mask_full.max() - cloud_mask_full.min())
    cloud_mask_uint8 = (cloud_mask_normalized * 255).astype(np.uint8)

    # Save the cloud mask using PIL
    Image.fromarray(cloud_mask_uint8, mode='L').save(output_mask_path)
    print(f"Full cloud mask saved to {output_mask_path}")

    # Display the original image and cloud mask side by side
    plt.figure(figsize=(16, 8))

    # Display the original image
    plt.subplot(1, 2, 1)
    plt.title('Original Image')
    plt.imshow(original_image, cmap='gray')
    plt.axis('off')

    # Display the cloud mask
    plt.subplot(1, 2, 2)
    plt.title('Cloud Mask')
    plt.imshow(cloud_mask_full, cmap='gray', vmin=0, vmax=1)
    plt.axis('off')

    plt.show()

def main(original_image_path, predictions_path, output_mask_path):
    # Load predictions
    predictions = np.load(predictions_path)
    
    # Reconstruct the full cloud mask
    cloud_mask_full = reconstruct_image(predictions)
    
    # Save and display the images
    save_and_display(original_image_path, cloud_mask_full, output_mask_path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Reconstruct and display images.')
    parser.add_argument('original_image_path', type=str, help='Path to the original image.')
    parser.add_argument('predictions_path', type=str, help='Path to the numpy file containing predictions.')
    parser.add_argument('output_mask_path', type=str, help='Path to save the output cloud mask image.')

    args = parser.parse_args()
    main(args.original_image_path, args.predictions_path, args.output_mask_path)
