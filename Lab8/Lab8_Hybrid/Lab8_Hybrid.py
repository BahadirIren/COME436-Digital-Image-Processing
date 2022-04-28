#!/usr/bin/env python
# coding: utf-8

# In[ ]:


conda install scipy


# In[1]:


import numpy
from numpy.fft import fft2, ifft2, fftshift, ifftshift 
from scipy import misc
from scipy import ndimage
import math
import cv2

def scaleSpectrum(A):
    return numpy.real(numpy.log10(numpy.absolute(A) + numpy.ones(A.shape)))

# sample values from a spherical gaussian function from the center of the image
def makeGaussianFilter(numRows, numCols, sigma, highPass=True): 
    centerI = int(numRows/2) + 1 if numRows % 2 == 1 else int(numRows/2) 
    centerJ = int(numCols/2) + 1 if numCols % 2 == 1 else int(numCols/2)
    
    def gaussian(i,j):
        coefficient = math.exp(-1.0 * ((i - centerI)**2 + (j - centerJ)**2) / (2 * sigma**2)) 
        return 1 - coefficient if highPass else coefficient
                                                                           
    return numpy.array([[gaussian(i,j) for j in range(numCols)] for i in range(numRows)])
                       
def filterDFT(imageMatrix, filterMatrix): 
    shiftedDFT = fftshift(fft2(imageMatrix)) 
    cv2.imwrite("images/dft.png", scaleSpectrum(shiftedDFT))
                       
    filteredDFT = shiftedDFT * filterMatrix
    cv2.imwrite("images/filtered-dft.png", scaleSpectrum(filteredDFT)) 
    return ifft2(ifftshift(filteredDFT))
                       
def lowPass(imageMatrix, sigma):
    n,m = imageMatrix.shape              
    return filterDFT(imageMatrix, makeGaussianFilter(n, m, sigma, highPass=False))
                       
def highPass(imageMatrix, sigma):
    n,m = imageMatrix.shape
    return filterDFT(imageMatrix, makeGaussianFilter(n, m, sigma, highPass=True))
                       
def hybridImage(highFreqImg, lowFreqImg, sigmaHigh, sigmaLow):
    highPassed = highPass(highFreqImg, sigmaHigh)
    lowPassed = lowPass(lowFreqImg, sigmaLow)
    return highPassed + lowPassed 

def playWithFiltering():
    marilyn = ndimage.imread("images/marilyn.png", flatten=True)
    highPassedMarilyn = highPass(marilyn, 20)
    lowPassedMarilyn = lowPass(marilyn, 20)
    cv2.imwrite("images/low-passed-marilyn.png", numpy.real(lowPassedMarilyn))
    cv2.imwrite("images/high-passed-marilyn.png", numpy.real(highPassedMarilyn))
    cv2.imwrite("images/sum-of-marilyns.png", numpy.real((highPassedMarilyn + lowPassedMarilyn)/ 2.0))


# In[4]:


einstein = cv2.imread("images/einstein.png",0)
marilyn = cv2.imread("images/marilyn.png",0)
hybrid = hybridImage(einstein, marilyn, 25, 10)
cv2.imwrite("images/einstein-marilyn.png", numpy.real(hybrid))


# In[ ]:


import matplotlib.pyplot as plt

plt.figure(figsize=(14, 18))
plt.subplot(131)
plt.imshow(cv2.cvtColor(einstein, cv2.COLOR_BGR2RGB))
plt.subplot(132) 
plt.imshow(cv2.cvtColor(marilyn, cv2.COLOR_BGR2RGB))
plt.subplot(133)
plt.imshow(numpy.real(hybrid) , cmap ='gray')
plt.show()


# In[6]:


einstein = cv2.imread("images/einstein.png",0)
marilyn = cv2.imread("images/marilyn.png",0)
hybrid = hybridImage(marilyn, einstein, 25, 10)
cv2.imwrite("images/marilyn-einstein.png", numpy.real(hybrid))


# In[ ]:


plt.figure(figsize=(14, 18))
plt.subplot(131)
plt.imshow(cv2.cvtColor(einstein, cv2.COLOR_BGR2RGB))
plt.subplot(132) 
plt.imshow(cv2.cvtColor(marilyn, cv2.COLOR_BGR2RGB))
plt.subplot(133)
plt.imshow(numpy.real(hybrid) , cmap ='gray')
plt.show()


# In[ ]:




