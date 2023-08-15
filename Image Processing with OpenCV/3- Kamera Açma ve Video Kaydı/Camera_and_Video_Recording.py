# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 14:08:21 2023

@author: Hasan Emre
"""


#%% import library 
import cv2

# capture 
cap = cv2.VideoCapture(0) # 0 veya 1 değerlerini alır

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # kameranın yüksekliğini ve genişliğini alıyoruz
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(width,height)

# video kaydet
writer = cv2.VideoWriter("video_kaydı.mp4", cv2.VideoWriter_fourcc(*"DIVX"), 20,(width,height)) # cv2.VideoWriter_fourcc(*"DIVX")  windows için
#  20 = video akışının hızı


while True:
    ret, frame = cap.read()
    cv2.imshow("Video", frame)
    
    # save
    writer.write(frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"): break  # video kaydı durdurma 
    
    
cap.release() # capture yi kapatıyoruz
writer.release() # kaydetmeyi kapatıyoruz
cv2.destroyAllWindows() # tüm pencereleri kapatıyoruz

