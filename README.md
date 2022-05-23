# Implementation-of-Erosion-and-Dilation
## Aim
To implement Erosion and Dilation using Python and OpenCV.
## Software Required
1. Anaconda - Python 3.7
2. OpenCV
## Algorithm:

### Step1:

Import the necessary packages.

### Step2:

Create the text image using cv2.putText.

### Step3:

Then create the structuring image for dilation/erosion

### Step4:

Apply erosion and dilation using cv2.erode and cv2.dilate

### Step5:

Plot the images using plt.imshow

 
## Program:

``` Python

# Import the necessary packages

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Create the Text using cv2.putText

img1=np.zeros((100,400),dtype='uint8')
font=cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img1,'Vigneshwar',(5,70),font,2,(255),5,cv2.LINE_AA)


# Create the structuring element

kernel=cv2.getStructuringElement(cv2.MORPH_CROSS,(7,7))
plt.imshow(img1)
plt.axis('off')
plt.title('orginal')

# Erode the image

image_erode=cv2.erode(img1,kernel)
plt.imshow(image_erode)
plt.axis('off')
plt.title('Erosion')

# Dilate the image

image_dilate=cv2.dilate(img1,kernel)
plt.imshow(image_dilate)
plt.axis('off')
plt.title('Dilation')


```
## Output:

### Display the input Image

<img width="278" alt="10-1" src="https://user-images.githubusercontent.com/77089276/169828171-028809a5-939d-4ab6-8947-8ea4a82f9481.PNG">

### Display the Eroded Image

<img width="297" alt="10-2" src="https://user-images.githubusercontent.com/77089276/169828276-de3aa966-6640-4db3-abbf-d0bc4df240be.PNG">

### Display the Dilated Image

<img width="279" alt="10-3" src="https://user-images.githubusercontent.com/77089276/169828356-780758d9-e7ad-4165-b509-074e7751e657.PNG">

## Result
Thus the generated text image is eroded and dilated using python and OpenCV.
