#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np


# In[3]:


np.zeros((3,4))


# In[4]:


np.ones((2, 3, 4), dtype = np.int16)


# In[6]:


np.ones((2, 3, 4), dtype = np.float64)


# In[9]:


x = np.ones((2, 3, 4), dtype = np.float64)

x.itemsize


# In[10]:


y = np.ones((2, 3, 4), dtype = np.int16)

y.itemsize


# In[15]:


np.arange(15).reshape(5,3)


# In[16]:


np.linspace(0, 2, 9) # starting, ending, element number 


# In[17]:


A = np.array([[1,1],[0,1]])
A


# In[18]:


B = np.array([[2,0],[3,4]])
B


# In[19]:


# element wise multiplication
A*B 


# In[21]:


# matrix multiplication
A@B
A.dot(B)


# In[22]:


# matrix addition
C = A + B
C


# In[25]:


# random array with size 3x4
D = np.random.rand(3,4)
D


# In[26]:


D.shape


# In[14]:


import cv2 as cv


# In[4]:


image = cv.imread('../Homework1/images/image1.jpg', 1)
image.shape


# In[7]:


image_gray = cv.imread('../Homework1/images/image1.jpg', 0)
image_gray.shape


# In[5]:


cv.imshow('image gray', image)

cv.waitKey(0)
cv.destroyAllWindows()
cv.waitKey(1)


# In[8]:


cv.imshow('image gray', image_gray)

cv.waitKey(0)
cv.destroyAllWindows()
cv.waitKey(1)


# In[59]:


A1 = np.zeros((300, 300,3), dtype = np.int16)


# In[60]:


A1[1:100,:,0]= 255


# In[61]:


cv.imshow('image', A1)

cv.waitKey(0)
cv.destroyAllWindows()
cv.waitKey(1)


# In[ ]:





# In[27]:


A_image = [0*A1, 127*A1]


# In[48]:


gray_level = 127


# In[50]:


gray_image = 0* np.ones((400,500,3), dtype = np.uint8)


# In[51]:


gray_image1 = 0* np.ones((400,500,3), dtype = np.uint8)


# In[53]:


for i in range(0,410,200):
    gray_image[:,i:i+50,0] = 255
    gray_image[:,i+50:i+100,1] = 255
    gray_image[:,i+150:i+200,2] = 255


# In[54]:


cv.imshow('image gray', gray_image)

cv.waitKey(0)
cv.destroyAllWindows()
cv.waitKey(1)


# In[55]:


n_im = gray_image[:,:,0]

cv.imshow('image gray', n_im)

cv.waitKey(0)
cv.destroyAllWindows()
cv.waitKey(1)


# In[58]:


n_im1 = image[:,:,0]

cv.imshow('image gray', n_im1)

cv.waitKey(0)
cv.destroyAllWindows()
cv.waitKey(1)


# In[67]:


im_second = cv.imread('../Homework1/images/image2.jpg')
cv.imshow('Second Image', im_second)

cv.waitKey(0)
cv.destroyAllWindows()
cv.waitKey(1)


# In[68]:


# drowing line
cv.line(im_second, (0,0), (100,251), (255,0,0), 30) # starting point, ending point, color, thickness
cv.line(im_second, (0,512), (251,251), (0,0,255), 30)
cv.imshow('second image', im_second)

cv.waitKey(0)
cv.destroyAllWindows()
cv.waitKey(1)


# In[72]:


# write to the local storage

is_written = cv.imwrite('new_image_second.jpg',im_second)

if is_written:
    print('successfully written')
else:
    print('failed!')


# In[80]:


height = int(im_second.shape[0] * 50 / 100)
width = int(im_second.shape[1] * 50 / 100)

dimension = (width, height)

resized_image = cv.resize(im_second, dimension, interpolation = cv.INTER_AREA)

resized_image.shape

cv.imshow('Scaled Image', resized_image)

cv.waitKey(0)
cv.destroyAllWindows()
cv.waitKey(1)


# In[ ]:




