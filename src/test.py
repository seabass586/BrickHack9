import cv2
import numpy as np


def main():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    # Opens window to show camera capture, press q to quit
    while True:
        _, frame = cap.read()

        # Convert BGR to HSV
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Locate center of screen to pick color
        height, width, _ = frame.shape
        cx = int(width / 2)
        cy = int(height / 2)
        # Pick pixel value
        pixel_center = hsv_frame[cy, cx]
        hue_value = pixel_center[0]

        # Blue range
        # lower_blue = np.array([90, 50, 50])
        # upper_blue = np.array([130, 255, 255])

        color = "Undefined"
        if hue_value < 5:
            color = "RED"
        elif hue_value < 22:
            color = "ORANGE"
        elif hue_value < 33:
            color = "YELLOW"
        elif hue_value < 78:
            color = "GREEN"
        elif hue_value < 131:
            color = "BLUE"
        elif hue_value < 170:
            color = "VIOLET"
        else:
            color = "RED"
        pixel_center_bgr = frame[cy, cx]
        b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])

        # mask = cv2.inRange(hsv, lower_blue, upper_blue)
        # result = cv2.bitwise_and(frame, frame, mask=mask)
        # cv2.imshow('frame', result)
        # cv2.imshow('mask', mask)

        cv2.rectangle(frame, (cx - 220, 10), (cx + 200, 120), (255, 255, 255), -1)
        cv2.putText(frame, color, (cx - 200, 100), 0, 3, (b, g, r), 5)
        cv2.circle(frame, (cx, cy), 5, (25, 25, 25), 3)
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1)

        if key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


main()
