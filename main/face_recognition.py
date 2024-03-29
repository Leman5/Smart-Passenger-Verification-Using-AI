import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import time
from main.models import Ticket

# from PIL import ImageGrab
def findEncodings(images):
    encodeList = []


    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList




def mainverification():
    path = 'media/uid_pics'
    images = []
    classNames = []
    myList = os.listdir(path)
    print(myList)
    for cl in myList:
        curImg = cv2.imread(f'{path}/{cl}')
        images.append(curImg)
        classNames.append(os.path.splitext(cl)[0])
    print(classNames)



    #### FOR CAPTURING SCREEN RATHER THAN WEBCAM
    # def captureScreen(bbox=(300,300,690+300,530+300)):
    #     capScr = np.array(ImageGrab.grab(bbox))
    #     capScr = cv2.cvtColor(capScr, cv2.COLOR_RGB2BGR)
    #     return capScr

    encodeListKnown = findEncodings(images)
    print('Encoding Complete')

    cap = cv2.VideoCapture(0)

    verified_passenger = None
    

    t_end = time.time() + 10 * 6
    while time.time() < t_end:
        print("Inside While")
        success, img = cap.read()        
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
        print("Started Reading")

        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)
        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            print(faceDis)
            matchIndex = np.argmin(faceDis)


            if matches[matchIndex]:
                uid = classNames[matchIndex].upper()
                print(type(uid))
                verified_passenger = Ticket.objects.get(uid=uid)
                y1, x2, y2, x1 = faceLoc
                print('a')
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                print('b')
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                print('c')
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                print('d')
                if(verified_passenger.boarded == "True"):
                    cv2.putText(img, "Already Boarded", (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                    print('e in if ')
                    print('Face verified',uid)                  

                else:
                    cv2.putText(img, uid, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                    print('e in else')
                    print('Face verified',uid)
                
            else:
                unknown = "Unknown Passenger"
                
                y1, x2, y2, x1 = faceLoc
                print('a')
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                print('b')
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
                print('c')
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 0, 255), cv2.FILLED)
                print('d')
                cv2.putText(img, unknown, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                print("Face Not Verified")
        
        cv2.imshow('Webcam', img)
        if (cv2.waitKey(1)==ord('q')):
                break 
    cv2.destroyAllWindows()
    return verified_passenger
