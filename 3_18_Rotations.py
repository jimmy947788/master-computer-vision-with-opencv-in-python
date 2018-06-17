import cv2
import numpy as np

image = cv2.imread("images/input.jpg")

height, width = image.shape[:2]

#參數1: 中心點
#參數2: 角度
#參數3: 縮放比例
rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, 1)

rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

cv2.imshow("Rotated Image", rotated_image)

cv2.waitKey(0)
cv2.destroyAllWindows()