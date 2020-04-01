# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 15:10:17 2020

@author: Antoine
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('lena.jpg')

#blur = cv2.blur(img,(5,5))
blur = cv2.GaussianBlur(img,(5,5),0)

cv2.imwrite('lena_gauss.jpg',blur)