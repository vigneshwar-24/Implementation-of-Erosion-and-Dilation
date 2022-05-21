#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


# Create the Text using cv2.putText
img1=np.zeros((100,400),dtype='uint8')
font=cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img1,'Vigneshwar',(5,70),font,2,(255),5,cv2.LINE_AA)


# In[3]:


kernel=cv2.getStructuringElement(cv2.MORPH_CROSS,(7,7))
plt.imshow(img1)
plt.axis('off')
plt.title('orginal')


# In[4]:


# Erode the image
image_erode=cv2.erode(img1,kernel)
plt.imshow(image_erode)
plt.axis('off')
plt.title('Erosion')


# In[5]:


# Dilate the image
image_dilate=cv2.dilate(img1,kernel)
plt.imshow(image_dilate)
plt.axis('off')
plt.title('Dilation')


# In[ ]:




