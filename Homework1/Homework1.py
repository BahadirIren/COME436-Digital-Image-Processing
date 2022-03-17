#!/usr/bin/env python
# coding: utf-8

# In[1]:


# • read an image 1 from hard disk
# • display it
# • read an image 2 from hard disk
# • display it
# • rescale image 1 50%
# • concatenate horizontal image 1-2
# • display
# • concatenate vertical image 1-2
# • save vertical concatenated image


import cv2

def scale_image(image, scale_factor):
    height = int(image.shape[0] * (scale_factor / 100))
    width = int(image.shape[1] * (scale_factor / 100))
    
    dimension = (width, height)
    
    return cv2.resize(image1, dimension, interpolation = cv2.INTER_AREA)


# image2 resized according to image1's height
def horizontal_concatenate_images(image1, image2):
    
    image1_heigth = image1.shape[0]
    image2_width = image2.shape[1]

    dimension = (image2_width, image1_heigth)

    resized_image2 = cv2.resize(image2, dimension, interpolation = cv2.INTER_AREA)

    horizontal_concat_image = cv2.hconcat([image1, resized_image2])

    cv2.imshow('horizontal concatenated image', horizontal_concat_image)
    

# image2 resized according to image1's width
def vertical_concatenate_images(image1, image2):
    
    image2_height = image2.shape[0]
    image1_width = image1.shape[1]
    
    dimension = (image1_width, image2_height)
    
    resized_image2 = cv2.resize(image2, dimension, interpolation = cv2.INTER_AREA)
    
    vertical_concat_image = cv2.vconcat([image1, resized_image2])
    
    cv2.imwrite('images/vertical_concatenated_image.jpg', vertical_concat_image)
    

image1 = cv2.imread('images/image1.jpg', 1)
cv2.imshow('image 1',image1)

image2 = cv2.imread('images/image2.jpg', 1)
cv2.imshow('image 2',image2)

resized_image1 = scale_image(image1, 50)

horizontal_concatenate_images(image1, image2)
vertical_concatenate_images(image1, image2)


cv2.waitKey(0) # close window when a key press is detected
cv2.destroyAllWindows()
cv2.waitKey(1)


# In[ ]:




