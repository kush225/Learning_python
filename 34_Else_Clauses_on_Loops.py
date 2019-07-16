#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Else_Clauses_on_Loops


# In[2]:


#Else With If is common and straight-forward[Either-or case]
num=2
if num < 2:
    print('num is less than 2')
else:
    print('num is not less than 2')


# In[4]:


#Else with for loop
my_list=[1,2,3,4,5]
for i in my_list:
    print(i)
else:
    print('Hit the For/Else Statement')
#else statement will get print if for loop doesnot terminate by a break statement   
#just think else as no break.


# In[5]:


#In this case else statement won't get print
my_list=[1,2,3,4,5]
for i in my_list:
    if i==4:
        break
    print(i)
else:
    print('Hit the For/Else Statement')


# In[6]:


#In this case else statement will print as break statement doesn't get executed.
my_list=[1,2,3,4,5]
for i in my_list:
    if i==6:
        break
    print(i)
else:
    print('Hit the For/Else Statement')


# In[8]:


#same wtih while loop
i=1
while i <=5:
    print(i)
    i+=1
else:
    print("Hit the While/Else Statement")


# In[9]:


#In this case else statement won't get print
i=1
while i <=5:
    print(i)
    i+=1
    if i==3:
        break
else:
    print("Hit the While/Else Statement")


# In[11]:


#In this case else statement will print as break statement doesn't get executed.
i=1
while i <=5:
    print(i)
    i+=1
    if i==7:
        break
else:
    print("Hit the While/Else Statement")


# In[14]:


#Example of Else statement with other loops

def find_index(to_search,target):
    for i,value in enumerate(to_search):
        if value == target:
            break
    else:
        return -1
    return i

my_list=['Bruce','Steve','Tony','Clarke']
index_location = find_index(my_list,'Tony')
print("Location of the Target is at index: {}".format(index_location))
#if value is not equal to target then break statement won't get execute and for loop else will return -1.
index_location2 = find_index(my_list,'oliver')
print("Location of the Target is at index: {}".format(index_location2))


# In[ ]:




