# Conv-segmentation
![Screenshot 2024-08-02 141037](https://github.com/user-attachments/assets/5e21ee2b-220a-40ed-933a-0faf51dd4777)
![image](https://github.com/user-attachments/assets/28eee49d-08a6-4c65-b8a1-21ac0fb173a8)
![image](https://github.com/user-attachments/assets/61215c43-9872-4edb-a946-00f0532ef39d)
![image](https://github.com/user-attachments/assets/ebb71736-429d-42d5-b46c-f1b4ba5b7aea)

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





