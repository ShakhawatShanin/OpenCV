import cv2 as cv
import numpy as np
import random
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'E:\\TESSERACT OCR\\tesseract.exe'
circles = []
counter1 = counter2 = 0
point1 = point2 = myPoint = myColor = []

def click_event(event, x, y, flags, param):
    global circles, counter1, counter2, point1, point2, myColor
    if event == cv.EVENT_LBUTTONDOWN:
        if counter1 == 0:
            point1 = int(x), int(y);
            counter1 += 1
            myColor = (random.randint(0, 2)*200, random.randint(0, 2)*200, random.randint(0, 2)*200)
        elif counter1 == 1:
            point2 = int(x), int(y);
            name = input('Enter Name: ')
            myPoint.append([point1, point2, name])
            counter1 = 0
        circles.append([x, y, myColor])
        counter2 += 1

img = cv.imread("Resources/text.png")
imgCopy = img.copy()
imgMask = np.zeros_like(imgCopy)

while True:
    for x, y, color in circles:
        cv.circle(img, (x, y), 2, color, cv.FILLED)
    cv.imshow("Image", img)
    cv.setMouseCallback('Image', click_event)
    if cv.waitKey(1) & 0xFF == ord('s'):
        print(myPoint)
        break

for i, r in enumerate(myPoint):
    imgCrop = img[r[0][1]:r[1][1], r[0][0]:r[1][0]]
    cv.imshow(str(i), imgCrop)
    img_text = pytesseract.image_to_string(imgCrop)
    print(img_text)
    #cv.rectangle(imgCopy, (r[0][0], r[0][1]), (r[1][0], r[1][1]), (0, 255, 0), cv.FILLED)

cv.imshow('I', imgCopy)
cv.waitKey(0)
