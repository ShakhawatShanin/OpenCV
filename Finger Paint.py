import math
import cv2 as cv
import numpy as np
import mediapipe as mp

vdo = cv.VideoCapture('Resources/Finger Paint.mp4')
mp_draw = mp.solutions.drawing_utils
mp_hand = mp.solutions.hands
hand = mp_hand.Hands()

draw_img = np.zeros((510, 605, 3), np.uint8)  # print img.shape for find
xi, yi = 0, 0
allLandmark = []
while True:
    ret, img = vdo.read()
    img = img[285:795, 0:605]  # img = img[y:y+h, x:x+w] | [x:y, x+w, y+h] = [0:285, 605:795]
    if not ret:
        break

    imgH, imgW, _ = img.shape
    process = hand.process(cv.cvtColor(img, cv.COLOR_BGR2RGB))
    if process.multi_hand_landmarks:
        for lm in process.multi_hand_landmarks:
            for i, each_lm in enumerate(lm.landmark):
                x, y = int(each_lm.x * imgW), int(each_lm.y * imgH)  # convert to x y coordinate
                allLandmark.append([i, x, y])

            if len(allLandmark) != 0:
                xi, yi = 0, 0

                x1, y1 = allLandmark[4][1:]
                x2, y2 = allLandmark[6][1:]
                x3, y3 = allLandmark[8][1:]

                dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
                if dist < 40:
                    if xi == 0 and yi == 0:
                        xi, yi = x2, y2
                    cv.line(img, (xi, yi), (x2, y2), (255, 255, 255), 18)
                    cv.line(draw_img, (xi, yi), (x2, y2), (255, 255, 255), 18)
                    xi, yi = x2, y2

                if allLandmark[6][2] < allLandmark[8][2]:
                    draw_img = np.zeros((510, 605, 3), np.uint8)

            cv.line(img, (x2, y2), (x3, y3), (255, 255, 255), 3)
            cv.line(img, (x1, y1), (x2, y2), (255, 255, 255), 3)
            cv.circle(img, (x1, y1), 5, (0, 0, 255), -1)
            cv.circle(img, (x2, y2), 5, (0, 0, 255), -1)
            cv.circle(img, (x3, y3), 5, (0, 0, 255), -1)

    cv.imshow('Finger Paint', img)
    cv.imshow('Canvas', draw_img)
    allLandmark.clear()
    k = cv.waitKey(1) & 0xff
    if k == ord('q'):
        break

vdo.release()
cv.destroyAllWindows()
