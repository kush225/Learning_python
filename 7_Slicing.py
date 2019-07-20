#!/usr/bin/env python
# coding: utf-8

# In[1]:


#slicing
# The slice() function returns a slice object.

# A slice object is used to specify how to slice a sequence. You can specify where to start the slicing, and where to end. You can also specify the step, which allows you to e.g. slice only every other item.


# In[2]:


my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#          0, 1, 2, 3, 4, 5, 6, 7, 8, 9    #indexes
#        -10,-9,-8,-7,-6,-5,-4,-3,-2,-1    #indexes


# In[3]:


#my_list[start:end] where element at end index is not included
print(my_list[0:9])


# In[4]:


print(my_list[:])


# In[5]:


print(my_list[2:6])


# In[6]:


print(my_list[-8:-4])


# In[7]:


#reversing the list
print(my_list[-1::-1])


# In[8]:


#same as above
print(my_list[::-1])


# In[9]:


#Excercise
sample_url = 'http://coreyms.com'


# In[10]:


#Reverse the URL
print(sample_url[::-1])


# In[12]:


#Get the top level domain
print(sample_url[-4:])


# In[13]:


#Print the URL without the http://
print(sample_url[7:])


# In[14]:


#Print the url without the http:// or the top level domain
print(sample_url[7:-4])

