import cv2
import time
from gaze_tracking import GazeTracking
import pyautogui as pag

gaze = GazeTracking()
cam = cv2.VideoCapture(0)
drag = 18
t = 0

while True:
    # We get a new frame from the webcam
    _, frame = cam.read()

    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)

    frame = gaze.annotated_frame()
    text = ""

    if gaze.is_blinking():
        text = "Blinking"
        t += 1
        time.sleep(0.1)
        if t == 5:
            pag.click(button='left')
            t = 0
    elif gaze.is_right():
        text = "Looking right"
        pag.moveRel(drag, 0)
    elif gaze.is_left():
        text = "Looking left"
        pag.moveRel(-drag, 0)
    elif gaze.is_center():
        text = "Looking center"
    elif gaze.is_top():
        text = "Looking Top"
        pag.moveRel(0, -drag)
    elif gaze.is_bottom():
        text = "Looking Bottom"
        pag.moveRel(0, drag)

    cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (0, 0, 255), 2)

    cv2.imshow("Demo", frame)

    if cv2.waitKey(1) == 27:
        break
