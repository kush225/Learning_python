#!/usr/bin/env python
# coding: utf-8

# In[1]:


#FUNCTION
# A function is a block of code which only runs when it is called.

# You can pass data, known as parameters, into a function.

# A function can return data as a result.


# In[2]:


#function is define using def keyword.
def hello(greeting):
    return greeting


# In[3]:


#calling the function
hello("hello")


# In[4]:


#defining a function with default value.
def hello_func(greeting, name='kushagra'):
    return '{}, {}'.format(greeting,name)


# In[5]:


hello_func('hi')


# In[6]:


print(hello_func('hi','Jack'))


# In[7]:


#Use *args - for variable number of arguments
#Use *kwargs - for variable number of keyword arguments
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)
#student_info function accepting *args & **kwargs and printing it.


# In[8]:


student_info('Math', 'Art', name='Jean', age=23)


# In[9]:


#list
courses=['Math','Art']
#dictionary
info={'name': 'jane', 'age': 25}


# In[10]:


#passing courses list and info dictionary to our function student_info
student_info(courses,info)
#all these are passed as an argument. 


# In[11]:


#so we need to specify arguments and keyword arguments
student_info(*courses,**info)

