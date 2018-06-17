import cv2
import numpy as np

image = cv2.imread('./images/input.jpg')

B, G, R = image[0, 0]
print("BGR image shape : ", image.shape)
print("image[0,0]=B:", B, "G:", G, "R:", R)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print("gray image shape : ", gray_image.shape)
print("gray[10,50]=", gray_image[10, 50])