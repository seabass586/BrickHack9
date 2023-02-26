import pygame
import cv2
import numpy as np


def empty(a):
    pass


def getContours(img, imgContour, shapeDict):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, 
                                           cv2.CHAIN_APPROX_NONE)

    for cnt in contours:
        area = cv2.contourArea(cnt)

        if area > 5000:
            cv2.drawContours(imgContour, cnt, -1, (0, 255, 0), 7)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)

            x, y, w, h = cv2.boundingRect(approx)

            match len(approx):
                case 3:
                    cv2.putText(imgContour, "Triangle", (x + w + 20, y + 20), 
                            cv2.FONT_HERSHEY_COMPLEX, .7, (0,255,0), 2)
                    shapeDict['Triangle'] += 1
                    break 
                case 4:
                    cv2.putText(imgContour, "Square", (x + w + 20, y + 20), 
                            cv2.FONT_HERSHEY_COMPLEX, .7, (0,255,0), 2)
                    shapeDict['Square'] += 1
                    break 
                case 5:
                    cv2.putText(imgContour, "Pentagon", (x + w + 20, y + 20), 
                            cv2.FONT_HERSHEY_COMPLEX, .7, (0,255,0), 2)
                    shapeDict['Pentagon'] += 1
                    break 
                case 6:
                    cv2.putText(imgContour, "Hexagon", (x + w + 20, y + 20), 
                            cv2.FONT_HERSHEY_COMPLEX, .7, (0,255,0), 2)
                    shapeDict['Hexagon'] += 1
                    break 
                case 8:
                    cv2.putText(imgContour, "Octagon", (x + w + 20, y + 20), 
                            cv2.FONT_HERSHEY_COMPLEX, .7, (0,255,0), 2)
                    shapeDict['Octagon'] += 1
                    break 


def check(shapeDict):
    pass


def game_loop(webcam):
    pygame.init()
    width, height = 1280, 720

    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("ShapeIt!")

    fps = 30
    clock = pygame.time.Clock()

    shapeDict = {'Triangle': 0, 'Square': 0, 'Pentagon': 0, 
                     'Hexagon': 0, 'Octagon': 0}

    start = True
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
                pygame.quit()


        # OpenCV
        success, img = webcam.read()
        imgContour = img.copy()

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

        getContours(imgDil, imgContour, shapeDict)

        check(shapeDict)

        imgContour = cv2.cvtColor(imgContour.copy(), cv2.COLOR_BGR2RGB)
        imgContour = np.rot90(imgContour) 

        frame = pygame.surfarray.make_surface(imgContour).convert()
        frame = pygame.transform.flip(frame, True, False)

        window.blit(frame, (0,0))

        pygame.display.update()

        clock.tick(fps)


def main():
    frameWidth = 1280
    frameHeight = 720
    cap = cv2.VideoCapture(0)
    cap.set(3, frameWidth)
    cap.set(4, frameHeight)

    cv2.namedWindow("Parameters")
    cv2.resizeWindow("Parameters", 640, 240)
    cv2.createTrackbar("Threshold1", "Parameters", 255, 255, empty)
    cv2.createTrackbar("Threshold2", "Parameters", 116, 255, empty)

    game_loop(cap)


main()

