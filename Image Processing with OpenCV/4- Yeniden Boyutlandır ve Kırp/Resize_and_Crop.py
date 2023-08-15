# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 14:27:59 2023

@author: Hasan Emre
"""

#%% import library
import cv2


img = cv2.imread("lena5.jpg")  # siyah beyaz istiyorsak sıfır koyuyoruz
print("Resim boyutu: ", img.shape) # siyah beyaz ise (512,512)  renkli ise (512,512,3)

cv2.imshow("Orijinal", img)

# Resmi yeniden boyutlandırma  (resize)
imgResized = cv2.resize(img, (800,800)) # istediğimiz boyuta çeviriyoruz
print("Resized img shape: ", imgResized.shape) # yeniden boyutlandırıldı mı diye resim boyutunu yazdırıyoruz
cv2.imshow("Img Resized", imgResized)  # ve resmi tekrar görüntülüyoruz.


# Resmi kırpma  (crop)

imgCropped = img[:300,0:300]   # ilk değer yükseklik (height)  ikinci değer genişlik (weigth)
cv2.imshow("Img Cropped", imgCropped)



