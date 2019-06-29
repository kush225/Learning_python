#!/usr/bin/env python
# coding: utf-8

# In[7]:


#function is define using def keyword.
def hello(greeting):
    return greeting


# In[8]:


#calling the function
print(hello("hello"))


# In[1]:


#def a function with default value.
def hello_func(greeting, name='kushagra'):
    return '{}, {}'.format(greeting,name)


# In[2]:


print(hello_func('hi'))


# In[9]:


print(hello_func('hi','Jack'))


# In[10]:


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


# In[11]:


student_info('Math', 'Art', name='Jean', age=23)


# In[12]:


courses=['Math','Art']
info={'name': 'jane', 'age': 25}


# In[13]:


student_info(courses,info)


# In[14]:


student_info(*courses,**info)

