#!/usr/bin/env python
# coding: utf-8

# In[1]:


#FOR LOOP
#A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

#This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

#With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.


# In[4]:


#list
numbers=[1,2,3,4,5]


# In[6]:


#for loop iterates once for each item in a list
for num in numbers:
    print(num)


# In[3]:


#break is used to terminate the loop
for num in numbers:
    if num == 3:
        print('found the number')
        break
    print(num)


# In[7]:


#continue statement rejects all the remaining statements in the current iteration of the loop and moves the control back to the top of the loop
for num in numbers:
    if num == 3:
        print('found the number')
        continue
        print('this will never get prints')
    print(num)


# In[8]:


#range(start,end) #end value doesn't get included
for i in range(1,11):
    print(i)


# In[9]:


#range(start,end,step)
for i in range(1,11,3):
    print(i)

