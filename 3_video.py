import cv2
import numpy

cap = cv2.VideoCapture('video/car.mp4')

while True:
    success, img = cap.read()

    img = cv2.GaussianBlur(img, (9, 9), 0)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    img = cv2.Canny(img, 100, 100)

    kernel = numpy.ones((5, 5), numpy.uint8)
    img = cv2.dilate(img, kernel, iterations=1)

    img = cv2.erode(img, kernel, itertations=1)

    cv2.imshow('Result', img)

    if cv2.waitKey(5) == ord('q'):
        break
