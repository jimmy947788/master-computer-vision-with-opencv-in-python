import cv2
import numpy as np

 
image = cv2.imread('images/bottlecaps.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
blur = cv2.medianBlur(gray, 5)
#cv2.imshow('blur image', blur)
cv2.waitKey(0)

# opencv 2.x
#$circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1.5, 20)
# opencv 3.x
circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 2, 50, minRadius=30, maxRadius=60)

print (circles)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
       # draw the outer circle
       cv2.circle(image,(i[0], i[1]), i[2], (255, 0, 0), 2)
      
       # draw the center of the circle
       cv2.circle(image, (i[0], i[1]), 2, (0, 255, 0), 5)
 
cv2.imshow('detected circles', image)
cv2.waitKey(0)
cv2.destroyAllWindows()