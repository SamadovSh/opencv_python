import cv2
import numpy as np

photo = np.zeros((500, 500, 3), dtype='uint8')

# RGB =  стандарт
# BRG = OPENCV
# photo[0:100, 50:150] = 153, 194, 64
cv2.rectangle(photo, (50, 70), (100, 100), (153, 194, 64), thickness=3)

cv2.line(photo, (0, photo.shape[1] // 2), (photo.shape[0], photo.shape[1] // 2), (153, 194, 64), thickness=3)

cv2.circle(photo, (photo.shape[1] // 2, photo.shape[0] // 2), 100, (153, 194, 64), thickness=1)

cv2.putText(photo, 'OPENCV', (100, 150), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 0, 255), 2)

cv2.imshow('Photo', photo)
cv2.waitKey(0)