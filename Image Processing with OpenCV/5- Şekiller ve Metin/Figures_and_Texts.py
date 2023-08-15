# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 16:09:20 2023

@author: Hasan Emre
"""

#%% import library
import cv2
import numpy as np

# resim oluştur
img = np.zeros((512,512,3), np.uint8) # siyah bir resim 
print(img.shape)
cv2.imshow("Siyah", img)


# Çizgi 
# (resim, başlangıç noktası, bitiş noktası, renk, kalınlık)
cv2.line(img, (0,0), (512,512), (0,255,0), 3 )  # RGB =  opencv de BGR = Yeşil için (0,255,0)
cv2.imshow("Cizgi", img)

# dikdörtgen
# (resim, başlangıç noktası, bitiş noktası, renk, içinin doluluğu )
cv2.rectangle(img, (0,0), (250,250), (255,0,0), cv2.FILLED)
cv2.imshow("Dikdortgen", img)


# Çember
# (resim, merkez, yarıçapı, renk, )
cv2.circle(img, (300,300), 45, (0,0,255),  cv2.FILLED)
cv2.imshow("Cember", img)


# Metin
# (resim, resim yazısı, başlangıç noktası, yazı tipi, yazı kalınlığı, renk)
cv2.putText(img, "Resim", (350,300), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255))
cv2.imshow("Metin", img)

#%% Örnek  EMRE

img = np.zeros((500,900,3), np.uint8)
cv2.imshow("Emre", img)


cv2.line(img, (100,100), (100,300), (0,0,255), 3)
cv2.line(img, (100,100), (200,100), (0,0,255), 3)
cv2.line(img, (100,200), (200,200), (0,0,255), 3)
cv2.line(img, (100,300), (200,300), (0,0,255), 3)

cv2.line(img, (250,300), (300,100), (0,0,255), 3)
cv2.line(img, (300,100), (350,300), (0,0,255), 3)
cv2.line(img, (350,300), (400,100), (0,0,255), 3)
cv2.line(img, (400,100), (450,300), (0,0,255), 3)

cv2.line(img, (500,300), (500,100), (0,0,255), 3)
cv2.line(img, (500,100), (600,100), (0,0,255), 3)
cv2.line(img, (600,100), (600,200), (0,0,255), 3)
cv2.line(img, (600,200), (500,200), (0,0,255), 3)
cv2.line(img, (500,200), (600,300), (0,0,255), 3)

cv2.line(img, (650,300), (650,100), (0,0,255), 3)
cv2.line(img, (650,100), (750,100), (0,0,255), 3)
cv2.line(img, (750,200), (650,200), (0,0,255), 3)
cv2.line(img, (650,300), (750,300), (0,0,255), 3)


cv2.imshow("Emre", img)

