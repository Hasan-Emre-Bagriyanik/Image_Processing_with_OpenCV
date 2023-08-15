# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 16:46:10 2023

@author: Hasan Emre
"""

#%% import library
import cv2
import numpy as np

# resmi içe aktar
img = cv2.imread("lena5.jpg")
cv2.imshow("Orijinal",img)

# yan yan resim birleştirme  (yatay)
hor = np.hstack((img,img))
cv2.imshow("Horizontal",hor)

# alt alta resim birleştirme (dikey)
ver = np.vstack((img,img))
cv2.imshow("Vertical",ver)

