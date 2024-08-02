# Conv-segmentation

## Instructions 
```bash
1. Open your terminal and run the following command: 
cd path/to/data
./download.sh

2. Extract Patches from an Image: 
python create_patches.py /path/to/img.tiff /path/to/patches
     *If the directory patches doesn’t exist, the script will create it.


3. Prediction
python segm.py /path/to/patches /path/to/predictions



