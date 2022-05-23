#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np


# In[4]:


def draw_circle(event, x, y, flasgs, param):
    
    if event ==  cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 100, (255, 0, 0), -1)
        
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x, y), 100, (0, 255, 0), -1)
    
    if event == cv2.EVENT_MOUSEMOVE:
        cv2.circle(img, (x, y), 15, (0, 0, 0), -1) 


# In[ ]:


img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)
while(1):
    cv2.imshow('image', img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()


# In[ ]:




