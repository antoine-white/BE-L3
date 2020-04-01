# -*- coding: utf-8 -*-
import numpy as np


def blue(img):
    for lign in img:
        for pixel in lign:
           pixel[1] = 0
           pixel[2] = 0
    return img

green = lambda img : np.array(list(map(lambda lign : list(map(lambda p : [0,p[1],0],lign)),img)), dtype = "uint8")
""" 
def green(img):
    for lign in img:
        for pixel in lign:
           pixel[0] = 0
           pixel[2] = 0
    return img
"""
def red(img):
    img[:, :, 0] = 0
    img[:, :, 1] = 0
    return img

def neg(img):
    for line in img:
        for pixel in line:
           pixel[0] = 255 - pixel[0] 
           pixel[1] = 255 - pixel[1]
           pixel[2] = 255 - pixel[2]
    return img
#coeff from https://stackoverflow.com/questions/1061093/how-is-a-sepia-tone-created     
def sepia(img):
    for line in img:
        for pixel in line:
           pixel[2] = int((float(pixel[2]) * 0.393) + (float(pixel[1]) * 0.769) + (float(pixel[0]) * 0.189))
           pixel[1] = int((float(pixel[2]) * 0.349) + (float(pixel[1]) * 0.686) + (float(pixel[0]) * 0.168))
           pixel[0] = int((float(pixel[2]) * 0.272) + (float(pixel[1]) * 0.534) + (float(pixel[0]) * 0.131))
           for i in range(0,len(pixel)):
               if pixel[i] > 255:
                   pixel[i] = 255;
    return img
    