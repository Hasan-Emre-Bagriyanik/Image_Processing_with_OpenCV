# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 10:46:55 2023

@author: Hasan Emre
"""

# %% import library

import cv2
import matplotlib.pyplot as plt

# karıştırma 
# gerçek resim RGB sıralamasında renk yapısı varken opencv de is BGR renk yapısı var bundan dolayı dönüştürme işlemi yapıyoruz
img1 = cv2.imread("img1.jpg")
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB) 
 
img2 = cv2.imread("img2.jpg")
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)

print("img1: ",img1.shape)
print("img2: ",img2.shape)  # shape ler aynı değillerse birleştirme işleminde hata verir.

# iki resmin boyutlarını eşitliyoruz
img1 = cv2.resize(img1, (600,600))
print("img1: ",img1.shape)

img2 = cv2.resize(img2, (600,600))
print("img2: ",img2.shape)

plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)

# karıştırılmış resim  = alpha*img1 + beta*img2
blended = cv2.addWeighted(src1 = img1, alpha = 0.5, src2 = img2, beta = 0.5, gamma = 0.0)
plt.figure()
plt.imshow(blended)


