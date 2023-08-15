# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 11:01:26 2023

@author: Hasan Emre
"""

#%% import library

import cv2
import matplotlib.pyplot as plt

# resmi içe aktar
img = cv2.imread("img1.jpg")  # cv2.imread("img1.jpg", 0)  siyah beyaz resim için 0 koyarakta yapabiliriz  yada aşağdaki gibi de olabilir
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.figure()
plt.imshow(img ,cmap = "gray") # rengi komple siyah beyaz yapıyor
plt.axis("off")
plt.show()


# eşikleme 
# threshold değeri 60 tan büüyk olan ları beyaz yap diyoruz ve geri kalan kısmı siyah bir şekilde eşiklemiş oluyoruz
_, thresh_img = cv2.threshold(img, thresh = 60, maxval= 255, type = cv2.THRESH_BINARY)

# _, thresh_img = cv2.threshold(img, thresh = 60, maxval= 255, type = cv2.THRESH_BINARY_INV) # bu şekilde ise 60 tan yukarıyı siyah yapıyor

plt.figure()
plt.imshow(thresh_img, cmap = "gray")
plt.axis("off")
plt.show()



# uyarlamalı eşik değeri 
# ( resim, maximum value, adaptive metotumuz, thresholdun eşikleme türü, blok boyutumuz, c değerimiz adaptivinin genelden pozitif olur )
thresh_img2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 8)
plt.figure()
plt.imshow(thresh_img2, cmap="gray")
plt.axis("off")
plt.show()

