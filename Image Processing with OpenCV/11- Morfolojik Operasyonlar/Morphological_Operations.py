# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 15:18:58 2023

@author: Hasan Emre
"""

#%% import library

import cv2
import matplotlib.pyplot as plt
import numpy as np

# 5 çeşit morfolojik Operasyon vardır
# Erozyon : resimdeki yazıların kalınlığı azaltarak inceltir
# Genişleme: Resimdeki yazıları daha da kalınlaştır
# Açma: Resim üzerinde erozyon + genişleme işlemi uygular
# Kapatma: Resim üzerindeki genişleme + erozyon şeklindedir
# Morfolojik Gradyan: Bir görüntünün genişlemsi ve erozyonu arasındaki farktır

# resmi içe aktar
img = cv2.imread("datai_team.jpg",0)
plt.figure()
plt.imshow(img, cmap= "gray")
plt.axis("off")
plt.title("Orijinal Img")
plt.show()
 

# Erozyon
kernel = np.ones((5,5), dtype=np.uint8)
result = cv2.erode(img, kernel, iterations = 1)  # iterasyon sayısını artırdıkça erozyon daha fazla olur ve gidtikçe yazı kaybolur
plt.figure()
plt.imshow(result, cmap= "gray")
plt.axis("off")
plt.title("Erozyon Img")
plt.show()
 
#%%
# Genişleme dilation
result2 = cv2.dilate(img, kernel, iterations = 2) # erozyonun tam tersi olarak kalınlaştırır iterasyonu da arttırırsak gittikçe yazı kalınlaşacak
plt.figure()
plt.imshow(result2, cmap= "gray")
plt.axis("off")
plt.title("Genişleme Img")
plt.show()
 
#%%
# White noise (beyaz gürültü)
whiteNoise = np.random.randint(0,2,size = img.shape[:2])  # 0 il 2 aralığında rastgele sayılar oluşturulacak ve boyutu girecek 
whiteNoise =  whiteNoise*255
plt.figure()
plt.imshow(whiteNoise, cmap= "gray")
plt.axis("off")
plt.title("White Noise Img")
plt.show()
 

noise_img = whiteNoise + img
plt.figure()
plt.imshow(noise_img, cmap= "gray")
plt.axis("off")
plt.title("Img with White Noise Img")
plt.show()


# Açılma (Açılma yöntemi ile yukarıda bir gürültülü resim ile bizim normal resimimizi birleştirdik ve 
# aşağıda açılma ile gürültülerden kurtulup düzgün bir resim ortaya çıkardık)
opening = cv2.morphologyEx(noise_img.astype(np.float32), cv2.MORPH_OPEN, kernel)
plt.figure()
plt.imshow(opening, cmap= "gray")
plt.axis("off")
plt.title("Acilma img")
plt.show()

#%%
# black Noise  ( kapatma açılmanın tam tersi olduğu için black noise inşa edeceğiz)
BlackNoise = np.random.randint(0,2,size = img.shape[:2])  # 0 il 2 aralığında rastgele sayılar oluşturulacak ve boyutu girecek 
BlackNoise =  BlackNoise*-255 # black noise için - ile 255 i çarpmak yeterli 
plt.figure()
plt.imshow(BlackNoise, cmap= "gray")
plt.axis("off")
plt.title("Black Noise ")
plt.show()

black_noise_img = BlackNoise + img
black_noise_img[black_noise_img <= -245] = 0  #♦ filtreliyoruz
plt.figure()
plt.imshow(black_noise_img, cmap= "gray")
plt.axis("off")
plt.title("Black Noise Img")
plt.show()


# Kapatma 
clossing = cv2.morphologyEx(black_noise_img.astype(np.float32), cv2.MORPH_CLOSE, kernel)
plt.figure()
plt.imshow(clossing, cmap= "gray")
plt.axis("off")
plt.title("Kapatma img")
plt.show()

#%% Gradient  (sadece yazıların kenarlarını alır yani içi dolu bir resim yazısında içi boş bir resim yazısında çevirir)
gradient =  cv2.morphologyEx(img.astype(np.float32), cv2.MORPH_GRADIENT, kernel)
plt.figure()
plt.imshow(gradient, cmap= "gray")
plt.axis("off")
plt.title("Grqdient img")
plt.show()
