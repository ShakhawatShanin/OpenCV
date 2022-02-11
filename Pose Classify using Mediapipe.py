import math
import cv2 as cv
import numpy as np
import mediapipe as mp

def findAngle(landmark1, landmark2, landmark3):
    x1, y1, _ = landmark1
    x2, y2, _ = landmark2
    x3, y3, _ = landmark3
    angle = math.degrees(math.atan2(y3 - y2, x3 - x2) - math.atan2(y1 - y2, x1 - x2))
    if angle < 0:
        angle += 360
    return angle

def classifyPose():
    label = 'Unknown Pose'
    left_knee_angle = findAngle(landmarks[mp_pose.PoseLandmark.LEFT_HIP.value],
                                landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value],
                                landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value])
    print(f'Left Knee Angle: ', left_knee_angle)

    right_knee_angle = findAngle(landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value],
                                 landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value],
                                 landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value])
    print(f'Right Knee Angle: ', right_knee_angle)

    if (left_knee_angle > 165 and left_knee_angle < 195) and (right_knee_angle > 165 and right_knee_angle < 195):
        label = 'T Pose'

    cv.putText(img, label, (10, 30), cv.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)

mp_draw = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.5, min_tracking_confidence=0.5)

img = cv.imread('Resources/Warrior-Pose.jpg')
h, w, _ = img.shape
results = pose.process(cv.cvtColor(img, cv.COLOR_BGR2RGB))

landmarks = []
if results.pose_landmarks:
    mp_draw.draw_landmarks(img, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
    for landmark in results.pose_landmarks.landmark:
        landmarks.append((int(landmark.x * w), int(landmark.y * h), (landmark.z * w)))

classifyPose()

cv.imshow('Image', img)
cv.waitKey(0)
