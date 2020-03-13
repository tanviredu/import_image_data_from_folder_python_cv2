training_data=[]

def create_training_data():
    i=0
    for item in os.listdir('../input'):
        class_num=test_res[i]
        img_array = cv2.imread(item,cv2.IMREAD_GRAYSCALE)
        new_array = cv2.resize(img_array,(IMG_SIZE,IMG_SIZE))
        training_data.append([new_array,class_num])    
        #print(class_num)
        i+=1
