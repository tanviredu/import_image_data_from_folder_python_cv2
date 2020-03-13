
import cv2
import os
#### this function will import the data from the folder
def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images

##test
train_images = load_images_from_folder('../input/chest-xray-pneumonia/chest_xray/train/NORMAL/')