#!/usr/bin/env python
# coding: utf-8
#Difference Between str() and repr()?
#The goal of __repr__ is to be unambiguous.
#The goal of __str__ is to be readable.

#__repr__
#1. is used for logging, debugging.
#2. meant to be used by developers.

#__str__
#1. is meant to used as a display to the end user.
# In[2]:


a= [1,2,3,4]
b= 'sample string' 


# In[3]:


#Both will give the same output
print(str(a))
print(repr(a))


# In[5]:


print(str(b))
print(repr(b))


# In[9]:


import datetime
import pytz
a=datetime.datetime(2015, 6, 11, 4, 35, 48, 528521, tzinfo=pytz.UTC)
b='2015-06-11 04:35:48.528521+00:00'


# In[10]:


#on surface both variables a and b looks same.
print(str(a))
print(str(b))
#The goal of __str__ is to be readable.


# In[11]:


#whenever we ran repr(a) we are able to get it's a datetime.
print(repr(a))
print(repr(b))
#The goal of __repr__ is to be unambiguous.


# In[12]:


a= datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
b=str(a)


# In[14]:


#Another example
print('str(a): {}'.format(str(a)))
print('str(b): {}'.format(str(b)))
print()
print('repr(a): {}'.format(repr(a)))
print('repr(b): {}'.format(repr(b)))

