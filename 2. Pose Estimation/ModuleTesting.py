import cv2, time
import PoseEstModule as pm

def main():
    cap = cv2.VideoCapture('Video/5.mp4')
    poseDectector = pm.PoseEstimation()
    ptime = 0

    while True:
        success, img = cap.read()

        if success:
            img = poseDectector.FindPose(img)
            lmList = poseDectector.FindPosition(img)

            if len(lmList) !=0:
                ctime = time.time()
                fps = 1/(ctime-ptime)
                ptime = ctime

                cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0))
                cv2.imshow('Video', img)
                cv2.waitKey(1)
        else:
            break

if __name__=='__main__':
    main()