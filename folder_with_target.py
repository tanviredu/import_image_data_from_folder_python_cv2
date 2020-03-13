
#### load partial images
import cv2
import os
#### this function will import the data from the folder
def load__partial_images_from_folder(folder,target):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append([img,target])
    return images[:10]