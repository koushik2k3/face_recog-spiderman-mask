import numpy as np
import cv2
import matplotlib.pyplot as plt
from winsound import *

vid = cv2.VideoCapture(0)
spider = cv2.imread('spider.png')  
img_height, img_width, _ = spider.shape
frame_width  = vid.get(cv2.CAP_PROP_FRAME_WIDTH )
frame_height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT )
while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
    
    face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        frame[ y:y+img_height , x:x+img_width ] = spider
        roi_gray=gray[y:y+h, x:x+w]
        roi_color=frame[y:y+h, x:x+w]
    # Display the resulting frame
    cv2.imshow('frame', frame)
       
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()