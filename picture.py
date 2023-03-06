#!/usr/bin/env python
# coding: utf-8

# In[4]:


pip install opencv-python


# In[2]:


import cv2
import numpy as np
from PIL import Image


# In[23]:


file_adres="baboon.png"
img=cv2.imread(file_adres)
hsv_img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
lower_red = np.array([0, 50, 50])
upper_red = np.array([10, 255, 255])
mask=cv2.inRange(hsv_img,lower_red,upper_red)
img[mask>0]=[0,0,0]


cv2.imshow('Modified.png',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# display(Image.fromarray(cv2.cvtColor(arr,cv2.COLOR_BGR2RGB)))


# In[ ]:




