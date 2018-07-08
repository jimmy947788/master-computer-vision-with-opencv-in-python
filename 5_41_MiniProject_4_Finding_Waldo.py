import cv2
import numpy as np

# Load input image and convert to grayscale
image = cv2.imread("images/WaldoBeach.jpg")
cv2.imshow("Where is Waldo?", image)
cv2.waitKey(0)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Load Template image
template = cv2.imread("images/waldo.jpg", 0)

# 參考 https://docs.opencv.org/2.4/modules/imgproc/doc/object_detection.html
result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# Create Bounding Box
top_left = max_loc
bottom_right = (top_left[0] + 50, top_left[1] + 50)
cv2.rectangle(image, top_left, bottom_right, (0,0,255), 5)

cv2.imshow("Where is Waldo?", image)
cv2.waitKey(0)
cv2.destroyAllWindows()