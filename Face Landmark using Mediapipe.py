import cv2 as cv
import mediapipe as mp   # find diff points on face
import time

# CREATE OBJECT
face_mesh_draw = mp.solutions.drawing_utils  # draw our faces
face_mesh_sol = mp.solutions.face_mesh       # get all face_mesh landmark (location)
face_mesh = face_mesh_sol.FaceMesh(max_num_faces=1)         # FaceMesh class

while True:
    img = cv.imread('Resources/shanin0.jpg')
    rgb_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_img)   # convert BGR image to RGB img

    print(results.multi_face_landmarks)   # print all the landmark

    if results.multi_face_landmarks:
        for each_face_lm in results.multi_face_landmarks:
            face_mesh_draw.draw_landmarks(img,
                                          each_face_lm,
                                          face_mesh_sol.FACEMESH_CONTOURS,
                                          landmark_drawing_spec=face_mesh_draw.DrawingSpec((0, 255, 0), 1, 1))

    cv.imshow('PICTURE', img)
    cv.waitKey(0)
