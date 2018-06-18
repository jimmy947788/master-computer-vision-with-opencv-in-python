import cv2
import numpy as np

image = cv2.imread("images/house.jpg")
original_image = image.copy()
cv2.imshow("Original Image", image)
cv2.waitKey(0)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY_INV)

binary, contour, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
#print(contour)

for c in contour:
    x, y, w, h = cv2.boundingRect(c)
    cv2.rectangle(original_image, (x,y), (x+w,y+h), (0,0,255), 2)
    cv2.imshow("Bounding Rectangle", original_image)

cv2.waitKey()

for c in contour:
    accuracy = 0.03 * cv2.arcLength(c, True) # 0.03 和 0.01有不同效果
    # cv.approxPloyDP是一個計算進似多邊形框的函式，該函式有三個引數： 
    # 第一個引數為「輪廓」 
    # 第二個引數為εε值，它表示圓輪廓與近似多邊形的最大差值（這個值越小，近似多邊形與源輪廓越接近） 
    # 第三個引數為「布林標記」表示這個多邊形是否閉和合 
    # εε是為所得到的近似多邊形周長與輪廓之間的最大差值，差值越小，多邊形輪廓越相似。 
    #原文網址：https://itw01.com/MU6QE38.html
    approx = cv2.approxPolyDP(c, accuracy, True)
    cv2.drawContours(image, [approx], 0, (0, 255, 0), 2)
    cv2.imshow("Approx Poly DP", image)

cv2.waitKey()
cv2.destroyAllWindows()