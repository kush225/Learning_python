#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Context Manager
#Managing Resources : In any programming language, the usage of resources like file operations or database connections is very common. But these resources are limited in supply. Therefore, the main problem lies in making sure to release these resources after usage. If they are not released then it will lead to resource leakage and may cause the system to either slow down or crash. It would be very helpful if user have a mechanism for the automatic setup and teardown of resources.In Python, it can be achieved by the usage of context managers which facilitate the proper handling of resources.


# In[3]:


#without context manager
f = open('sample.txt','w')
f.write('hello my name is kushagra')
f.close()
#we have remember to close the file 


# In[5]:


#With Context Manager
with open('sample2.txt', 'w') as f:
    f.write('hello my name is kushagra')
#Benefits of using Context Manager
#Handles Tear down of resources so we don't have to do manually.
#We no longer have to close the file after we are done working with it.
#And also recommended bcoz if we throw an error while working with it, it will properly close the file automatically


# In[6]:


#Making our own Context Manager using class
class Open_file():
    def __init__(self,filename, mode):
        self.filename=filename
        self.mode=mode
    
    def __enter__(self):
        self.file = open(self.filename,self.mode)
        return self.file
    
    def __exit__(self,exc_type,exc_val,tracebook):
        self.file.close()

#on running this it will run __init__ method and __enter__ method
with Open_file('sample.txt','w') as f: 
    #since file is opened we can perform operation.
    f.write('Testing')
#on exiting the indent block __exit__ method runs and close the file
    
#True value means file got closed after coming out of indent block.
print(f.closed)


# In[7]:


#Making our own Context Manager using function
#we need to import decorator for creating context manager using function.
from contextlib import contextmanager

@contextmanager
def open_file(file,mode):
    try:
        f = open(file,mode)
        yield f
        #this two line will work same as __enter__
    finally:
        f.close()
        #this will run when we exit the indent block
    
with open_file('sample.txt','w') as f:
    f.write("hello")

print(f.closed)


# In[10]:


#The above context manager that we made are already in builtin so we don't really need those.
#so let's make a useful context manager
#so suppose we are at home directory and we have to go to some directory and do some work and come back to home again
#In this case we have to manually come to home path again and again
import os

cwd = os.getcwd()   #getting current working dir
os.chdir('dir1')    #changing cwd to dir1
print(os.listdir()) #listing files in dir1
os.chdir(cwd)       #switching back to the directory where we started

cwd = os.getcwd()   #getting current working dir
os.chdir('dir2')    #changing cwd to dir2
print(os.listdir()) #listing files in dir2
os.chdir(cwd)       #switching back to the directory where we started

#So let's use a context manager so when we exit the indent we come to home location automatically


# In[21]:


#above example using context manager
#path at which we are initally present
print(os.getcwd())

@contextmanager
def change_loc(destination):
    try:
        cwd=os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)

#changing path location
with change_loc('dir2'):
    #doing operation at changed location
    print(os.listdir())

#automatically at initial location
print(os.getcwd())

#changing path location
with change_loc('dir1'):
    #doing operation at changed location
    print(os.listdir())
    
#automatically at initial location    
print(os.getcwd())

#Earlier we have to remember to change back and now we can re use this context manager over and over. and we know resources will be managed automatically.
#Other Uses of Context Manager
#Database Connection, Acquiring Lock,etc

