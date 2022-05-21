# Implementation-of-Erosion-and-Dilation
## Aim
To implement Erosion and Dilation using Python and OpenCV.
## Software Required
1. Anaconda - Python 3.7
2. OpenCV
## Algorithm:
### Step1:
<br>


### Step2:
<br>

### Step3:
<br>

### Step4:
<br>

### Step5:
<br>

 
## Program:

``` Python
# Import the necessary packages
import cv2
import matplotlib.pyplot as plt
import numpy as np


# Create the Text using cv2.putText
img1=np.zeros((100,400),dtype='uint8')
font=cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img1,'Vigneshwar',(5,70),font,2,(255),5,cv2.LINE_AA)


# Create the structuring element
kernel=cv2.getStructuringElement(cv2.MORPH_CROSS,(7,7))


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

<img width="278" alt="10-1" src="https://user-images.githubusercontent.com/77089276/169656428-cf1b0e8c-2591-4a13-9f54-011527ef2123.PNG">

### Display the Eroded Image

<img width="297" alt="10-2" src="https://user-images.githubusercontent.com/77089276/169656433-0dd993ce-e0d8-49a6-8965-7ff94a03baa9.PNG">

### Display the Dilated Image

<img width="279" alt="10-3" src="https://user-images.githubusercontent.com/77089276/169656435-2982b447-ee6a-46c9-9f3d-e5cbc5accfb8.PNG">

## Result
Thus the generated text image is eroded and dilated using python and OpenCV.
