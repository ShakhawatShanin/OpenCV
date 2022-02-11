import numpy as np
import cv2 as cv

def click_event(event, x, y, flags, param):  # event = event_name
    if event == cv.EVENT_LBUTTONDOWN:
        font = cv.FONT_HERSHEY_SIMPLEX
        prnt_xy = str(x) + ', ' + str(y)
        cv.putText(img, prnt_xy, (x, y), font, .5, (255, 255, 0), 2)  # (x, y)=location where we put the text
        cv.imshow('image', img)

img = np.zeros((500, 500, 3), np.uint8)
cv.imshow('image', img)

cv.setMouseCallback('image', click_event)  # 'image' name should be same everywhere

cv.waitKey(0)
cv.destroyAllWindows()
