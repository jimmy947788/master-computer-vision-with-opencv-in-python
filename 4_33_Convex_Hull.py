import cv2
import numpy as np

image = cv2.imread("images/hand.jpg")
cv2.imshow("Original Image", image)
cv2.waitKey(0)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray_image, 176, 255, 0)

binary, contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

n = len(contours) - 1
print("len(contours) - 1 = ", n)
contours = sorted(contours, key=cv2.contourArea, reverse=False )[:n]

for c in contours:
    x, y, w, h = cv2.boundingRect(c)
    cv2.rectangle(image, (x,y), (x+w,y+h), (0,0,255), 2)
    cv2.imshow("Bounding Rectangle", image)

cv2.waitKey()

for c in contours:
    hull = cv2.convexHull(c)
    cv2.drawContours(image, [hull], 0, (0,255,0), 2)
    cv2.imshow("Convex Hull", image)

cv2.waitKey()
cv2.destroyAllWindows()

