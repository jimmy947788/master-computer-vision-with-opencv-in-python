import cv2
import numpy as np

image = cv2.imread("images/opencv_inv.png", 0)
cv2.imshow("Original Image", image)
cv2.waitKey()

kernel = np.ones((5,5), np.uint8)

erosion = cv2.erode(image, kernel, iterations = 1)
cv2.imshow("Erosion", erosion)
cv2.waitKey()

dilation = cv2.dilate(image, kernel, iterations = 1)
cv2.imshow("Dilation", dilation)
cv2.waitKey()

opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
cv2.imshow("Opening", opening)
cv2.waitKey()

closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
cv2.imshow("Closing", closing)
cv2.waitKey()

cv2.destroyAllWindows()
