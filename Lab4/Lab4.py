#!/usr/bin/env python
# coding: utf-8

# In[3]:


import cv2 as cv


# In[6]:


img_boji = cv.imread("images/boji.jpg")

img_boji.shape


# In[30]:


# show boji image
cv.imshow("boji", img_boji)
cv.waitKey(0)
cv.destroyAllWindows()
cv.waitKey(1)


# In[8]:


# resize image 

dimension = (int((img_boji.shape[1] / 2)), int((img_boji.shape[0] / 2)))

resized_img_boji = cv.resize(img_boji, dimension, interpolation = cv.INTER_AREA)
# resized_img_boji.shape

cv.imshow("resized boji", resized_img_boji)
cv.waitKey(0)
cv.destroyAllWindows()
cv.waitKey(1)


# In[74]:


# red color
# resized_img_boji[200:300,0:100, 0] = 0
# resized_img_boji[200:300,0:100, 1] = 0
# resized_img_boji[200:300,0:100, 2] = 255

# green color
# resized_img_boji[200:300,0:100, 0] = 0
# resized_img_boji[200:300,0:100, 1] = 255
# resized_img_boji[200:300,0:100, 2] = 0

# blue color
# resized_img_boji[200:300,0:100, 0] = 255
# resized_img_boji[200:300,0:100, 1] = 0
# resized_img_boji[200:300,0:100, 2] = 0

# white color
# resized_img_boji[200:300,0:100, 0] = 255
# resized_img_boji[200:300,0:100, 1] = 255
# resized_img_boji[200:300,0:100, 2] = 255


# In[9]:


# adding squares to the corners of the image

height = int(resized_img_boji.shape[0])
width = int(resized_img_boji.shape[1])

# top left corner
resized_img_boji[0:50, 0:50, 0] = 255
resized_img_boji[0:50, 0:50, 1] = 255
resized_img_boji[0:50, 0:50, 2] = 255

# top right corner
resized_img_boji[ 0:50 , (width -50): width, 0] = 255
resized_img_boji[ 0:50 ,(width -50): width, 1] = 255
resized_img_boji[ 0:50 ,(width -50): width, 2] = 255

# bottom left corner
resized_img_boji[ (height - 50):height ,0:50, 0] = 255
resized_img_boji[ (height - 50):height ,0:50, 1] = 255
resized_img_boji[ (height - 50):height ,0:50, 2] = 255


# bottom right corner
resized_img_boji[ (height - 50):height , (width -50):width, 0] = 255
resized_img_boji[ (height - 50):height ,(width -50): width, 1] = 255
resized_img_boji[ (height - 50):height ,(width -50): width, 2] = 255

cv.imshow("square", resized_img_boji)
cv.waitKey(0)
cv.destroyAllWindows()
cv.waitKey(1)


# In[26]:


# gray colored image

grayscale = cv.cvtColor(resized_img_boji, cv.COLOR_BGR2GRAY)

cv.imshow("gray image", grayscale)
cv.waitKey(0)
cv.destroyAllWindows()
cv.waitKey(1)


# In[ ]:


conda install matplotlib


# In[1]:


import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


# In[12]:


fig, axs = plt.subplots()
fig.suptitle("Matplotlib test", fontsize =16)
axs.imshow(cv.cvtColor(resized_img_boji, cv.COLOR_BGR2RGB))


# In[21]:


fig, axs = plt.subplots(1,2)

axs[0].imshow(cv.cvtColor(resized_img_boji, cv.COLOR_BGR2RGB))
axs[1].imshow(cv.cvtColor(grayscale, cv.COLOR_BGR2RGB))


# In[35]:


fig, axs = plt.subplots(2,2)

axs[0,0].imshow(cv.cvtColor(resized_img_boji, cv.COLOR_BGR2RGB))
axs[0,1].imshow(cv.cvtColor(gray1, cv.COLOR_BGR2RGB))
axs[1,0].imshow(cv.cvtColor(gray2, cv.COLOR_BGR2RGB))
axs[1,1].imshow(cv.cvtColor(gray3, cv.COLOR_BGR2RGB))


# In[42]:


fig, axs = plt.subplots(3,2)

gray1 = resized_img_boji[:,:,0]
gray2 = resized_img_boji[:,:,1]
gray3 = resized_img_boji[:,:,2]

(r,g,b) = cv.split(resized_img_boji)
gray4 = 0.2989 * r + 0.5870 * g + 0.1140 * b
gray5 = 0.33 * r + 0.33 * g + 0.33 * b

axs[0,0].imshow(cv.cvtColor(resized_img_boji, cv.COLOR_BGR2RGB))
axs[0,1].imshow(cv.cvtColor(gray1, cv.COLOR_BGR2RGB))
axs[1,0].imshow(cv.cvtColor(gray2, cv.COLOR_BGR2RGB))
axs[1,1].imshow(cv.cvtColor(gray3, cv.COLOR_BGR2RGB))
axs[2,0].imshow(cv.cvtColor(np.uint8(gray4), cv.COLOR_BGR2RGB)) # we should convert to uint8
axs[2,1].imshow(cv.cvtColor(np.uint8(gray5), cv.COLOR_BGR2RGB)) # we should convert to uint8


# In[46]:


# resimleri ic ice gecirme
img1 = cv.imread("images/girl.png")
img2 = cv.imread("images/monarch.png")

dst = cv.addWeighted(img1, 0.3, img2, 0.7,100) 

cv.imshow("dst", dst)
cv.waitKey(0)
cv.destroyAllWindows()
cv.waitKey(1)


# In[50]:


fig, axs = plt.subplots(2,2)

img1 = cv.imread("images/girl.png")
img2 = cv.imread("images/monarch.png")

dst1 = cv.addWeighted(img1, 0.3, img2, 0.7, 100) # take 0.3 from img1 and take 0.7 from img2
dst2 = cv.addWeighted(img1, 0.7, img2, 0.3, 0)

axs[0,0].imshow(cv.cvtColor(img1, cv.COLOR_BGR2RGB))
axs[0,1].imshow(cv.cvtColor(img2, cv.COLOR_BGR2RGB))
axs[1,0].imshow(cv.cvtColor(dst1, cv.COLOR_BGR2RGB))
axs[1,1].imshow(cv.cvtColor(dst2, cv.COLOR_BGR2RGB))


# In[ ]:




