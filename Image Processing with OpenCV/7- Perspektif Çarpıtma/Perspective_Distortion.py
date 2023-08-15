# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 16:51:34 2023

@author: Hasan Emre
"""

#%% import library
import cv2
import numpy as np

# resmi içe aktar
img = cv2.imread("kart.png")
cv2.imshow("Orijinal", img)

# dönüştürmek istediğimiz boyutları yazıyoruz 
width = 400
height = 500

# ilk olarak döndermek istediğimiz resmin köşelerinin koordinatlarını alıyoruz
pts1 = np.float32([[203,1],[1,472],[540,150],[338,617]]) 
# daha sonra nasıl düzleştireceksek ona göre tekrar koordinatlar giriyoruz
pts2 = np.float32([[0,0], [0,height], [width,0], [width,height]])

# Resmi Perspektife çevirerek matrix değerlerini alıyoruz
matrix = cv2.getPerspectiveTransform(pts1, pts2)
print(matrix)
# Perspektif ettiğimiz resmi çeviriyoruz
imgOutput = cv2.warpPerspective(img, matrix, (width, height))
cv2.imshow("Nihai Resim", imgOutput)

