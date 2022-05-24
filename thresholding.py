import cv2
import numpy as np
img=cv2.imread('/home/darik/Desktop/Dev/dna.jpg')
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,t1=cv2.threshold(img,120,255,cv2.THRESH_BINARY)
ret,t2=cv2.threshold(img,120,255,cv2.THRESH_BINARY_INV)
ret,t3=cv2.threshold(img,120,255,cv2.THRESH_TRUNC)
ret,t4=cv2.threshold(img,120,255,cv2.THRESH_TOZERO)
ret,t5=cv2.threshold(img,120,255,cv2.THRESH_TOZERO_INV)
cv2.imshow('Binary Threshold',t1)
cv2.imshow('Binary Threshold Inverse',t2)
cv2.imshow('Truncated Threshold ',t3)
cv2.imshow('Set to 0',t4)
cv2.imshow('Set to 0 Inverted',t5)
if cv2.waitKey(0) & Oxff==27:
    cv2.destroyAllWIndows()
