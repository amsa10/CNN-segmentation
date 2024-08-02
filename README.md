# Conv-segmentation
![image](https://github.com/user-attachments/assets/b1c112f5-9210-4159-8c23-123c1604fe6d)
https://github.com/amsa10/Conv-segmentation/blob/main/data/segmented.png?raw=true

[Click here to view the image](https://github.com/amsa10/Conv-segmentation/blob/main/data/segmented.png?raw=true)




## Instructions 
```bash
1. Open your terminal and run the following command: 
cd path/to/data
./download.sh

2. Extract Patches from an Image: 
python create_patches.py /path/to/img.tiff /path/to/patches
     *If the directory patches doesn’t exist, the script will create it.


3. Prediction
cd /path/to/preprocessing_data
python predict_patches.py /path/to/patches /path/to/output https://model/download

4 Unpatch and display
python reconstruct_and_display.py /path/to/original_image.tiff /path/to/predictions.npy /path/to/output/segmented.png


## Literature

This project is based on by the following works: 

1. https://arxiv.org/abs/1901.10077

 


