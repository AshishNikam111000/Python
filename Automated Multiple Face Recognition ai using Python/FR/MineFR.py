import face_recognition
import cv2
import numpy as np

video = cv2.VideoCapture(0)

image = face_recognition.load_image_file("Ashish.jpg")
image_encoding = face_recognition.face_encodings(image)[0]

while True:
    ret, frame = video.read()
    small_frame = cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]

    face_location = face_recognition.face_locations(rgb_small_frame)
    face_encoding = face_recognition.face_encodings(rgb_small_frame,face_location)

    for face_encode in face_encoding:
        matches = face_recognition.compare_faces([image_encoding],face_encode)
        name = "Ashish"

        #face_dist = face_recognition.face_distance([image_encoding],face_encode)
        #best_match = np.argmin(face_dist)
        if (matches[0]):
            print("Match Found")

    for t, r, b, l in face_location:
        t *= 4
        r *= 4
        b *= 4
        l *= 4

        cv2.rectangle(frame,(l,t),(r,b),(255,0,0),2)
        cv2.rectangle(frame,(l,b-35),(r,b),(0,0,255),cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame,name,(l+6, b-6),font,1.0,(255,255,255),1)

    cv2.imshow("VideoFrame", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


video.release()
cv2.destroyAllWindows()