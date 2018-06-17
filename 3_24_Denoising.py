import cv2
import numpy as np

image = cv2.imread("images/elephant.jpg")
cv2.imshow("Original Image", image)
cv2.waitKey()

dst = cv2.fastNlMeansDenoisingColored(image, None, 6, 6, 7, 21)

cv2.imshow("Fast Means Denoising", dst)
cv2.waitKey()
cv2.destroyAllWindows()