#!/usr/bin/env python
# coding: utf-8

# In[1]:


first_name='kushagra'
last_name='gupta'


# In[2]:


#Using Format method
sentence= 'My name is {} {}'.format(first_name,last_name)
print(sentence)


# In[4]:


#using F strings. 
sentence= f'My name is {first_name.upper()} {last_name.upper()}'
print(sentence)
#[sweet]


# In[5]:


#Using Format Method
person={'name':'ritika','age':18}
sentence='My name is {} and I am {} years old'.format(person['name'],person['age'])
print(sentence)


# In[6]:


#Using F Strings
person={'name':'ritika','age':18}
sentence=f'My name is {person["name"]} and I am {person["age"]} years old'
print(sentence)


# In[7]:


#you can't use same type of quotes as they will conflict. or you have to use escape sequences.
person={'name':'ritika','age':18}
sentence=f'My name is {person['name']} and I am {person['age']} years old'
print(sentence)


# In[8]:


#you can do Calculation
calculation =f'4 times 11 is equal to {4 *11}'
print(calculation)


# In[11]:


#Advance formatting using F Strings
for n in range(1,11):
    sentence=f'The value is {n:02}'    #zero padding by 2
    print(sentence)


# In[13]:


pi =3.14159265
sentence=f'Pi is equal to {pi:0.4f}'   #Rounding the floating value to 4 places.
print(sentence)


# In[14]:


from datetime import datetime

birthday=datetime(2000,9,16)

sentence=f'Ritika has a birthday on {birthday}'
print(sentence)


# In[18]:


from datetime import datetime

birthday=datetime(2000,11,16)

sentence=f'Ritika has a birthday on {birthday:%b %d, %Y}'
print(sentence)

