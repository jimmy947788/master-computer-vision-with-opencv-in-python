import cv2
import numpy as np

image = cv2.imread("images/input.jpg")

# Let's make our image 3/4 of it's original size
image_scaled = cv2.resize(image, None, fx =0.75, fy=0.75)
cv2.imshow("Scaling - Liner Interpolation", image_scaled)
cv2.waitKey(0)

# Let's double the size of our image
image_scaled = cv2.resize(image, None, fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
cv2.imshow("Scaling - Cubic Interpolation", image_scaled)
cv2.waitKey(0)

# Let's skew the re-sizing by setting exact dimensions
image_scaled = cv2.resize(image, (900, 400), interpolation = cv2.INTER_AREA)
cv2.imshow("Scaling - Skewed Interpolation", image_scaled)
cv2.waitKey(0)

cv2.destroyAllWindows()

# 各種內插法補強圖片的比較
# 參考 http://tanbakuchi.com/posts/comparison-of-openv-interpolation-algorithms/