#!/usr/bin/env python
# coding: utf-8

# In[2]:


#os Module
#The OS module in python provides functions for interacting with the operating system.
#This module provides a portable way of using operating system dependent functionality.


# In[3]:


import os


# In[4]:


#You can check All the options in os module using dir()
#print(dir(os))


# In[3]:


#Current working Directory
print(os.getcwd())


# In[7]:


#Changing Current Working Directory
os.chdir('/home/kushagra/Documents')


# In[8]:


print(os.getcwd())


# In[9]:


#Listing the files and directories in current Directories
print(os.listdir())


# In[10]:


#making Directory, makedirs works similar to mkdir -p option
os.mkdir('OS-Demo-1')
os.makedirs('OS-Demo-2/a/b/c')


# In[11]:


print(os.listdir())


# In[12]:


#Deleting Directories, removedirs will remove sub directories also
os.rmdir('OS-Demo-1')
os.removedirs('OS-Demo-2/a/b/c')


# In[13]:


#Rename file or folder
os.rename('bzLifecycle.png','bugzlifecycle.png')


# In[14]:


print(os.listdir())


# In[16]:


#information about file
print(os.stat("bugzlifecycle.png"))


# In[17]:


#Modified time
print(os.stat("bugzlifecycle.png").st_mtime)


# In[18]:


#Modified time in Human Readable Format
from datetime import datetime
mod_time=os.stat("bugzlifecycle.png").st_mtime
print(datetime.fromtimestamp(mod_time))


# In[35]:


for dirpath, dirnames, dirfiles in os.walk('/home/kushagra/Desktop/percentile'):
    print("Current dir:", dirpath)
    print("Directories:", dirnames)
    print("Files:", dirfiles)
    print()


# In[37]:


#Printing Environment Variable
print(os.environ.get('HOME'))


# In[38]:


#Joining path and file
file_path=os.path.join(os.environ.get('HOME'),'test.txt')
print(file_path)


# In[39]:


#To get filename
print(os.path.basename('/home/cavisson/test.txt'))


# In[40]:


#To get path
print(os.path.dirname('/home/cavisson/test.txt'))


# In[41]:


#To split path and filename
print(os.path.split('/home/cavisson/test.txt'))


# In[48]:


#To check whether file exists or not
print(os.path.exists("/home/kushagra/test.txt"))


# In[49]:


print(os.path.exists("/home/cavisson/test.txt"))


# In[45]:


#Check whether file or not
print(os.path.isfile("/home/kushagra/test.txt"))


# In[46]:


#Check whether Dir or not
print(os.path.isdir("/home/kushagra"))


# In[52]:


#Spliting extension
print(os.path.splitext('/tmp/test.txt'))


# In[53]:


#options with os.path module
print(dir(os.path))

