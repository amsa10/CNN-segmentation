import os
import numpy as np
import requests
from tqdm import tqdm
import tensorflow as tf
from tensorflow.keras.losses import Loss
from tensorflow.keras.optimizers import Adam
from PIL import Image
import argparse

class SoftJaccardLoss(Loss):
    def call(self, y_true, y_pred):
        epsilon = 1e-7
        intersection = tf.reduce_sum(y_true * y_pred, axis=[1, 2, 3])
        union = tf.reduce_sum(y_true + y_pred, axis=[1, 2, 3]) - intersection
        loss = 1 - (intersection + epsilon) / (union + epsilon)
        return tf.reduce_mean(loss)

def download_model(model_url, model_path):
    response = requests.get(model_url, stream=True)
    if response.status_code == 200:
        total_size = int(response.headers.get('content-length', 0))
        with open(model_path, 'wb') as file:
            with tqdm(total=total_size, unit='B', unit_scale=True, unit_divisor=1024) as progress_bar:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        file.write(chunk)
                        progress_bar.update(len(chunk))
        print(f"Model downloaded successfully and saved to {model_path}")
    else:
        print(f"Failed to download model, status code: {response.status_code}")

def load_model(model_path):
    # Load the model
    model = tf.keras.models.load_model(model_path, compile=False)
    
    # Recompile with custom loss function and optimizer if necessary
    optimizer = Adam(learning_rate=1e-4)
    model.compile(optimizer=optimizer, loss=SoftJaccardLoss())
    
    return model

def load_patches(patches_dir):
    patches = []
    for filename in os.listdir(patches_dir):
        if filename.endswith('.png'):
            patch_path = os.path.join(patches_dir, filename)
            patch = Image.open(patch_path)
            patch_array = np.array(patch) / 255.0  # Normalize
            patches.append(patch_array)
    return np.array(patches)

def save_predictions(predictions, output_dir):
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for idx, prediction in enumerate(predictions):
        prediction_image = Image.fromarray((prediction.squeeze() * 255).astype(np.uint8))
        prediction_image.save(os.path.join(output_dir, f'prediction_{idx}.png'))

def main(patches_dir, output_dir, model_url):
    model_path = '/content/pretrained_model.h5'
    
    # Download the pretrained model
    download_model(model_url, model_path)
    
    # Load the model
    model = load_model(model_path)
    
    # Load patches from the specified directory
    patches = load_patches(patches_dir)
    
    # Make predictions
    predictions = model.predict(patches)
    
    # Save predictions to the specified directory
    save_predictions(predictions, output_dir)
    print(f"Predictions saved to {output_dir}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Download a model, make predictions on patches, and save predictions.')
    parser.add_argument('patches_dir', type=str, help='Directory containing image patches.')
    parser.add_argument('output_dir', type=str, help='Directory to save predictions.')
    parser.add_argument('model_url', type=str, help='URL to download the pretrained model.')
    
    args = parser.parse_args()
    main(args.patches_dir, args.output_dir, args.model_url)


