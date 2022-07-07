import cv2
import numpy as np
#img=cv2.imread("Resources/CAr_image.jfif")

#mg1=cv2.resize(img,(1000,500))
#cv2.imshow("output",img1)
#imgHSV=cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)
#cv2.imshow("HSV_IMAGE",imgHSV)

#trackbars
def empty(a):
    pass
#create window for trackbars
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar("Hue-min","TrackBars",0,179,empty)
cv2.createTrackbar("Hue-max","TrackBars",179,179,empty)
cv2.createTrackbar("Sat-min","TrackBars",0,255,empty)
cv2.createTrackbar("Sat-max","TrackBars",255,255,empty)
cv2.createTrackbar("val-max","TrackBars",255,255,empty)
cv2.createTrackbar("val-min","TrackBars",0,255,empty)

while True:

    img1=cv2.imread("Resources/photo.jpeg")
    img=cv2.resize(img1,(640,600))

    imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min=cv2.getTrackbarPos("Hue-min","TrackBars")
    h_min = cv2.getTrackbarPos("Hue-min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue-max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat-min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat-max", "TrackBars")
    v_min = cv2.getTrackbarPos("val-min", "TrackBars")
    v_max = cv2.getTrackbarPos("val-max", "TrackBars")
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower=np.array([h_min,s_min,v_min])
    upper=np.array([h_max,s_max,v_max])
    mask=cv2.inRange(imgHSV,lower,upper)
    cv2.imshow("Orignal", img)
    cv2.imshow("mask", mask)

   # cv2.imshow("HSV",imgHSV)

    cv2.waitKey(1)
cv2.waitKey(0)
