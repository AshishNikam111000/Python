import cv2, time
import mediapipe as mp
from mediapipe.python.solutions import face_detection

cap = cv2.VideoCapture(0)
ptime = 0

mpFace = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
face_detection = mpFace.FaceDetection(0.75)



while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = face_detection.process(imgRGB)

    if results.detections:
        for id, detection in enumerate(results.detections):
            # mpDraw.draw_detection(img, detection)      // default drawing functions
            bb = detection.location_data.relative_bounding_box
            h, w, c = img.shape
            bbox = int(bb.xmin * w), int(bb.ymin * h), int(bb.width * w), int(bb.height * h)
            cv2.rectangle(img, bbox, (0, 255, 0), 3)
            cv2.putText(img, f'{int(detection.score[0] * 100 )}%', (bbox[0], bbox[1]-20), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)


    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime = ctime

    cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 5)
    cv2.imshow('Image', img)
    cv2.waitKey(1)