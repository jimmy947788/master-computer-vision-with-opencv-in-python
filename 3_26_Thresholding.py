import cv2
import numpy as np

image = cv2.imread("images/gradient.jpg")
cv2.imshow("Original Image", image)

# Value below 127 goes to 0 (black, everything above goes to 255(white))
ret, thresh1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("1 Threshold Binary", thresh1)

# Value below 127 goes to 255 and values above 127 go to 0 (reverse of above)
ret, thresh2 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("2 Threshold Binary Inverse", thresh2)

# Value below 127 are truncated (held) as 127 (the 255 argument is unused)
ret, thresh3 = cv2.threshold(image, 127, 255, cv2.THRESH_TRUNC)
cv2.imshow("3 Threshold truncated", thresh3)

# Value below 127 goes to 0, above 127 are unchanged
ret, thresh4 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO)
cv2.imshow("4 Threshold to zero", thresh4)

# Reserver of above, below 127 is unchanged, above 127 goes to 0
ret, thresh5 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO_INV)
cv2.imshow("5 Threshold to zero Inverse", thresh5)

cv2.waitKey()
cv2.destroyAllWindows()