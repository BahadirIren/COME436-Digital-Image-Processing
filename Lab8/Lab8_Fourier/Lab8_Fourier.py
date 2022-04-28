#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import numpy as np
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


desert = cv2.imread('../images/desert.png', 0) 
coffee = cv2.imread('../images/coffee.png', 0)

a,b= desert.shape 

coffee=cv2.resize(coffee,(b,a)) 

plt.figure(figsize=(14, 18)) 
plt.subplot(121)
plt.imshow(desert, cmap='gray') 
plt.subplot(122)
plt.imshow(coffee, cmap='gray') 
plt.show()


# In[ ]:


# fourier transform
desert_fft = np.fft.fftshift(np.fft.fft2(desert)) 
coffee_fft = np.fft.fftshift(np.fft.fft2(coffee))

plt.figure(figsize=(14, 18))
plt.subplot(121)
plt.imshow(np.log(np.abs(desert_fft)), cmap='gray')
plt.subplot(122) 
plt.imshow(np.log(np.abs(coffee_fft)), cmap='gray') 
plt.show()


# In[ ]:


desert_amplitude = np.sqrt(np.real(desert_fft) ** 2 + np.imag(desert_fft) ** 2)
desert_phase = np.arctan2(np.imag(desert_fft), np.real(desert_fft))

plt.figure(figsize=(14, 18))
plt.subplot(121)
plt.imshow(np.log(desert_amplitude+1e-10), cmap='gray') 
plt.subplot(122)
plt.imshow(desert_phase, cmap='gray')


# In[ ]:


coffee_amplitude = np.sqrt(np.real(coffee_fft) ** 2 + np.imag(coffee_fft) ** 2) 
coffee_phase = np.arctan2(np.imag(coffee_fft), np.real(coffee_fft))

plt.figure(figsize=(14, 18))
plt.subplot(121) 
plt.imshow(np.log(coffee_amplitude+1e-10), cmap='gray') 
plt.subplot(122)
plt.imshow(coffee_phase, cmap='gray')


# In[ ]:


desert_coffee_comb = np.multiply(desert_amplitude, np.exp(1j * desert_phase)) 
desert_coffee = np.real(np.fft.ifft2(desert_coffee_comb)) # drop imagniary as they are

# combined image has values < 0 and > 1, needs to be scaled.
plt.figure(figsize=(15, 20))
plt.subplot(131) 
plt.imshow(np.abs(desert_coffee), cmap='gray') 
plt.subplot(132)

desert_coffee_shift = desert_coffee + desert_coffee.min() 
desert_coffee_shift[desert_coffee_shift>255] = 255 

plt.imshow(desert_coffee_shift, cmap='gray') 
plt.subplot(133)
desert_coffee[desert_coffee>255] = 255 
desert_coffee[desert_coffee <0] = 0 
plt.imshow(desert_coffee, cmap='gray')


# In[ ]:


# amplitude_phase
desert_coffee_comb = np.multiply(desert_amplitude, np.exp(1j * coffee_phase)) 
desert_coffee = np.real(np.fft.ifft2(desert_coffee_comb)) # drop imagniary as they are around 1e-14

# combined image has values < 0 and > 1, needs to be scaled.
plt.figure(figsize=(15, 20))
plt.subplot(131) 
plt.imshow(np.abs(desert_coffee), cmap='gray') 
plt.subplot(132)

desert_coffee_shift = desert_coffee + desert_coffee.min() 
desert_coffee_shift[desert_coffee_shift>255] = 255 

plt.imshow(desert_coffee_shift)
plt.subplot(133)
desert_coffee[desert_coffee>255] = 255 
desert_coffee[desert_coffee <0] = 0 
plt.imshow(desert_coffee)


# In[ ]:


# amplitude_phase
coffee_desert_comb = np.multiply(coffee_amplitude, np.exp(1j * desert_phase)) 
coffee_desert = np.real(np.fft.ifft2(coffee_desert_comb)) # drop imagniary as they are around 1e-14

# combined image has values < 0 and > 1, needs to be scaled.
plt.figure(figsize=(15, 20))
plt.subplot(131)
plt.imshow(np.abs(coffee_desert), cmap='gray')
plt.subplot(132)

coffee_desert_shift = coffee_desert + coffee_desert.min()
coffee_desert_shift[coffee_desert_shift>255] = 255

plt.imshow(coffee_desert_shift)
plt.subplot(133)
coffee_desert[coffee_desert>255] = 255 
coffee_desert[coffee_desert <0] = 0 
plt.imshow(coffee_desert)


# In[ ]:




