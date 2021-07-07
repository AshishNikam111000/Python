import cv2, time
import FaceMeshModule as fh

def main():
    cap = cv2.VideoCapture(0)
    ptime = 0
    detector = fh.FaceMeshDectector()

    while True:
        success, img = cap.read()


        img, faces = detector.FindFaceMesh(img)
        if len(faces) != 0:
            print(len(faces))

        ctime = time.time()
        fps = 1/(ctime-ptime)
        ptime = ctime
        
        cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)
        cv2.imshow('FaceMesh', img)
        if cv2.waitKey(1) and 0xFF == ord('q'):
            break


if __name__=="__main__":
    main()