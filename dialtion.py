import cv2 
import numpy as np
input_image = np.array((
    [0, 0, 0, 0, 0, 0, 0, 0,1,1],
    [0, 1, 1, 1, 0, 0, 0, 1,1,1],
    [0, 1, 1, 1, 0, 0, 0, 0,1,1],
    [0, 1, 1, 1, 0, 1, 0, 0,1,1],
    [0, 0, 1, 0, 0, 0, 0, 0,1,1],
    [0, 0, 1, 0, 0, 1, 1, 0,1,1],
    [0, 0, 1, 0, 0, 0, 0, 0,1,1],
    [0, 0, 1, 0, 0, 1, 1, 0,1,1],
    [0,1, 0, 1, 0, 0, 1, 0,1,1],
    [0, 1, 1, 1, 0, 0, 0, 0,1,1]), dtype="uint8")
kernel = np.array((
        [0, 1, 0],
        [1, -1, 1],
        [0, 1, 0]), dtype="uint8")
img_erosion = cv2.erode(input_image, kernel)
img_dilation = cv2.dilate(input_image, kernel)
 
cv2.imshow('Input', input_image)
cv2.imshow('Erosion', img_erosion)
cv2.imshow('Dilation', img_dilation)
 
cv2.waitKey(0)