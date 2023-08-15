# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 11:31:50 2023

@author: Hasan Emre
"""

#%% import library
import cv2
import matplotlib.pyplot as plt
import numpy as np

import warnings
warnings.filterwarnings("ignore")

# blurring (detayı azaltır ve gürültüyü engeller)
img = cv2.imread("NYC.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure()
plt.imshow(img)
plt.axis("off")
plt.title("Orijinal")
plt.show()


"""
    Ortalama Bulanıklaştırma Yöntemi
    5x5 kutular şeklinde piksellerin ortalamalarını alıyor
"""
# çıktılara dst olarak adlandırıyorlar girdilere ise src olarak adalandırıyorlar 
dst2 = cv2.blur(img,ksize=(3,3))
plt.figure()
plt.imshow(dst2)
plt.axis("off")
plt.title("Ortalama Bulanıklaştırma Yöntemi")
plt.show()




"""
    Gaussian Blur
"""

gb = cv2.GaussianBlur(img, ksize=(3,3), sigmaX = 7)
plt.figure()
plt.imshow(gb)
plt.axis("off")
plt.title(" Gaussian Blur")
plt.show()



"""
    Medyan Blur
    kutuyu sıralı vektör haline getirip ortasındaki sayıyı alıyoruz ve kutunun genliğine yazıyoruz
"""

mb = cv2.medianBlur(img, ksize = 3)
plt.figure()
plt.imshow(mb)
plt.axis("off")
plt.title("Medyan Blur")
plt.show()


#%% Gaussian Noisy ile bulanıklaştırmayı buluyoruz
def gaussianNoise(image):
    row, col, ch = image.shape  # row = 543,  col = 543, ch = 3
    mean = 0
    var = 0.05
    sigma = var**0.5
    
    gauss = np.random.normal(mean, sigma, (row,col,ch)) 
    gauss = gauss.reshape(row,col,ch)
    noisy = image + gauss
    
    return noisy

# içe aktar  ve normalize edeceğiz 0 ile 1 arasında olacak
img = cv2.imread("NYC.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)/255.0
plt.figure()
plt.imshow(img)
plt.axis("off")
plt.title("Orijinal")
plt.show()

# gaussian fonksiyonunu görselleştiriyoruz
gaussianNoisyImage = gaussianNoise(img)
plt.figure()
plt.imshow(gaussianNoisyImage)
plt.axis("off")
plt.title("Gaussian")
plt.show()

# gauss blur ile Noise azaltma işlemi 
gb2 = cv2.GaussianBlur(gaussianNoisyImage, ksize=(3,3), sigmaX = 7)
plt.figure()
plt.imshow(gb2)
plt.axis("off")
plt.title("with Gaussian Blur")
plt.show()


#%% tuz karabiber gürültüsü (resim üzerine siyah ve beyaz noktaların rastgele yereştirilmesi)

img = cv2.imread("NYC.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)/255.0
plt.figure()
plt.imshow(img)
plt.axis("off")
plt.title("Orijinal")
plt.show()


def saltPepperNoise(image):
    row, col, ch = image.shape  # row = 543,  col = 543, ch = 3
    s_vs_p = 0.5
    amount = 0.004
    
    noisy = np.copy(image)
    
    # salt (beyaz noktacıklar ekleniyor)
    num_Salt = np.ceil(amount * image.size * s_vs_p) # ceil( ondalıklı sayıyı yuvarlama işlemi yapıyor)
    coords = [np.random.randint(0, i-1, int(num_Salt)) for i in image.shape] # koordinatlara rastgele int sayılar ekleniyor
    coords = tuple(coords)
    noisy[coords] = 1  # beyaz 1 siyah 0
    
    # pepper (siyah noktacıklar ekleniyor)
    num_pepper = np.ceil(amount * image.size *( 1- s_vs_p)) # ceil( ondalıklı sayıyı yuvarlama işlemi yapıyor)
    coords = [np.random.randint(0, i-1, int(num_pepper)) for i in image.shape] # koordinatlara rastgele int sayılar ekleniyor
    coords = tuple(coords)
    noisy[coords] = 0  # beyaz 1 siyah 0
    
    return noisy

# resim üzerinde siyah beyaz noktalar oluşturduk ve sonra bunu görüntüledik
# daha sonrasında median Blur ile noktaların yani gürültülerin kaybolduğunu gözlemledik

SPImage = saltPepperNoise(img)
plt.figure()
plt.imshow(SPImage)
plt.axis("off")
plt.title("SP image")
plt.show()

mb2 = cv2.medianBlur((SPImage * 255).astype(np.uint8), ksize=3) / 255.0
plt.figure()
plt.imshow(mb2)
plt.axis("off")
plt.title("with Medyan Blur")
plt.show()
