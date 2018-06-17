import cv2
import numpy as np

image = cv2.imread("images/elephant.jpg")
cv2.imshow("Original Image", image)
cv2.waitKey()

blur = cv2.blur(image, (3,3))
cv2.imshow("Averaging Blurring", blur)
cv2.waitKey()

Gaussian = cv2.GaussianBlur(image, (7,7), 0)
cv2.imshow("Gaussian Blurring", Gaussian)
cv2.waitKey()

median = cv2.medianBlur(image, 5)
cv2.imshow("Median Blurring", median)
cv2.waitKey()

bilateral = cv2.bilateralFilter(image, 9, 75, 75)
cv2.imshow("Bilateral Blurring", bilateral)
cv2.waitKey()

cv2.destroyAllWindows()