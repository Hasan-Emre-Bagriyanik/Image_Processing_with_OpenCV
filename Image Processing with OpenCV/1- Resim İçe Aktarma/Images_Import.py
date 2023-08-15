# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 13:09:55 2023

@author: Hasan Emre
"""

#%% import library

import cv2 

# içe aktarma 
img = cv2.imread("resim.jpg", 0)  # buradaki sıfır siyah beyaz anlamına gelir 

# görselleştir
cv2.imshow("ilk resim", img)

k = cv2.waitKey(0) &0xFF  # waitKey klavyeden komut bekliyor demek

if k == 27:  #• 27 klavyede esc tuşunun sayısıdır
    cv2.destroyAllWindows()  # Bütün pencereleri kapat 
elif k == ord("s"):  # bu şekilde de sayı karşılığı değilde klavyedeki harf karşılığına denk geliyor
    cv2.imwrite("resim_gray.jpg", img) # resim açıldığıdna s tuşuna basıldığında resmi siyah beyaz kaydeder 
    cv2.destroyAllWindows()
     