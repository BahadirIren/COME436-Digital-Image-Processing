#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2 as cv
import matplotlib.pyplot as plt

# read image from disk
original_image = cv.imread("images/tulips.jpg", 1)
blue_background_image = cv.imread("images/tulips.jpg", 1)
black_background_image = cv.imread("images/tulips.jpg", 1)
green_background_image = cv.imread("images/tulips.jpg", 1)
red_background_image = cv.imread("images/tulips.jpg", 1)

images = [original_image, blue_background_image, black_background_image, 
          green_background_image, red_background_image]

height = original_image.shape[0]
width = original_image.shape[1]

for i in range(0, height):
    for j in range(0, width):
        
        if original_image[i, j, 0] in range(252, 256):
            if original_image[i, j, 1] in range(252, 256):
                if original_image[i, j, 2] in range(252, 256):
                    
                    # set blue background
                    blue_background_image[i, j, 0] = 255
                    blue_background_image[i, j, 1] = 0
                    blue_background_image[i, j, 2] = 0
                    
                    # set black background
                    black_background_image[i, j, 0] = 0
                    black_background_image[i, j, 1] = 0
                    black_background_image[i, j, 2] = 0
                    
                    # set green background
                    green_background_image[i, j, 0] = 0
                    green_background_image[i, j, 1] = 255
                    green_background_image[i, j, 2] = 0
                    
                    # set red background
                    red_background_image[i, j, 0] = 0
                    red_background_image[i, j, 1] = 0
                    red_background_image[i, j, 2] = 255


# write images to disk
cv.imwrite("images/blue_background_image.png", blue_background_image)
cv.imwrite("images/black_background_image.png", black_background_image)
cv.imwrite("images/green_background_image.png", green_background_image)
cv.imwrite("images/red_background_image.png", red_background_image)

# plot graph
fig, axs = plt.subplots(1, len(images))
    
for i in range(0, len(images)):
    axs[i].imshow(cv.cvtColor(images[i], cv.COLOR_BGR2RGB))


# In[3]:


import cv2 as cv
import numpy as np

image = np.zeros((400, 400, 3), dtype = np.uint8)

red_radius = 150
blue_radius = 140

thickness = -1

center_coordinates = (200, 200)

red_color = (0, 0, 255)
blue_color = (255, 0, 0)

image = cv.circle(image, center_coordinates, red_radius, red_color, thickness)
image = cv.circle(image, center_coordinates, blue_radius, blue_color, thickness)

cv.imshow("Circle with opencv", image)
cv.waitKey(0)
cv.destroyAllWindows()
cv.waitKey(1)


# In[4]:


import math
import cv2 as cv
import numpy as np

def calculate_distance(a, b):
    x1, y1 = a
    x2, y2 = b
    return math.sqrt(math.pow((x1 - x2), 2) + math.pow((y1 - y2), 2))


image = np.zeros((400, 400, 3), dtype = np.uint8)

red_radius = 150
blue_radius = 140

center_coordinates = (200, 200)

for i in range(0, 400):
    for j in range(0, 400):
                     
        distance = calculate_distance((i, j), center_coordinates)
        if distance <= red_radius:
            # draw red circle
            image[i, j, 0] = 0
            image[i, j, 1] = 0
            image[i, j, 2] = 255
          
        if distance <= blue_radius:
            # draw blue circle
            image[i, j, 0] = 255
            image[i, j, 1] = 0
            image[i, j, 2] = 0
            
cv.imshow("Circle without opencv", image)
cv.waitKey(0)
cv.destroyAllWindows()
cv.waitKey(1)


# In[ ]:




