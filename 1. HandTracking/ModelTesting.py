import mediapipe as mp
import cv2, time
import HandModule as htm
      
cap = cv2.VideoCapture(0)
ptime = 0
ctime = 0
detector = htm.HandDetector()

while True:
    success, img = cap.read()
    img = detector.FindHands(img)
    lmlist = detector.FindPos(img, draw=False)

    if len(lmlist) != 0:
        print(lmlist[4])

    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime = ctime
    cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 2)

    cv2.imshow("Image", img)
    cv2.waitKey(1)

