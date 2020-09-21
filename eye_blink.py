import cv2
import dlib
from math import hypot 

cap = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(gray)
    for face in faces:

        landmarks = predictor(gray, face)

        for n in range(36, 47):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            cv2.circle(frame, (x, y), 4, (255, 0, 0), -1)

            landmarks = predictor(gray, face)

            # right Eye
            r_left_point = (landmarks.part(36).x, landmarks.part(36).y)
            r_right_point = (landmarks.part(39).x, landmarks.part(39).y)
            r_center_top = (int((landmarks.part(37).x + landmarks.part(38).x) / 2),
                            int((landmarks.part(37).y + landmarks.part(38).y) / 2))
            r_center_bottom = (int((landmarks.part(40).x + landmarks.part(41).x) / 2),
                               int((landmarks.part(40).y + landmarks.part(41).y) / 2))
            r_hor_line = cv2.line(frame, r_left_point, r_right_point, (0, 255, 0), 2)
            r_ver_line = cv2.line(frame, r_center_top, r_center_bottom, (0, 255, 0), 2)
            # left Eye
            l_left_point = (landmarks.part(42).x, landmarks.part(42).y)
            l_right_point = (landmarks.part(45).x, landmarks.part(45).y)
            l_center_top = (int((landmarks.part(43).x + landmarks.part(44).x) / 2),
                            int((landmarks.part(43).y + landmarks.part(44).y) / 2))
            l_center_bottom = (int((landmarks.part(46).x + landmarks.part(47).x) / 2),
                               int((landmarks.part(46).y + landmarks.part(47).y) / 2))
            l_hor_line = cv2.line(frame, l_left_point, l_right_point, (0, 255, 0), 2)
            l_ver_line = cv2.line(frame, l_center_top, l_center_bottom, (0, 255, 0), 2)
            # To predict the blink
            # we take the ratio oh horizontal and vertical lengths
            # right Eye
            r_hor_line_length = hypot((r_left_point[0] - r_right_point[0]), (r_left_point[1] - r_right_point[1]))
            r_ver_line_length = hypot((r_center_top[0] - r_center_bottom[0]), (r_center_top[1] - r_center_bottom[1]))
            r_ratio = r_hor_line_length / r_ver_line_length
            # Left eye
            l_hor_line_length = hypot((r_left_point[0] - l_right_point[0]), (l_left_point[1] - l_right_point[1]))
            l_ver_line_length = hypot((r_center_top[0] - l_center_bottom[0]), (l_center_top[1] - l_center_bottom[1]))
            l_ratio = l_hor_line_length / l_ver_line_length
            # use ratios to determine the blink
            # right eye blink
            print(l_ratio)
            #if r_ratio > 4.6:
               #cv2.putText(frame, "RIGHT BLINK", (50, 150), cv2.FONT_HERSHEY_DUPLEX, 3, (255, 0, 0))
            # left eye blink
            if l_ratio > 1.38:
                cv2.putText(frame, "LEFT BLINK", (150, 50), cv2.FONT_HERSHEY_DUPLEX, 3, (255, 0, 0))

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()
