import pygame
import cv2
import numpy as np
import random


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
                    shapeDict['triangle'] += 1
                    break 
                case 4:
                    cv2.putText(imgContour, "Square", (x + w + 20, y + 20), 
                            cv2.FONT_HERSHEY_COMPLEX, .7, (0,255,0), 2)
                    shapeDict['square'] += 1
                    break 
                case 5:
                    cv2.putText(imgContour, "Pentagon", (x + w + 20, y + 20), 
                            cv2.FONT_HERSHEY_COMPLEX, .7, (0,255,0), 2)
                    shapeDict['pentagon'] += 1
                    break 
                case 6:
                    cv2.putText(imgContour, "Hexagon", (x + w + 20, y + 20), 
                            cv2.FONT_HERSHEY_COMPLEX, .7, (0,255,0), 2)
                    shapeDict['hexagon'] += 1
                    break 
                case 8:
                    cv2.putText(imgContour, "Octagon", (x + w + 20, y + 20), 
                            cv2.FONT_HERSHEY_COMPLEX, .7, (0,255,0), 2)
                    shapeDict['octagon'] += 1
                    break 
                case _:
                    cv2.putText(imgContour, "Unknown", (x + w + 20, y + 20), 
                            cv2.FONT_HERSHEY_COMPLEX, .7, (0,255,0), 2)
                    break 


def check(shapeDict, target):

    for shape in shapeDict:
        if shapeDict[shape] >= 50:
            if shape == target:
                return True
            elif shapeDict[shape] >= 80 and shape != target:
                return False


def get_shape():
    val = random.randint(0,4)
    if val == 0:
        return 'triangle'
    elif val == 1:
        return 'square'
    elif val == 2:
        return 'pentagon'
    elif val == 3:
        return 'hexagon'
    elif val == 4:
        return 'octagon'
    

def clear_dict(shapeDict):
    for shape in shapeDict:
        shapeDict[shape] = 0
    print(shapeDict)
    return shapeDict


def game_loop(webcam):
    pygame.init()
    width, height = 1280, 720

    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("ShapeIt!")

    fps = 30
    clock = pygame.time.Clock()

    shapeDict = {'triangle': 0, 'square': 0, 'pentagon': 0, 
                 'hexagon': 0, 'octagon': 0}

    start = True
    drawing = True
    task = get_shape()
    print(task)

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

        if check(shapeDict, task) == True:
            print ("Nice!!")
            shapeDict = clear_dict(shapeDict)
            task = get_shape()
            print(task)
        elif check(shapeDict, task) == False:
            print ("NO!!!!! >:(")
            shapeDict = clear_dict(shapeDict)
            task = get_shape()
            print(task)


        imgContour = cv2.cvtColor(imgContour.copy(), cv2.COLOR_BGR2RGB)
        imgContour = np.rot90(imgContour) 

        frame = pygame.surfarray.make_surface(imgContour).convert()
        frame = pygame.transform.flip(frame, True, False)

        window.blit(frame, (155, 90))

        pygame.display.update()

        clock.tick(fps)


def main():
    frameWidth = 1180
    frameHeight = 620
    cap = cv2.VideoCapture(0)
    cap.set(3, frameWidth)
    cap.set(4, frameHeight)

    cv2.namedWindow("Parameters")
    cv2.resizeWindow("Parameters", 640, 240)
    cv2.createTrackbar("Threshold1", "Parameters", 255, 255, empty)
    cv2.createTrackbar("Threshold2", "Parameters", 116, 255, empty)

    game_loop(cap)


main()

