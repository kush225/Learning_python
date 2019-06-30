#!/usr/bin/env python
# coding: utf-8

# In[1]:


person={'name':'John','age':30}


# In[8]:


sentence='My name is ' + person['name'] + ' and i am ' + str(person['age']) + ' yrs old.'
print(sentence)


# In[12]:


#Above code using String Formatting
sentence='My name is {} and i am {} yrs old.'.format(person['name'],person['age'])
print(sentence)


# In[16]:


tag='h1'
text="This is a Heading"


# In[17]:


sentence='<{0}>{1}<\{0}>'.format(tag,text)
print(sentence)


# In[20]:


sentence='My name is {0[name]} and i am {0[age]} yrs old.'.format(person)
print(sentence)


# In[22]:


class Person():
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
p1 = Person("Aron",25)

sentence='My name is {0.name} and i am {0.age} yrs old.'.format(p1)
print(sentence)


# In[23]:


sentence='My name is {name} and i am {age} yrs old.'.format(name='ken',age=24)
print(sentence)


# In[24]:


person={'name':'John','age':30}


# In[25]:


#Best way to unpack a dictionary
sentence='My name is {name} and i am {age} yrs old.'.format(**person)
print(sentence)


# In[26]:


for i in range(1,11):
    sentence="The Value is {}".format(i)
    print(sentence)


# In[27]:


#To Print numbers in 2 digit only
for i in range(1,11):
    sentence="The Value is {:02}".format(i)
    print(sentence)


# In[29]:


pi =3.14159265
sentence="Value of pi is {:.2f}".format(pi)
print(sentence)


# In[32]:


sentence="1MB is equal to {} bytes".format(1000**2)
print(sentence)


# In[33]:


sentence="1MB is equal to {:,} bytes".format(1000**2)
print(sentence)


# In[34]:


sentence="1MB is equal to {:,.2f} bytes".format(1000**2)
print(sentence)


# In[35]:


import datetime
my_date = datetime.datetime(2016,9,24,12,30,45)
print(my_date)


# In[36]:


sentence='{:%B %d, %Y}'.format(my_date)
print(sentence)


# In[40]:


#September 24, 2016 fell on a Saturday and was the 268 day of the year.
sentence="{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year.".format(my_date)
print(sentence)

