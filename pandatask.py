#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
os.getcwd()


# In[2]:


import pandas as pd
import numpy as np
from tensorflow import keras as tf


# In[7]:


dataset=tf.datasets.mnist.load_data()
train_df=pd.DataFrame(list(zip(dataset[0][0], dataset[0][1])), columns =['image', 'label'])
test_df = pd.DataFrame(list(zip(dataset[0][0], dataset[0][1])), columns =['image', 'label'])
p=train_df.to_csv("first_panda")
f=test_df.to_csv("second_panda")


# In[13]:


print(type(dataset[0][0]))


# In[23]:


first_file=pd.read_csv("first_panda")
second_file=pd.read_csv("second_panda")
first_file1=first_file['image'].to_numpy()
first_file2=first_file['label'].to_numpy()
second_file1=second_file['image'].to_numpy()
second_file2=second_file['label'].to_numpy()


# In[25]:


print(type(first_file1))
print(type(first_file2))
print(type(second_file1))
print(type(second_file2))
p=((first_file1,first_file2),(second_file1,second_file2))
print(type(p))


# In[ ]:




