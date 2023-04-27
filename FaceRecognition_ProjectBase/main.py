import cv2
import os

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

imgBackground = cv2.imread('graphics/background.png')
folderModePath = 'graphics/Modes'
modePathList = os.listdir(folderModePath)
imgModeList = []
modeType = 0

for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath, path)))

while True:
    success, img = cap.read()
    imgBackground[160:160 + 480, 55:55 + 640] = img
    imgBackground[70:70 + 570, 827:827 + 379] = imgModeList[modeType]
    cv2.imshow("Face Recognition", imgBackground)
    cv2.waitKey(1)