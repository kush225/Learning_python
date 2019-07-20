#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Strings are arrays of bytes representing Unicode characters.
#Strings in Python can be created using single quotes or double quotes or even triple quotes.


# In[2]:


greetings='Hello'
name='kushagra'


# In[3]:


#placeholder can be used to access variable using format method
message="{0}, {1}. welcome!".format(greetings,name)
print(message)


# In[4]:


#or you can use f string which are new to python.. you need to have python 3.6 or above to use f string
message2=f"{greetings}, {name}. welcome!"
print(message2)


# In[5]:


#To convert a string to all upper you can use in built method.
variable = "hello"
print(variable.upper())


# In[8]:


#you can use dir() function which return the list of valid attributes for that object
print(dir(variable))


# In[15]:


#you can use help function which display the documentation of modules, functions, classes, keywords etc.
print(help(dir))

