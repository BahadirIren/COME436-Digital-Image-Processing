#!/usr/bin/env python
# coding: utf-8

# In[ ]:


conda install scikit-image


# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread, imshow
from skimage.color import rgb2hsv, rgb2gray, rgb2yuv 
from skimage import color, exposure, transform
from skimage.exposure import equalize_hist


# In[ ]:


dark_image = imread('images/against_the_light.png')


# In[ ]:


dark_image_grey = rgb2gray(dark_image) 
plt.figure(num=None, figsize=(8, 6), dpi=80) 
plt.imshow(dark_image_grey, cmap='gray')


# In[ ]:


dark_image_grey_fourier = np.fft.fftshift(np.fft.fft2(dark_image_grey)) 
plt.figure(num=None, figsize=(8, 6), dpi=80) 
plt.imshow(np.log(abs(dark_image_grey_fourier)), cmap='gray')


# In[ ]:


def fourier_masker_ver(image, i): 
    f_size = 15
    
    dark_image_grey_fourier = np.fft.fftshift(np.fft.fft2(rgb2gray(image))) 
    dark_image_grey_fourier[:225, 235:240] = i 
    dark_image_grey_fourier[-225:,235:240] = i
    
    fig, ax = plt.subplots(1,3,figsize=(15,15)) 
    
    ax[0].imshow(np.log(abs(dark_image_grey_fourier)), cmap='gray') 
    ax[0].set_title('Masked Fourier', fontsize = f_size) 
    
    ax[1].imshow(rgb2gray(image), cmap = 'gray')
    ax[1].set_title('Greyscale Image', fontsize = f_size)
    
    ax[2].imshow(abs(np.fft.ifft2(dark_image_grey_fourier)), cmap='gray') 
    ax[2].set_title('Transformed Greyscale Image', fontsize = f_size)
    
fourier_masker(dark_image, 1)


# In[ ]:


arr = [10, 20, 30, 40, 50] 
print (arr[-2:])


# In[ ]:


def fourier_masker_hor(image, i):
    f_size = 15
    
    dark_image_grey_fourier = np.fft.fftshift(np.fft.fft2(rgb2gray(image))) 
    dark_image_grey_fourier[235:240, :230] = i
    dark_image_grey_fourier[235:240,-230:] = i
    
    fig, ax = plt.subplots(1,3,figsize=(15,15)) 
    
    ax[0].imshow(np.log(abs(dark_image_grey_fourier)), cmap='gray') 
    ax[0].set_title('Masked Fourier', fontsize = f_size) 
    
    ax[1].imshow(rgb2gray(image), cmap = 'gray')
    ax[1].set_title('Greyscale Image', fontsize = f_size)
    
    ax[2].imshow(abs(np.fft.ifft2(dark_image_grey_fourier)), cmap='gray') 
    ax[2].set_title('Transformed Greyscale Image', fontsize = f_size)
    
fourier_masker_hor(dark_image, 1)


# In[ ]:


def fourier_iterator(image, value_list): 
    for i in value_list:
        fourier_masker_ver(image, i)
        
fourier_iterator(dark_image, [0.001, 1, 100])


# In[ ]:


def fourier_transform_rgb(image):
    f_size = 25
    transformed_channels = [] 
    for i in range(3):
        rgb_fft = np.fft.fftshift(np.fft.fft2((image[:, :, i]))) 
        rgb_fft[:225, 235:237] = 1
        rgb_fft[-225:,235:237] = 1 
        transformed_channels.append(abs(np.fft.ifft2(rgb_fft)))

    final_image = np.dstack([transformed_channels[0].astype(int), 
                             transformed_channels[1].astype(int),
                             transformed_channels[2].astype(int)])
    
    fig, ax = plt.subplots(1, 2, figsize=(17,12)) 
    ax[0].imshow(image)
    ax[0].set_title('Original Image', fontsize = f_size) 
    ax[0].set_axis_off()
    
    ax[1].imshow(final_image)
    ax[1].set_title('Transformed Image', fontsize = f_size) 
    ax[1].set_axis_off()
    
    fig.tight_layout()


# In[ ]:


fourier_transform_rgb(dark_image)


# In[ ]:




