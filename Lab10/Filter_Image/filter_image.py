#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imshow, imread
from skimage.color import rgb2hsv, hsv2rgb 
import cv2


# In[ ]:


red_girl = imread('RGirl.png') 
plt.figure(num=None, figsize=(8, 6), dpi=80) 
imshow(red_girl)


# In[ ]:


red_filtered_girl = (red_girl[:,:,0] > 150) 
plt.figure(num=None, figsize=(8, 6), dpi=80) 
imshow(red_filtered_girl, cmap = 'gray')


# In[ ]:


red_girl_new = red_girl.copy()
red_girl_new[:, :, 0] = red_girl_new[:, :, 0]*red_filtered_girl 
red_girl_new[:, :, 1] = red_girl_new[:, :, 1]*red_filtered_girl 
red_girl_new[:, :, 2] = red_girl_new[:, :, 2]*red_filtered_girl 
plt.figure(num=None, figsize=(8, 6), dpi=80) 
imshow(red_girl_new)


# In[ ]:


def rgb_splitter(image):
    rgb_list = ['Reds','Greens','Blues']
    fig, ax = plt.subplots(1, 3, figsize=(15,5), sharey = True) 
    for i in range(3):
        ax[i].imshow(image[:,:,i], cmap = rgb_list[i])
        ax[i].set_title(rgb_list[i], fontsize = 15) 
    
rgb_splitter(red_girl)


# In[ ]:


red_filtered = (red_girl[:,:,0] > 150) & (red_girl[:,:,1] < 100) & (red_girl[:,:,2] < 110)
plt.figure(num=None, figsize=(8, 6), dpi=80)
red_girl_new = red_girl.copy()
red_girl_new[:, :, 0] = red_girl_new[:, :, 0] * red_filtered
red_girl_new[:, :, 1] = red_girl_new[:, :, 1] * red_filtered 
red_girl_new[:, :, 2] = red_girl_new[:, :, 2] * red_filtered 
imshow(red_girl_new)


# In[ ]:


def display_as_hsv(image): 
    img = cv2.imread(image)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    hsv_list = ['Hue','Saturation','Value']
    fig, ax = plt.subplots(1, 3, figsize=(15,7), sharey = True)
    
    ax[0].imshow(img_hsv[:,:,0], cmap = 'hsv') 
    ax[0].set_title(hsv_list[0], fontsize = 20) 
    ax[0].axis('off')
    
    ax[1].imshow(img_hsv[:,:,1], cmap = 'Greys') 
    ax[1].set_title(hsv_list[1], fontsize = 20) 
    ax[1].axis('off')
    ax[2].imshow(img_hsv[:,:,2], cmap = 'gray') 
    ax[2].set_title(hsv_list[2], fontsize = 20) 
    ax[2].axis('off')
    
    fig.tight_layout() 

display_as_hsv('RGirl.png')


# In[ ]:


img = cv2.imread('RGirl.png')
red_girl_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) 
plt.figure(num=None, figsize=(8, 6), dpi=80) 
plt.imshow(red_girl_hsv[:,:,0], cmap='hsv') 
plt.colorbar()


# In[ ]:


lower_mask = red_girl_hsv [:,:,0] > 160 
upper_mask = red_girl_hsv [:,:,0] < 255 
mask = upper_mask*lower_mask
red = red_girl[:,:,0]*mask
green = red_girl[:,:,1]*mask
blue = red_girl[:,:,2]*mask
red_girl_masked = np.dstack((red,green,blue)) 
plt.figure(num=None, figsize=(8, 6), dpi=80) 
imshow(red_girl_masked)


# In[ ]:


lower_mask = red_girl_hsv [:,:,0] > 160 
upper_mask = red_girl_hsv [:,:,0] < 255 
saturation = red_girl_hsv [:,:,1] > 150 
mask = upper_mask*lower_mask*saturation 
red = red_girl[:,:,0]*mask
green = red_girl[:,:,1]*mask
blue = red_girl[:,:,2]*mask
red_girl_masked = np.dstack((red,green,blue)) 
plt.figure(num=None, figsize=(8, 6), dpi=80) 
imshow(red_girl_masked)


# In[ ]:




