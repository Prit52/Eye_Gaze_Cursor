import cv2
cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) == 27:
        break
cap.release()
cv2.destroyAllWindows() 
