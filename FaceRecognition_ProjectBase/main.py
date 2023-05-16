import cv2
import cvzone
import os
import face_recognition
import pickle
import numpy as np
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
from datetime import datetime


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facerecognition-b9b88-default-rtdb.europe-west1.firebasedatabase.app/",
    'storageBucket': "facerecognition-b9b88.appspot.com"
})

bucket = storage.bucket()

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

imgBackground = cv2.imread('graphics/background.png')
folderModePath = 'graphics/Modes'
modePathList = os.listdir(folderModePath)
imgModeList = []
modeType = 0

file = open('EncodeFile.p', 'rb')
encodeListKnownWithIds = pickle.load(file)
file.close()
encodeListKnown, studentIds = encodeListKnownWithIds

for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath, path)))

#this is the initializing part so keep it here
modeType = 0
counter = 0
id = -1
imgStudent = []

while True:
    success, img = cap.read()

    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)

    imgBackground[157:157 + 480, 63:63 + 640] = img


    #The clock
    now = datetime.now()
    
    cv2.putText(imgBackground, now.strftime('%Y-%m-%d %H:%M:%S'), (782, 103),
                cv2.FONT_HERSHEY_DUPLEX, 0.6, (255, 85, 1), 2)

    #imgBackground[156:156 + 333, 768:768 + 455] =

    if modeType == 1:
        imgBackground[156:156 + 333, 768:768 + 455] = imgModeList[modeType]
    else:
        imgBackground[526:526 + 111, 768:768 + 455] = imgModeList[modeType]


    for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            bbox = 63 + x1, 157 + y1, x2 - x1, y2 - y1
            imgBackground = cvzone.cornerRect(imgBackground, bbox, rt=0)
            id = studentIds[matchIndex]

            if counter == 0:
                counter = 1
                modeType = 1

    if counter != 0:

            if counter == 1:

                studentInfo = db.reference(f'Students/{id}').get()
                print(studentInfo)

                blob = bucket.get_blob(f'Images\{id}.png')
                array = np.frombuffer(blob.download_as_string(), np.uint8)
                imgStudent = cv2.imdecode(array, cv2.COLOR_BGRA2BGR)
                #Update data of attendance, check is already
                ref = db.reference(f'Students/{id}')
                studentInfo['total_attendance'] +=1
                ref.child('total_attendance').set(studentInfo['total_attendance'])

                if 10<counter<20:
                    modeType = 2

                imgBackground[156:156 + 333, 768:768 + 455] = imgModeList[modeType] # MARKED

                if counter<=10:
                    cv2.putText(imgBackground, str(studentInfo['total_attendance']), (1152, 103),
                                cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 255, 255), 2)

                    cv2.putText(imgModeList[1], str("ID : "+id), (260, 109),
                                cv2.FONT_HERSHEY_DUPLEX, 0.8, (21, 21, 21),2)

                    cv2.putText(imgModeList[1], str("Name : "+studentInfo['name']), (50, 297),
                                cv2.FONT_HERSHEY_DUPLEX, 0.7, (21, 21, 21), 2)

                    #cv2.putText(imgBackground, str(id), (1013, 325),
                    #            cv2.FONT_HERSHEY_DUPLEX, 1, (21, 21, 21), 1)

                    #cv2.putText(imgBackground, str(studentInfo['name']), (1013, 260),
                    #            cv2.FONT_HERSHEY_DUPLEX, 1, (21, 21, 21), 1)

                    imgModeList[1][38:38 +185, 35:35 +185] = imgStudent



            counter += 1

            if counter >= 20:
                counter = 0
                modeType = 0
                studentInfo = []
                imgStudent = []
                #imgBackground[156:156 + 333, 768:768 + 455] = imgModeList[1]


    cv2.imshow("Face Recognition", imgBackground)
    cv2.waitKey(1)
