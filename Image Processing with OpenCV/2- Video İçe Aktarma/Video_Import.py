# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 13:41:15 2023

@author: Hasan Emre
"""

#%% import library

import cv2
import time

# video ismi
video_name = "MOT17-04-DPM-det.webm"

# video içe aktar: capture, cap
 
cap = cv2.VideoCapture(video_name) # bu videoyu cap içine aktarıyoruz

print("Genişlik: ", cap.get(3))  #" 3.index te genişlik 4. indexde ise yükseklik değerleri bulunur
print("Yükseklik: ", cap.get(4))

if cap.isOpened() == False:  # bu kontrol ile videonun içe aktarılıp aktarılmadığı belirleniryor
    print("hata")
    
    
while True:
    
    ret, frame =  cap.read()  # Videoyu okuma 
    
    if ret == True:
        time.sleep(0.1)  # resimlerin hızlı bir şekilde yüklenip video haline geldiğini görmek için biraz yavaşlatıyoruz. Kullanmazsak çok hızlı akar
        
        cv2.imshow("Video", frame)
    
    else: 
        break  # video bittiği zaman döngüden çıkar 
    
    if cv2.waitKey(1) & 0xFF == ord("q"): 
        break  # kendi istediğimiz zaman videodan çıkarız
        
        
    
cap.release()  # stop capture
cv2.destroyAllWindows() # pencereleri kapatıyoruz