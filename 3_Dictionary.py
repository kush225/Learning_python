#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Dictionary holds key:value pair. 
student= {'name' : 'kushagra', 'age' : 23, 'interests' : [ 'Maths' ,'Science']}


# In[3]:


print(student)


# In[4]:


print(student['interests'])


# In[6]:


#get doesnot give error when data not available
print(student.get('phone'))


# In[8]:


#you can also set the return value in case data is not available
print(student.get('name','Not Found'))
print(student.get('phone','Not Found'))


# In[9]:


#Adding and Appending Elements to Dict
student['phone']='555-55555'
student['name']='jane'


# In[10]:


print(student)


# In[20]:


#using update multiple changes at once
student.update({'name': 'yo' , 'age' : 26 , 'phone' : '99-99999'})
print(student)


# In[13]:


#Deleting Element
del student['age']
print(student)


# In[21]:


#removes the value of given key and stores in the variable
no=student.pop('phone')
print(student)


# In[22]:


print(no)


# In[23]:


#printing keys of dict
print(student.keys())


# In[24]:


#printing values of dict
print(student.values())


# In[25]:


#printing items of dict
print(student.items())


# In[26]:


for key, value in student.items():
    print(key, value)

