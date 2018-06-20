import cv2
import numpy as np

template_image = cv2.imread("images/4star.jpg", 0)
cv2.imshow("Template Image", template_image)
cv2.waitKey(0)

target_image = cv2.imread("images/shapestomatch.jpg")
target_gray_image = cv2.cvtColor(target_image, cv2.COLOR_BGR2GRAY)

ret, thresh1 = cv2.threshold(template_image, 127, 255, 0)
ret, thresh2 = cv2.threshold(target_gray_image, 127, 255, 0)

binary, contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

stored_contours = sorted(contours, key=cv2.contourArea, reverse=True)

template_contour = contours[1]

binary, contours, hierarchy = cv2.findContours(thresh2, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
    match = cv2.matchShapes(template_contour, c, 1, 0.0) # Match Shapes
    print(match)
    if match < 0.15:
        closest_contour = c
    else:
        closest_contour = []

cv2.drawContours(target_image, [closest_contour], -1, (0,255,0), 3)
cv2.imshow("Output Image", target_image)
cv2.waitKey()
cv2.destroyAllWindows() 
