import cv2
import dlib

cap = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()
while True:
   ret, frame = cap.read()
   gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   faces = detector(gray)
   for face in faces:
       x1, y1 = face.left(), face.top()
       x2, y2 = face.right(), face.bottom()
       cv2.rectangle(frame,(x1, y1),(x2, y2),(0, 255, 0),2)
   cv2.imshow("Frame", frame)
   key = cv2.waitKey(1)
   if key == 27:
       break
cap.release()
cv2.destroyAllWindows()
