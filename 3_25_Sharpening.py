import cv2
import numpy as np

image = cv2.imread("images/input.jpg")
cv2.imshow("Original Image", image)
cv2.waitKey()

kernel_sharpening = np.array(
    [
        [-1, -1, -1],
        [-1, 9, -1],
        [-1, -1, -1]
    ]
)

sharpened = cv2.filter2D(image, -1, kernel_sharpening)

# Sharpening 銳化
cv2.imshow("Image Sharpening", sharpened)

cv2.waitKey()
cv2.destroyAllWindows()