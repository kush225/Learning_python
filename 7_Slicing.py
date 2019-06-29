#!/usr/bin/env python
# coding: utf-8

# In[1]:


my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#          0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#        -10,-9,-8,-7,-6,-5,-4,-3,-2,-1


# In[7]:


#my_list[start:end] where element at end index is not included
print(my_list[0:9])


# In[9]:


print(my_list[:])


# In[10]:


print(my_list[2:6])


# In[11]:


print(my_list[-8:-4])


# In[12]:


#reversing the list
print(my_list[-1::-1])


# In[13]:


#same as above
print(my_list[::-1])


# In[14]:


#Excercise
sample_url = 'http://coreyms.com'


# In[15]:


#Reverse the URL
print(sample_url[::-1])


# In[16]:


#Get the top level domain
print(sample_url[-4:])


# In[18]:


#Print the URL without the http://
print(sample_url[7:])


# In[19]:


#Print the url without the http:// or the top level domain
print(sample_url[7:-4])

