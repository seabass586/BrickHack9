import cv2
import numpy

cap = cv2.VideoCapture(0)

# Opens window to show camera capture, press q to quit
while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


def main():
    print(cv2.__version__)


main()
