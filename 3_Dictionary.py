#!/usr/bin/env python
# coding: utf-8

# In[1]:


#DICTIONARY
#It is a collection which is unordered, changeable and indexed which doesn't allow duplicate members.


# In[2]:


#Dictionary holds key:value pair. 
student= {'name' : 'kushagra', 'age' : 23, 'interests' : [ 'Maths' ,'Science']}


# In[3]:


print(student)


# In[4]:


#accessing value of dictionary
print(student['interests'])


# In[5]:


#gives an KeyError if key:value doesn't exist
print(student['hobby'])


# In[6]:


#using get function which doesnot give error when data not available
print(student.get('phone'))


# In[7]:


#you can also set the return value in case data is not available
print(student.get('name','Not Found'))
print(student.get('phone','Not Found'))


# In[8]:


#Adding and Appending Elements to Dict
student['phone']='555-55555'
student['name']='jane'


# In[9]:


print(student)


# In[10]:


#using update multiple changes at once
student.update({'name': 'yo' , 'age' : 26 , 'phone' : '99-99999'})
print(student)


# In[11]:


#Deleting Element
del student['age']
print(student)


# In[12]:


#removes the value of given key and stores in the variable
no=student.pop('phone')
print(student)


# In[13]:


print(no)


# In[14]:


#printing keys of dict
print(student.keys())


# In[15]:


#printing values of dict
print(student.values())


# In[16]:


#printing items of dict
print(student.items())


# In[17]:


#Iterating over dictionary.
for key, value in student.items():
    print(key, value)

