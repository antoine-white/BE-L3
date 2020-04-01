# -*- coding: utf-8 -*-
import cv2
import numpy as np
import color_ops


img = cv2.imread('lena.jpg')
cv2.imwrite('lena_sep.jpg',color_ops.sepia(img))
"""sepia = color_ops.sepia(img.copy())
print(sepia)
cv2.imwrite('lena_sepia2.jpg',sepia)


#rint(img)
#
#print(img)
"""
"""
red = np.zeros((256, 256, 3), dtype = "uint8")
for l in red:
    for l in a:
        p[2] = 255  
cv2.imwrite('red.png',red)

key = cv2.waitKey(0)
"""

