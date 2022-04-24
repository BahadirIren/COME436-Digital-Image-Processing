#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


# In[ ]:


x = np.arange(-500, 500, 1)
X, Y = np.meshgrid(x, x)
wavelength = 200
grating = np.sin(2 * np.pi * X / wavelength) 
plt.set_cmap("gray")
plt.imshow(grating)
plt.show()

# calculate the fourier transform of grating
ft = np.fft.ifftshift(grating)
ft = np.fft.fft2(ft)
ft = np.fft.fftshift(ft)
plt.subplot(122)
plt.imshow(abs(ft))
plt.xlim([480, 520])
plt.ylim([520, 480]) # note, order is reversed for y
plt.show()


# In[ ]:


x = np.arange(-500, 500, 1)
X, Y = np.meshgrid(x, x)
wavelength = 200
angle = np.pi / 9
grating = np.sin(2 * np.pi * (X * np.cos(angle) + Y * np.sin(angle)) / wavelength)
plt.set_cmap("gray")
plt.imshow(grating)
plt.show()

# calculate the fourier transform of grating
ft = np.fft.ifftshift(grating)
ft = np.fft.fft2(ft)
ft = np.fft.fftshift(ft)
plt.subplot(122)
plt.imshow(abs(ft))
plt.xlim([480, 520])
plt.ylim([520, 480]) # note, order is reversed for y
plt.show()


# In[ ]:


x = np.arange(-500, 500, 1)
X, Y = np.meshgrid(x, x)

wavelength1 = 200
angle1 = 0
grating1 = np.sin(2 * np.pi * (Y * np.cos(angle1) + X * np.sin(angle1)) / wavelength1)

wavelenght2 = 100
angle2 = np.pi / 4
grating2 = np.sin(2 * np.pi * (Y * np.cos(angle2) + X * np.sin(angle2)) / wavelenght2)

plt.set_cmap("gray")
plt.subplot(121)
plt.imshow(grating1)
plt.subplot(122)
plt.imshow(grating2)
plt.show()

gratings = grating1 + grating2

# calculate the fourier transform of grating
ft = np.fft.ifftshift(gratings)
ft = np.fft.fft2(ft)
ft = np.fft.fftshift(ft)
plt.figure()
plt.subplot(121)
plt.imshow(gratings)
plt.subplot(122)
plt.imshow(abs(ft))
plt.xlim([480, 520])
plt.ylim([520, 480]) # note, order is reversed for y
plt.show()


# In[ ]:


img = cv.imread("boy.bmp")


# In[ ]:


kernel = np.ones((5,5),np.float32)/25 
dst = cv.filter2D(img,-1,kernel) 
blur = cv.blur(img,(5,5))

cv.imshow('original',img) 
cv.imshow('filtered',dst) 
cv.imshow('blured',blur) 
cv.waitKey(0) 
cv.destroyAllWindows()
cv.waitKey(1) 


# In[ ]:


blur = cv.GaussianBlur(img,(5,5),0) 
median5 = cv.medianBlur(img,5) 
median9 = cv.medianBlur(img,9)


# In[ ]:


from random import * 
mean = 0
var = 40
sigma = var ** 0.5
gaussian = np.random.normal(mean, sigma, (img.shape[0],img.shape[1])) 
noisy_image=img
noisy_image[:, :, 0] = img[:, :, 0] + gaussian 
noisy_image[:, :, 1] = img[:, :, 1] + gaussian 
noisy_image[:, :, 2] = img[:, :, 2] + gaussian


# In[ ]:


#cv2.imshow('gaussian noise',noisy_image)
median5 = cv.medianBlur(noisy_image,5) 
median9 = cv.medianBlur(noisy_image,9) 

cv.imshow('median5 filtered',median5) 
cv.imshow('median9 filtered',median9) 
cv.imshow('noisy imaged',noisy_image) 
cv.waitKey(0)
cv.destroyAllWindows()
cv.waitKey(1)


# In[ ]:


img = cv.imread('boy.bmp',0) 
img=cv.cvtColor(noisy_image, cv.COLOR_BGR2GRAY) 
cv.imshow('gray',img)
cv.waitKey(0)
cv.destroyAllWindows()
cv.waitKey(1)


# In[ ]:


dft = cv.dft(np.float32(img),flags = cv.DFT_COMPLEX_OUTPUT) 
dft_shift = np.fft.fftshift(dft)
magnitude_spectrum = 20*np.log(cv.magnitude(dft_shift[:,:,0],dft_shift[:,:,1])) 
plt.subplot(121),plt.imshow(img, cmap = 'gray')

plt.title('Input Image'), plt.xticks([]), plt.yticks([]) 
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray') 
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([]) 
plt.show()


# In[ ]:


rows, cols = img.shape
crow,ccol = int(rows/2) , int(cols/2)

# create a mask first, center square is 1, remaining all zeros
mask = np.zeros((rows,cols,2),np.uint8) 
mask[crow-60:crow+60, ccol-60:ccol+60] = 1

# apply mask and inverse DFT
fshift = dft_shift*mask
f_ishift = np.fft.ifftshift(fshift)
img_back = cv.idft(f_ishift)
img_back = cv.magnitude(img_back[:,:,0],img_back[:,:,1])

plt.subplot(121),plt.imshow(img, cmap = 'gray') 
plt.title('Input Image'), plt.xticks([]), plt.yticks([]) 
plt.subplot(122),plt.imshow(img_back, cmap = 'gray') 
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([]) 
plt.show()


# In[ ]:


xx=np.max(img_back)/255 
img_backn=img_back/xx


# In[ ]:


ximg=img_backn.astype(int)


# In[ ]:


cv.imshow('gray',ximg) 
cv.waitKey(0) 
cv.destroyAllWindows()
cv.waitKey(1)


# In[ ]:


cv.imshow('gray',img) 
cv.waitKey(0) 
cv.destroyAllWindows()
cv.waitKey(1) 


# In[ ]:


np.max(img_back)


# In[ ]:




