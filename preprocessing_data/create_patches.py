import numpy as np
from PIL import Image
from skimage.transform import resize
import os

def extract_patches(img, patch_size, resize_to):
    patches = []
    patch_info = []
    h, w, _ = img.shape
    for i in range(0, h - patch_size + 1, patch_size):
        for j in range(0, w - patch_size + 1, patch_size):
            patch = img[i:i+patch_size, j:j+patch_size]
            patch_resized = resize(patch, resize_to, mode='reflect')
            patches.append(patch_resized)
            patch_info.append((i, j))
    return np.array(patches), patch_info

def save_patches(patches, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for idx, patch in enumerate(patches):
        patch_image = Image.fromarray((patch * 255).astype(np.uint8))  # Convert to uint8
        patch_image.save(os.path.join(output_dir, f'patch_{idx}.png'))

def save_patch_info(patch_info, output_file):
    with open(output_file, 'w') as file:
        for info in patch_info:
            file.write(f'{info[0]},{info[1]}\n')

def main(image_path, output_dir, patch_size, resize_to):
    # Load the image
    image = Image.open(image_path)
    img_array = np.array(image)
    
    # Normalize to range [0, 1]
    img_array = img_array / 65535.0
    
    # Expand dimensions for single-channel to RGBNIR (assuming dummy channels)
    rgbnir_array = np.stack([img_array] * 4, axis=-1)  # Assuming dummy RGBNIR

    # Extract patches and their positions
    patches, patch_info = extract_patches(rgbnir_array, patch_size, resize_to)
    
    # Save patches and metadata
    save_patches(patches, output_dir)
    save_patch_info(patch_info, os.path.join(output_dir, 'patch_info.txt'))

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Extract patches from an image.')
    parser.add_argument('image_path', type=str, help='Path to the input image.')
    parser.add_argument('output_dir', type=str, help='Directory to save patches and metadata.')
    parser.add_argument('--patch_size', type=int, default=384, help='Size of the patches to extract (default: 384).')
    parser.add_argument('--resize_to', type=int, nargs=2, default=(192, 192), help='Size to resize patches as two integers (default: (192, 192)).')
    
    args = parser.parse_args()
    main(args.image_path, args.output_dir, args.patch_size, tuple(args.resize_to))
