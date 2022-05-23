#!/usr/bin/env python
# coding: utf-8

# In[6]:


import cv2
import numpy as np


# In[ ]:


# all cv2 color functions
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print(flags)


# In[7]:


green = np.uint8([[[0, 255, 0]]])


# In[8]:


hsv_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)


# In[9]:


hsv_green


# In[13]:


lower_red = np.array([150, 150, 0])
upper_red = np.array([180, 255, 255])


# In[ ]:


cap = cv2.VideoCapture(0) # 0 internal camera

while(1):
    _,frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_red, upper_red)
    result = cv2.bitwise_and(frame, frame, mask = mask)
    
    cv2.imshow('HSV', hsv)
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('result', result)
    
    k = cv2.waitKey(5) & 0xFF
    
    if k == 27: # if user pressed escape button on keyboard
        break
        
cap.release()   
cv2.waitKey(1)
cv2.destroyAllWindows()
cv2.waitKey(1)


# In[ ]:




