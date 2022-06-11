import cv2
import numpy as np

framewidth = 480
frameheight = 640
nplate_cascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')
count=0
cap = cv2.VideoCapture(0)
cap.set(3,framewidth)
cap.set(4,frameheight)
cap.set(10,150)



while True:
    _,img = cap.read()
    # img = cv2.imread('p1.jpg')
    imggray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    numberplates = nplate_cascade.detectMultiScale(imggray,1.1,4)
    for (x,y,w,h) in numberplates:
        area = w*h
        if area>500:
            cv2.rectangle(img,(x,y),(x+w,y+h), (255,0,0),3)
            cv2.putText(img,'number plate ', (x,y-5),cv2.FONT_ITALIC,2,(255,0,0),3)
            imageroi = img[y:y+h,x:x+w]
            cv2.imshow('imageroi',imageroi)

    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xff == ord('s'):
        cv2.imwrite('scanned/numberplate_'+str(count)+'.jpg',imageroi)
        cv2.rectangle(img, (0,200), (640,300), (0,255,0), -1)
        cv2.putText(img,"scan saved", (150,265),cv2.FONT_ITALIC,2,(0,0,255),3)
        cv2.imshow('img',img)
        cv2.waitKey(5)
        count+=1
        print(count)











