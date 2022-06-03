#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import cv2
import matplotlib.pyplot as plt
import math


# In[ ]:


img = cv2.imread("images/rectangle2.png")
plt.imshow(img, cmap= "gray")


# In[ ]:


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
dst = cv2.Canny(gray, 50, 200, None, 3)
plt.imshow(dst, cmap= "gray")


# In[ ]:


dstp = np.copy(img)
lines = cv2.HoughLines(dst, 1, np.pi/ 180, 90, None, 0, 0)

if lines is not None:
    for i in range(0, len(lines)):
        rho = lines[i][0][0]
        theta = lines[i][0][1]
        a = math.cos(theta)
        b = math.sin(theta)
        x0 = a*rho
        y0 = b* rho
        point1 = (int(x0+500*(-b)), int(y0+500*(a)))
        point2 = (int(x0-500*(-b)), int(y0-500*(a)))
        cv2.line(dstp, point1, point2, (0,0,255), 3, cv2.LINE_AA) # antialiasing


cv2.imshow("source", dst)
cv2.imshow("detected", dstp)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:


lines.shape


# In[ ]:


linesP = cv2.HoughLinesP(dst, 1, np.pi / 180, 50, None, 50, 10)
if linesP is not None:
    for i in range(0, len(linesP)):
        l = linesP[i][0]
        cv2.line(dstp, (l[0], l[1]), (l[2], l[3]), (0,0,255), 3, cv2.LINE_AA)

cv2.imshow("Source", gray)
cv2.imshow("Detected Lines (in red) - Probabilistic Line Transform", dstp)
cv2.waitKey(0) 
cv2.destroyAllWindows()


# In[ ]:


src = cv2.imread('images/Hough_circle.png')
src_original= np.copy(src)
gray = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY) 
rows = gray.shape[0]

# outer circle
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, rows / 8, param1=100, param2=30,
                            minRadius=28, maxRadius=100)

# inner circle
circles2 = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, rows / 8, param1=100, param2=30,
                            minRadius=1, maxRadius=60)

if circles is not None:
    circles = np.uint16(np.around(circles)) 
    for i in circles[0, :]:
        center = (i[0], i[1])
        # circle center
        cv2.circle(src, center, 1, (0, 0, 0), 15)
        # circle outline
        radius = i[2]
        cv2.circle(src, center, radius, (0, 0, 0), 15)

if circles2 is not None:
    circles2 = np.uint16(np.around(circles2)) 
    for i in circles2[0, :]:
        center = (i[0], i[1])
        # circle center
        cv2.circle(src, center, 1, (0, 0, 0), 15)
        # circle outline
        radius = i[2]
        cv2.circle(src, center, radius, (0, 0, 0), 15)

cv2.imshow("original", src_original) 
cv2.imshow("detected circles", src) 
cv2.waitKey(0) 
cv2.destroyAllWindows()

