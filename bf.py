import cvzone
from cvzone.HandTrackingModule import HandDetector
import mediapipe as mp
import cv2
import serial
cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=1)
ser = serial.Serial('COM21', 9600)
alto=str(101)
bajo=str(2)
previous_fingers1 = None
while True:
  success, img = cap.read()
  hands,img = detector.findHands(img)
  img = cv2.flip(img, 1)
  if hands:
    #mano   
    print(previous_fingers1)
    print("-----------------------")

    for hand in hands:
      fingers = detector.fingersUp(hand)
      if isinstance(fingers, list) and fingers == [1, 1, 1, 1, 1]:
        ser.write(b'1\n')
      elif  isinstance(fingers, list) and fingers == [0, 0, 0, 1, 1]:
        ser.write(b'2\n')
      elif  isinstance(fingers, list) and fingers == [1, 0, 0, 0, 0]:
        ser.write(b'3\n')
      elif  isinstance(fingers, list) and fingers == [0, 0, 0, 0, 0]:
        ser.write(b'4\n')

  if cv2.waitKey(1) & 0xFF == ord("q"):
    break

  cv2.imshow("Image", img)
  cv2.waitKey(1)