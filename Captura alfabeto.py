# -*- coding: utf-8 -*-
"""
@author: ssant
"""
import cv2
import matplotlib.pyplot as plt
import imutils
import random
import os
Direccion='C:/Users/ssant/OneDrive/Escritorio/Maestria/Tesis/Dataset/palabras/palabras_prueba'
contenido=["Amor","Ayudar","Banco","Doler","Hospital","Jugar",
           "Aereopuerto","Recordar","Sano","Trasmilenio"]
for i in contenido:
    cap = cv2.VideoCapture(0)
    flag = cap.isOpened()
    index = 451
    while(flag):
        ret, frame = cap.read()
        cv2.imshow("Capture_Paizhao",frame)
        k = cv2.waitKey(1) & 0xFF
        #if k == ord ('s'): #Presione la tecla s para guardar la imágen
        if index <=900:
            cv2.imwrite(Direccion +"/"+i+"_"+str(index) + ".jpg", frame)
            print("save" +i+"-"+ str(index) + ".jpg successfuly!")
            index += 1
        elif k == ord ('q'): #Presione la tecla q, el programa sale
            break
    cap.release()
    cv2.destroyAllWindows()
