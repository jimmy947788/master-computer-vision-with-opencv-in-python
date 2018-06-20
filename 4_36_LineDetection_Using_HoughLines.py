import cv2
import numpy as np

image = cv2.imread("images/soduku.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 170, apertureSize = 3)

lines = cv2.HoughLines(edges, 1, np.pi / 180, 250)
print(lines[0])

for [[rho, theta]] in lines:
    #第一个元素是距离rho  
    #第二个元素是角度theta 
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    print("x0:", x0, "y0:", y0)
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    
    cv2.line(image, (x1, y1), (x2, y2), (255,0,0), 2)

cv2.imshow("Hough Lines", image)
cv2.waitKey()
cv2.destroyAllWindows()