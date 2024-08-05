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
@INPROCEEDINGS{38-cloud-1,
  author={S. {Mohajerani} and P. {Saeedi}},
  booktitle={IGARSS 2019 - 2019 IEEE International Geoscience and Remote Sensing Symposium},
  title={Cloud-Net: An End-To-End Cloud Detection Algorithm ....},
  year={2019},
  volume={},
  number={},
  pages={1029-1032},
  doi={10.1109/IGARSS.2019.8898776},
  ISSN={2153-6996},
  month={July},
}

@INPROCEEDINGS{38-cloud-2,   
  author={S. Mohajerani and T. A. Krammer and P. Saeedi},   
  booktitle={2018 IEEE 20th International Workshop on Multimedia Signal Processing (MMSP)},   
  title={{"A Cloud Detection Algorithm for Remote Sensing Images Using Fully Convolutional Neural Networks"}},   
  year={2018},    
  pages={1-5},   
  doi={10.1109/MMSP.2018.8547095},   
  ISSN={2473-3628},   
  month={Aug},  
}

 


