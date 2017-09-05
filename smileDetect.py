import cv2
import numpy as np
import sys
from time import gmtime, strftime
from decimal import Decimal
import datetime

startRun = datetime.datetime.now()
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
smileCascade = cv2.CascadeClassifier("haarcascade_smile.xml")

cap = cv2.VideoCapture(0)  #0,1,2.. dokud se nenajde webka
cap.set(3, 640)
cap.set(4, 480)

sF = 1.05
frameCounter = 0
smileCounter = 0
faceCounter = 0
startTimeF = strftime("%Y-%m-%d_%Hh%Mm%Ss", gmtime())
startTime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
print 'Start: ', startTime
while True:
    frameTime = strftime("%Y-%m-%d_%Hh%Mm%Ss", gmtime())
    frameCounter += 1

    ret, frame = cap.read()  #Capture frame-by-frame
    img = frame
    cv2.imshow('jejedno', img)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor = sF,
        minNeighbors = 8,
        minSize = (55, 55),
        flags = cv2.cv.CV_HAAR_SCALE_IMAGE
    )
    # ---- Draw a rectangle around the faces

    for (x, y, w, h) in faces:
        faceCounter += 1
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        smile = smileCascade.detectMultiScale(
            roi_gray,
            scaleFactor= 1.7,
            minNeighbors=22,
            minSize=(25, 25),
            flags=cv2.cv.CV_HAAR_SCALE_IMAGE
            )

        # Set region of interest for smiles
        for (x, y, w, h) in smile:
            cv2.rectangle(roi_color, (x, y), (x+w, y+h), (255, 0, 0), 1)
            smileCounter += 1
            #print "!!!!!!!!!!!!!!!!!"

    #cv2.cv.Flip(frame, None, 1)
    cv2.imshow('Smile Detector', frame)
    cv2.imwrite('./webcam_pics/' + frameTime + '.jpg', gray)

    c = cv2.cv.WaitKey(7) % 0x100
    if c == 27:
        break
stopRun=datetime.datetime.now()
stopTime=strftime("%Y-%m-%d %H:%M:%S", gmtime())
if faceCounter>0:
    smileFaceRatio=smileCounter/float(faceCounter)
else:
    smileFaceRatio=Decimal('nan')
delkaExperimentu=(stopRun-startRun).seconds
print 'Stop: ', stopTime
print 'Frame count:', frameCounter
print 'Number of detected faces: ', faceCounter
print 'Number of detected smiles: ', smileCounter
print 'Smile to face ratio: ', smileFaceRatio
print 'Python version: ',(sys.version)

f=open('f_%s.txt' % startTimeF, 'a')
f.write('Zacatek experimentu: %s\n' % startTime)
f.write('Konec experimentu: %s\n' % stopTime)
f.write('Delka experimentu:%s' % str(delkaExperimentu / 60))
f.write('m %s' % str(delkaExperimentu%60))
f.write('s\n')
f.write('Pocet porizenych snimku: %s\n' % frameCounter)
f.write('Pocet ulozenych snimku')
f.write('Pocet snimku s detekovanym oblicejem: %s\n' % faceCounter)
f.write('Pocet snimku s detekovanym oblicejem a usmevem: %s\n' % smileCounter)
f.write('Detekovany usmev / Detekovany oblicej: %s\n' %smileFaceRatio)
cap.release()
cv2.destroyAllWindows()