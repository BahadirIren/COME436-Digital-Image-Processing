#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pywt
import pywt.data


# In[2]:


pywt.families()


# In[3]:


w = pywt.Wavelet("db3")
print(w)


# In[5]:


pywt.wavelist()


# In[6]:


wavelet = pywt.Wavelet("haar")
print(wavelet)


# In[7]:


original = pywt.data.camera()
plt.imshow(original, cmap="gray")


# In[24]:


coeffs2 = pywt.dwt2(original, "bior1.3")
titles = ["Approximation", "horizontal detail", "vertical detail", "diagonal detail"]
LL,(LH, HL, HH) = coeffs2


# In[25]:


fig = plt.figure(figsize=(12,3))
for i,a in enumerate([LL, LH, HL, HH]):
    ax = fig.add_subplot(1,4,i+1)
    ax.imshow(a, interpolation= "nearest", cmap= plt.cm.gray)
    ax.set_title(titles[i], fontsize=10)

fig.tight_layout()
plt.show()


# In[26]:


transformed_image_inverse = pywt.idwt2(coeffs2,"bior1.3")
plt.imshow(transformed_image_inverse, cmap="gray")


# In[ ]:




