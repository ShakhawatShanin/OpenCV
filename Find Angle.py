import math
import cv2 as cv
import numpy as np

img = cv.imread('Resources/Protractor360.png')
points = []
def mouseEvent(eventName, x, y, flags, params):
    if eventName == cv.EVENT_LBUTTONDOWN:
        points.append([x, y])
        print(points)
        cv.circle(img, (x, y), 5, (255, 0, 0), -1)
        cv.arrowedLine(img, tuple(points[0]), (x, y), (255, 0, 0), 3)
        cv.imshow('image', img)

        if len(points) == 3:
            degrees = findAngle()
            print(abs(degrees))

def findAngle():
    x1, y1 = np.array(points[0])  # origin | 0 index value
    x2, y2 = np.array(points[1])
    x3, y3 = np.array(points[2])

    radian = np.arctan2(y3 - y1, x3 - x1) - np.arctan2(y2 - y1, x2 - x1)
    angle = np.abs(radian * 180 / np.pi)
    angle = round(angle, 3)
    if angle > 180.0:
        angle = 360 - angle

    cv.putText(img, str((angle)), (x1-40, y1+40), cv.FONT_HERSHEY_DUPLEX, 2, (0, 0, 255), 2)
    cv.imshow('image', img)
    return angle

while True:
    cv.imshow('image', img)
    cv.setMouseCallback('image', mouseEvent)
    if cv.waitKey(1) & 0xff == ord('e'):
        break
