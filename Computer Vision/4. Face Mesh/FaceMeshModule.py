import cv2
import mediapipe as mp

class FaceMeshDectector():
    def __init__(self, mode=False, maxFaces=2, minDetectionCon=0.5, minTrackCon=0.5):
        self.mode = mode
        self.maxFaces = maxFaces
        self.minDetectionCon = minDetectionCon
        self.minTrackCon = minTrackCon

        self.mpDraw = mp.solutions.drawing_utils
        self.mpFaceMesh = mp.solutions.face_mesh
        self.FaceMesh = self.mpFaceMesh.FaceMesh(self.mode, self.maxFaces, self.minDetectionCon, self.minTrackCon)
        self.drawSpec = self.mpDraw.DrawingSpec(thickness=1, circle_radius=2)



    def FindFaceMesh(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.FaceMesh.process(imgRGB)
        faces = []
        
        if results.multi_face_landmarks:
            for faceLms in results.multi_face_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, faceLms, self.mpFaceMesh.FACE_CONNECTIONS, self.drawSpec, self.drawSpec)
                face = []
                for id, lm in enumerate(faceLms.landmark):
                    h, w, c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    # cv2.putText(img, str(id), (cx, cy), cv2.FONT_HERSHEY_PLAIN, 0.3, (0, 255, 0), 1)

                    face.append([cx, cy])
                faces.append(face)
        return img, faces


    