import cv2
import numpy as np

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

def empty(a):
    pass

cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameters", 640, 240)
cv2.createTrackbar("Threshold1", "Parameters", 90, 255, empty)
cv2.createTrackbar("Threshold2", "Parameters", 0, 255, empty)


while True:
    success, img = cap.read()

    imgBlur = cv2.GaussianBlur(img, (7, 7), 1)
    imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)

    # thresholds for the canny detection algorithm
    threshold1 = cv2.getTrackbarPos("Threshold1", "Parameters")
    threshold2 = cv2.getTrackbarPos("Threshold2", "Parameters")

    # canny algorithm detects edges and shows the contours
    imgCanny = cv2.Canny(imgGray, threshold1, threshold2)

    # dilates the image so the edges are bigger and easier to see
    kernel = np.ones((5, 5))
    imgDil = cv2.dilate(imgCanny, kernel, iterations=1)

    # cv2.imshow("Result", img )
    cv2.imshow("Result", imgDil )

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break