#!/usr/bin/env python
# coding: utf-8

# In[29]:


import cv2
import numpy as np

corrupted_img = cv2.imread('images/corrupted.png')

blurred_img = cv2.medianBlur(corrupted_img, 3)

kernel = np.array([[-1,-1,-1], 
                   [-1, 9,-1],
                   [-1,-1,-1]])

sharpened_img = cv2.filter2D(blurred_img, -1, kernel)

cv2.imwrite('images/repaired_img.png', sharpened_img)


# In[ ]:




