import cvzone
from cvzone.HandTrackingModule import HandDetector
import mediapipe as mp
import cv2
import serial
cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=1)
ser = serial.Serial('COM5', 9600)
while True:
    success, img = cap.read()
    hands,img = detector.findHands(img)
    
    if hands:
        #mano
        
        hand1=hands[0]
        lmList1=hand1["lmList"]
        bbox1=hand1["bbox"]
        centerPoint1=hand1["center"]
        handType=hand1["type"]
        fingers1=detector.fingersUp(hand1)
        
        print(fingers1)
        printear = ''.join(str(l) for l in fingers1)
        # ser.write(printear.encode())
        #print(printear)
        #print("Esto dice arduino", ser.read(5))
        #print(len(printear))
        #if fingers1==[11111]:
        if isinstance(fingers1, list) and fingers1 == [1, 1, 1, 1, 1]:
            #printear = ''.join(str(l) for l in fingers1)
            #ser.write(printear.encode('1'))
            ser.write(b'1')
            
        else:
           # ser.write(printear.encode('0'))
            ser.write(b'0')

            
        
        #print(len(lmList1))
        
 
    cv2.imshow("Image", img)
    cv2.waitKey(1)