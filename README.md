# Conv-segmentation 

This is an initial version 
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
@article{mohajerani2019cloud,
  title={Cloud-Net: An end-to-end cloud detection algorithm },
  author={Mohajerani, Shima and Saeedi, P},
  journal={arXiv preprint arXiv:1901.10077},
  year={2019}
}

 


