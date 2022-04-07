#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2 as cv
import numpy as np


# In[3]:


src = cv.imread("pug.jpg")
src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY) # convert image to gray
# src_gray = cv.imread("pug.jpg", 0) it is also a gray image

# histogram equalization
equ = cv.equalizeHist(src_gray)

cv.imshow("gray", src_gray)
cv.imshow("equ gray", equ)
cv.waitKey(0)
cv.destroyAllWindows()
cv.waitKey(1)


# In[56]:


# Sharpening (Highpass) filter
# kernel = np.array([
#     [0, -1, 0],
#     [-1, 5, -1],
#     [0, -1, 0]
# ])

# 
# kernel = np.array([
#     [-1, -1, -1],
#     [-1, 8, -1],
#     [-1, -1, -1]
# ])

# kernel = np.array([
#     [1, 1, 1],
#     [1, 1, 1],
#     [1, 1, 1]
# ]) / 9


# kernel = np.array([
#     [-2, -1, 0],
#     [-1, 1, 1],
#     [0, 1, 2]
# ]) 

# kernel = np.array([
#     [-1, 0, 1],
#     [-2, 0, 2],
#     [-1, 0, 1]
# ])


# Gaussian kernel
# kernel = np.array([
#     [1, 2, 1],
#     [2, 4, 2],
#     [1, 2, 1],
# ]) / 16


kernel = np.array([
    [-1, 0, 1, -1, 0, 1, -1, 0, 1, 0],
    [-2, 0, 2, -2, 0, 2, -2, 0, 2, 1],
    [ 0, 0, 1, -1, 1, 1,  0, 0, 1, 1],
    [-1, 0, 1, -1, 0, 1, -1, 0, 1, 0],
    [-2, 0, 2, -2, 0, 2, -2, 0, 2, 1],
    [ 0, 0, 1, -1, 0, 1, -1, 0, 1, 1],
    [-1, 0, 1, -1, 1, 1, -1, 0, 1, 0],
    [-2, 0, 2, -2, 0, 1,  3, 2, 1, 1],
    [-1, 0, 1, -1, 0, 1, -1, 0, 1, 1],
    [ 0, 0, 1, -1, 1, 1, -1, 0, 1, 1]
]) / 10

filtered_img = cv.filter2D(src, -1, kernel)

# filtered_img = cv.medianBlur(src, 5)

cv.imshow("original image", src)
cv.imshow("filtered image", filtered_img)
cv.waitKey(0)
cv.destroyAllWindows()
cv.waitKey(1)


# In[ ]:




