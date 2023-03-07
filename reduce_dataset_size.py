#!/usr/bin/env python
# coding: utf-8

# In[23]:


import tensorflow.keras as tk
import random
import collections
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist


# In[16]:


def display_random_images_with_labels(d, n=10):
    choices = list(range(len(d[0])))
    for i in range(n):
        index = random.choice(choices)
        choices.remove(index)
        print("index:",index)
        print("Lable:",d[1][index])
        plt.imshow(d[0][index], cmap='gray')
        plt.show()


# # Dataset

# In[19]:


# Loading dataset
dataset = keras.datasets.mnist.load_data()
print("There are",len(dataset[0][0]),"images in training dataset")
print("There are",len(dataset[1][0]),"images in training dataset")
print("___________________\n\n")
print("Randomly printing 10 images with labels from training dataset")
display_random_images_with_labels(dataset[0])
print("___________________\n\n")
print("Randomly printing 10 images with labels from testing dataset")
display_random_images_with_labels(dataset[0])
print("___________________\n\n")

print("There are",len(dataset[0][1]),"labels in training dataset for",len(dataset[0][0]),"images in training dataset")
print("There are",len(dataset[1][1]),"labels in training dataset for",len(dataset[1][0]),"images in training dataset")
print("___________________\n\n")

print("There are", len(set(dataset[0][1])),"unique classes in training dataset")
print("Breakdown of each labels is below (format: dict key is label, dict value is occurrence of that label/ number of images for that label)")
display(collections.Counter(dataset[0][1]))
print("There are", len(set(dataset[1][1])),"unique classes in validation dataset")
print("Breakdown of each labels is below (format: dict key is label, dict value is occurrence of that label/ number of images for that label)")
display(collections.Counter(dataset[1][1]))
print("___________________\n\n")


# # Task
# 
# You have to reduce the size of this dataset by 10 times.
# 
# There are currently almost 5000 to 6000 thousand images (total: 60000) for each label in training and almost 1000 images (total: 10000) for each label in testing dataset.
# 
# You are required to reduce this training dataset so that it will have exactly 600 images for each label (total: 6000) in training dataset and exactly 100 images for each label in testing dataset (total: 1000)
# 
# new dataset should be stored into new_dataset variable name and should have exactly same format as the original dataset.
# 

# In[70]:



tr_x=[]
tr_y=[]
ts_x=[]
ts_y=[]
for i in range(10):
    tr_x.append(dataset[0][0][dataset[0][1]==i][:600])
    tr_y.append(dataset[0][1][dataset[0][1]==i][:600])
    ts_x.append(dataset[1][0][dataset[1][1]==i][:100])
    ts_y.append(dataset[1][1][dataset[1][1]==i][:100])
new_dataset = ((np.concatenate(tr_x), np.concatenate(tr_y)) , (np.concatenate(ts_x), np.concatenate(ts_y)))


# In[ ]:





# # Validation of Task

# In[69]:


# Checking the shape of first image in new training dataset
print(new_dataset[0][0][0].shape)
print("___________________")
print("There are",len(new_dataset[0][1]),"labels in training dataset for",len(new_dataset[0][0]),"images in training dataset")
print("There are",len(new_dataset[1][1]),"labels in training dataset for",len(new_dataset[1][0]),"images in training dataset")
print("___________________\n\n")
print("There are", len(set(new_dataset[0][1])),"unique classes in training dataset")
print("Breakdown of each labels is below (format: dict key is label, dict value is occurrence of that label/ number of images for that label)")
display(collections.Counter(new_dataset[0][1]))
print("There are", len(set(new_dataset[1][1])),"unique classes in validation dataset")
print("Breakdown of each labels is below (format: dict key is label, dict value is occurrence of that label/ number of images for that label)")
display(collections.Counter(new_dataset[1][1]))
print("___________________\n\n")
print("Randomly printing 10 images with labels from training dataset")
display_random_images_with_labels(new_dataset[0])
print("___________________\n\n")
print("Randomly printing 10 images with labels from testing dataset")
display_random_images_with_labels(new_dataset[0])
print("___________________\n\n")








# In[ ]:




