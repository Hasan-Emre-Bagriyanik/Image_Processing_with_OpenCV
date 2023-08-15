# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 13:30:48 2023

@author: Hasan Emre
"""

#%% import library

import cv2
import matplotlib.pyplot as plt

# resmi içe aktar 
img  = cv2.imread("sudoku.jpg")
plt.figure()
plt.imshow(img,  cmap="gray")
plt.axis("off")
plt.title("Orijinal img")
plt.show()


# x gardyan 
# (resim , outputun derinliği, x yönünde , y yönünde , 5*5 lik bir kutucuk)
# resimde sadece x ekseni içindeki çizgiler oluştu
sobelx = cv2.Sobel(img,ddepth= cv2.CV_16S, dx=1, dy = 0, ksize=5)
plt.figure()
plt.imshow(sobelx,  cmap="gray")
plt.axis("off")
plt.title("Sobel X img")
plt.show()


# y gardyan 
# (resim , outputun derinliği, x yönünde , y yönünde , 5*5 lik bir kutucuk)
# resimde sadece y ekseni içindeki çizgiler oluştu
sobely = cv2.Sobel(img,ddepth= cv2.CV_16S, dx=0 ,dy = 1, ksize=5)
plt.figure()
plt.imshow(sobely,  cmap="gray")
plt.axis("off")
plt.title("Sobel Y img")
plt.show()


# Laplacian gradyan
laplacian = cv2.Laplacian(img, ddepth = cv2.CV_16S)
plt.figure()
plt.imshow(laplacian,  cmap="gray")
plt.axis("off")
plt.title("laplacian img")
plt.show()
