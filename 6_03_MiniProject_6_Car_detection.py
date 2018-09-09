import cv2
import numpy as np
import time

car_classidier = cv2.CascadeClassifier("Haarcascades/haarcascade_car.xml")

cap = cv2.VideoCapture("images/cars.avi")

while cap.isOpened():

    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cars = car_classidier.detectMultiScale(gray, 1.3, 3)

    for (x,y,w,h) in cars:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,255),2)
        cv2.imshow("Cars", frame)

    if cv2.waitKey(1) == 13:
        break

cap.release()
cv2.destroyAllWindows()