import cv2
import cmake, dlib
import face_recognition

while True:
        
    image = cv2.imread("Photo.jpg")
    #cv2.imshow("Color",image)
    #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY);cv2.imshow("Gray",gray)  
    #hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV);cv2.imshow("HSV",hsv)

    #edge = cv2.Canny(image,5,500); cv2.imshow("Color",edge)        #Edge Detection


    if cv2.waitKey(1) == 27:
            break

