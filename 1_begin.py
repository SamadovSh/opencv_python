import cv2

# img = cv2.imread('images/building.jpg')
# img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))
# img = cv2.GaussianBlur(img, (7, 7), 0)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Result', img)
# # img[0:100, 0:150]

# # cv2.imwrite('images/gray.png', img)
# cv2.waitKey(0)

# print(img.shape)


cap = cv2.VideoCapture('videos/car.mp4')

while True:
    success, img = cap.read()
    # img = cv2.Canny(img, 50, 50)

    # img = cv2.GaussianBlur(img, (13, 13), 0)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Car', img)

    if cv2.waitKey(5) == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
