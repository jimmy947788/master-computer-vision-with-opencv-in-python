import cv2
import numpy as np

image = cv2.imread("images/input.jpg")

rotated_image = cv2.transpose(image)

cv2.imshow("Rotated Image", rotated_image)

cv2.waitKey(0)
cv2.destroyAllWindows()