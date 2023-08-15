# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 14:00:01 2023

@author: Hasan Emre
"""

#%% import library

import cv2
import matplotlib.pyplot as plt
import numpy as np

# resim içe aktar
img = cv2.imread("red_blue.jpg")
img_vis = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure()
plt.imshow(img_vis)
plt.show()


print(img.shape) # boyutu (371, 366, 3)
# 
# (resim, RGB yada Gray burada 0 ile gray olacak, resmin belli bir kısmını alma , renk boyutu 255 ve 0 ile 256, ranges ile gidilecek sıra)
img_hist = cv2.calcHist([img], channels = [0], mask = None, histSize = [256], ranges = [0, 256])
print(img_hist.shape)
plt.figure()
plt.plot(img_hist)
plt.show()


# bir renk scalası belirledik ve bir döngü ile içerisinde 3 farklı renk ile plot çizdiriyoruz 
color = ("b","g","r")
plt.figure()
for i , c in enumerate(color):
    hist = cv2.calcHist([img], channels = [i], mask = None, histSize = [256], ranges = [0, 256])
    plt.plot(hist, color = c) 


#%%
# farklı bir üzerinden maskeleme yaparak sadece belirli bir yerde inceleme yapacağız
golden_gate = cv2.imread("goldenGate.jpg")
golden_gate_vis = cv2.cvtColor(golden_gate, cv2.COLOR_BGR2RGB)
plt.figure()
plt.imshow(golden_gate_vis)
plt.title("Orijinal İmg")

print(golden_gate.shape)  # (2448, 3264, 3)  

# Resmin boyutu çok büyük olduğu için mask işlemi yaparak belirli kısmı inceleyeceğiz
mask = np.zeros(golden_gate.shape[:2], np.uint8)
plt.figure()
plt.imshow(mask, cmap="gray")
plt.title("Mask İmg")

# mask ta aralık belirledik ve bunu 255 e yani beyaz olarak eşitledik
mask[1500:2000, 1000:2000] = 255
plt.figure()
plt.imshow(mask, cmap="gray")
plt.title("Mask Belirli aralıklı İmg")


# masked işlemi ile belirli yeri gerçek resim üzerinden tanımladık ve geri kalan yerleri siyah yaparak kapattık
masked_img_vis = cv2.bitwise_and(golden_gate_vis,golden_gate_vis, mask = mask )
plt.figure()
plt.imshow(masked_img_vis, cmap="gray")
plt.title("Masked İmg")

# mask işleminden sonra histogram plotu çizdiriyoruz ve hangi renk scalasına göre plotlar çiziyoruz. channels ı değiştirerek farklı renkleri de ne kadar kullanıldığını görebiliyoruz
masked_img = cv2.bitwise_and(golden_gate,golden_gate, mask = mask )
masked_img_hist = cv2.calcHist([golden_gate], channels = [0], mask = mask, histSize = [256], ranges = [0, 256])
plt.figure()
plt.plot(masked_img_hist)
plt.title("masked_img_hist")


#%% 
# histogram eşitleme
# karşıtlık arttırma 

# resmi içe aktarma
img = cv2.imread("hist_equ.jpg", 0)
plt.figure()
plt.imshow(img, cmap = "gray")
plt.title("Orijinal img")

img_hist = cv2.calcHist([img], channels = [0], mask = None, histSize = [256], ranges = [0, 256])
plt.figure()
plt.plot(img_hist)
plt.title("img_hist")

# eşitleme 
# resim daha canlı bir şekilde görünüme sahip oldu
eq_hist = cv2.equalizeHist(img)
plt.figure()
plt.imshow(eq_hist, cmap = "gray")
plt.title("eq_hist img")

# eşitleme sonucu cizdirdiğimiz histogram
eq_img_hist = cv2.calcHist([eq_hist], channels = [0], mask = None, histSize = [256], ranges = [0, 256])
plt.figure()
plt.plot(eq_img_hist)
plt.title("eq_img_hist")
