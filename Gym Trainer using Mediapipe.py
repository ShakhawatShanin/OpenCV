import math
import cv2 as cv
import numpy as np
import mediapipe as mp
counter = 0

def findAngle(landmark1, landmark2, landmark3):
    x1, y1, _ = landmark1
    x2, y2, _ = landmark2   # origin
    x3, y3, _ = landmark3
    angle = math.degrees(math.atan2(y3 - y2, x3 - x2) - math.atan2(y1 - y2, x1 - x2))
    if angle < 0:
        angle += 360

    return angle

vdo = cv.VideoCapture('Resources/exercise.mp4')
mp_draw = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, min_tracking_confidence=0.5)
landmarks = []

while True:
    ret, frame = vdo.read()
    if not ret:
        break
    h, w, _ = frame.shape
    frame = cv.resize(frame, (w//5, h//5))

    # STORE COORDINATE AT LANDMARKS LIST
    results = pose.process(cv.cvtColor(frame, cv.COLOR_BGR2RGB))
    if results.pose_landmarks:
        for landmark in results.pose_landmarks.landmark:
            landmarks.append((int(landmark.x * w), int(landmark.y * h), (landmark.z * w)))

    # GET ANGLE
    landmark1 = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value]
    landmark2 = landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value]
    landmark3 = landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value]
    right_elbow_angle = findAngle(landmark1, landmark2, landmark3)
    right_elbow_angle = int(right_elbow_angle)

    # COUNT SYSTEM
    if right_elbow_angle > 70:
        direction = "down"
    if right_elbow_angle < 70 and direction == 'down':
        direction = "up"
        counter += 1

    # DRAW SPECIFIC LANDMARK POSE
    cv.line(frame, (landmark1[0]//5, landmark1[1]//5), (landmark2[0]//5, landmark2[1]//5), (255, 255, 255), 8)
    cv.line(frame, (landmark3[0]//5, landmark3[1]//5), (landmark2[0]//5, landmark2[1]//5), (255, 255, 255), 8)
    cv.circle(frame, (landmark1[0]//5, landmark1[1]//5), 15, (0, 0, 255), -1)
    cv.circle(frame, (landmark2[0]//5, landmark2[1]//5), 15, (0, 0, 255), -1)
    cv.circle(frame, (landmark3[0]//5, landmark3[1]//5), 15, (0, 0, 255), -1)
    cv.putText(frame, str(right_elbow_angle), ((landmark2[0]//5)+15, landmark2[1]//5), cv.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 3)

    cv.rectangle(frame, (5, 5), (165, 55), (255, 255, 255), cv.FILLED)  # BOX DRAW
    cv.putText(frame, 'COUNT: ', (10, 35), cv.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 3)  # COUNT STRING
    cv.putText(frame, str(counter), (135, 35), cv.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 3)  # COUNT VARIABLE VALUE

    cv.imshow('Exercise', frame)
    landmarks.clear()
    k = cv.waitKey(1) & 0xff
    if k == ord('q'):
        break

vdo.release()
cv.destroyAllWindows()
