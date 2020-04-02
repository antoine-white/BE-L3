import sys
import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy import ndimage
    
MIN_SHARP = 0.155
block_size = 4
#source : https://theailearner.com/tag/top-hat-transform-opencv/
def topHatTransformation(img):
    # Structuring element
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(25,25))
    # Apply the top hat transform
    tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
    return tophat

def getComputedVal(img,x,y):
    (lenx,leny) = img.shape
    OFFSET = 6
    min_x = x-OFFSET if x - OFFSET >= 0 else x  
    min_y = y-OFFSET if y - OFFSET >= 0 else y
    max_x = x+OFFSET if x + OFFSET <= lenx else x 
    max_y = y+OFFSET if y + OFFSET <= leny else y
    total = 0
    for i in range(min_x,max_x):
        for j in range(min_y,max_y):
            total += img[i][j]
    return total/((max_x+min_x)*(max_y-min_y))

def sharpMap(img):
    (x,y) = img.shape
    img_tmp = np.zeros((x,y), dtype = "uint8")
    for i in range(0,x):
        for j in range(0,y):
            tmp = (getComputedVal(img,i,j))*255
            img_tmp[i][j] = tmp if tmp < 255 else 255
            #img_tmp[i][j] = getComputedVal(img,i,j)
    return img_tmp

def block(img):
    (x,y) = img.shape  
    lightTotal = 0
    for i in range(0,x):
        for j in range(0,y):
            if img[i][j] == 255:
                lightTotal += 1
    if (lightTotal/(x*y) >= MIN_SHARP):
        return np.full((x,y), 255)
    else:
        return np.zeros((x,y))

def sharpMapBlock(img):
    (x,y) = img.shape    
    img_tmp = np.zeros((x,y), dtype = "uint8")
    for i in range(0,x,block_size):
        for j in range(0,y,block_size):
            img_tmp[i:i+block_size,j:j+block_size] = block(img[i:i+block_size,j:j+block_size])
    return img_tmp
        

def methode_1(imgPath):
    img = cv2.imread(imgPath)
    img = cv2.Canny(img,100,200)
    cv2.imwrite(imgPath + ".edge.jpg",img)
    img = topHatTransformation(img)
    #cv2.imwrite(imgPath + ".tophat.jpg",img)
    #img = sharpMap(img)
    #cv2.imwrite(imgPath + ".sharp-map.jpg",img)
    img = sharpMapBlock(img)
    cv2.imwrite(imgPath + ".sharp-map-block-" + str(block_size) + "-"+ str(MIN_SHARP) + ".jpg",img)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("enter the name of the picture as the first arg")
        exit(-1)
    elif len(sys.argv) == 2:
        methode_1(sys.argv[1])
    else :
         if len(sys.argv) == 4:
            block_size = int(sys.argv[3])
        MIN_SHARP = float(sys.argv[2])
        methode_1(sys.argv[1])