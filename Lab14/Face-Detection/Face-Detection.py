#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import sys

cascPath = 'haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(cascPath)

videoCapture = cv2.VideoCapture(0)

while True:
    ret, frames = videoCapture.read()
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor = 1.1,
        minNeighbors = 5,
        minSize = (20,20),
        flags = cv2.CASCADE_SCALE_IMAGE
    )

    #Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frames, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Video", frames)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
videoCapture.release()
cv2.destroyAllWindows()

