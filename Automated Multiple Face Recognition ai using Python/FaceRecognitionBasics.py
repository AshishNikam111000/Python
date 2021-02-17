import cv2
import cmake, dlib
import face_recognition

while True:
    
    image = cv2.imread("Photo.jpg")
    img = face_recognition.load_image_file("Photo.jpg")
    loc = face_recognition.face_locations(img)
    x = loc[0][3] ; y = loc[0][0]
    a = loc[0][1] ; b = loc[0][2]

    cv2.rectangle(image,(x,y),(a,b),(255,0,0),2)
    cv2.putText(image,"Ashish",(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),2)
    cv2.imshow("Test",image)

    features = face_recognition.face_landmarks(img)   #Every feature of the face
    known_en = face_recognition.face_encodings(img)[0]  #Encodes the known face
    
    #results = face_recognition.compare_faces([known_en],unknown_en)   #It compares faces and return boolean value

    if cv2.waitKey(1) == 27:
            break

