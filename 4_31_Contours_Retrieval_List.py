import cv2
import numpy as np

image = cv2.imread("images/shapes_donut.jpg")
cv2.imshow("Input Image", image)
cv2.waitKey(0)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

edge = cv2.Canny(gray, 30, 200)
cv2.imshow("Canny Edge", edge)
cv2.waitKey(0)

# https://blog.csdn.net/sunny2038/article/details/12889059
# 第一个参数是寻找轮廓的图像；
# 第二个参数表示轮廓的检索模式，有四种（本文介绍的都是新的cv2接口）：
#     cv2.RETR_EXTERNAL表示只检测外轮廓
#     cv2.RETR_LIST检测的轮廓不建立等级关系
#     cv2.RETR_CCOMP建立两个等级的轮廓，上面的一层为外边界，里面的一层为内孔的边界信息。如果内孔内还有一个连通物体，这个物体的边界也在顶层。
#     cv2.RETR_TREE建立一个等级树结构的轮廓。
# 第三个参数method为轮廓的近似办法
#     cv2.CHAIN_APPROX_NONE存储所有的轮廓点，相邻的两个点的像素位置差不超过1，即max（abs（x1-x2），abs（y2-y1））==1
#     cv2.CHAIN_APPROX_SIMPLE压缩水平方向，垂直方向，对角线方向的元素，只保留该方向的终点坐标，例如一个矩形轮廓只需4个点来保存轮廓信息
#     cv2.CHAIN_APPROX_TC89_L1，CV_CHAIN_APPROX_TC89_KCOS使用teh-Chinl chain 近似算法
#
# 官方參考：
# http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_contours/py_contours_hierarchy/py_contours_hierarchy.html
binary,contours,hierarchy = cv2.findContours(edge, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
cv2.imshow("Canny Edge After Contouring", edge)
cv2.waitKey(0)

print(contours)
print("Number of Contours found " + str(len(contours)))

cv2.drawContours(image, contours, -1, (0,255,0), 3)
cv2.imshow("Contours", image)
cv2.waitKey(0)

cv2.destoryAllWindows()