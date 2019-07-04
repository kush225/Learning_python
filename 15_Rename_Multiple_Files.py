#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os 


# In[12]:


#Files Present in Directory
os.listdir('/home/kushagra/Desktop/test')


# In[23]:


#Spliting name and extension of file
for f in os.listdir():
    print(os.path.splitext(f))
   


# In[24]:


#Printing Name and ext of files
for f in os.listdir():
    name,ext = os.path.splitext(f)
    print(name)
    print(ext)


# In[25]:


#Spliting name on the basis of "-"
for f in os.listdir():
    name,ext = os.path.splitext(f)
    song,artist,number=name.split("-")
    song=song[2:]
    print(song)


# In[31]:


#Renaming the files as per our requirement, using zfill we make sure that every number is of 2 digit.
for f in os.listdir():
    name,ext=os.path.splitext(f)
    song,artist,number=name.split("-")
    song=song[2:]
    number=number.zfill(2)
    os.rename(f,"{0}-{1}{2}".format(number,song,ext))


# In[32]:


#You can see name is changed 
os.listdir()


# In[ ]:




