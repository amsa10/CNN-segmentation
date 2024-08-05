# Conv-semseg

This is an initial version 

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

## References

- S. Mohajerani and P. Saeedi. ["Cloud-Net: An End-to-end Cloud Detection Algorithm for Landsat 8 Imagery"](https://arxiv.org/pdf/1901.10077.pdf). (forthcoming) 2019. to appear at IEEE International Geoscience and Remote Sensing Symposium (IGARSS).

 


