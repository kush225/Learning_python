#!/usr/bin/env python
# coding: utf-8

# In[1]:


numbers=[1,2,3,4,5]


# In[2]:


#break is used to terminate the loop
for num in numbers:
    if num == 3:
        print('found the number')
        break
    print(num)


# In[5]:


#continue statement rejects all the remaining statements in the current iteration of the loop and moves the control back to the top of the loop
for num in numbers:
    if num == 3:
        print('found the number')
        continue
        print('this will never get prints')
    print(num)


# In[9]:


#range(start,end)
for i in range(1,11):
    print(i)


# In[10]:


#range(start,end,step)
for i in range(1,11,3):
    print(i)

