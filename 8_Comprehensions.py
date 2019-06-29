#!/usr/bin/env python
# coding: utf-8

# In[1]:


#List Comprehensions
nums=[1,2,3,4,5,6,7,8,9,10]


# In[2]:


#I want 'n' for each 'n' in nums
my_list=[]
for n in nums:
    my_list.append(n)
print(my_list)


# In[4]:


#List Comprehension of above code
my_list=[n for n in nums]
print(my_list)


# In[5]:


#I want 'n*n' for each 'n' in nums
my_list=[]
for n in nums:
    my_list.append(n*n)
print(my_list)


# In[7]:


#List Comprehension of above code
my_list=[n*n for n in nums]
print(my_list)


# In[12]:


#Using map + lambda of above code
my_list= list(map(lambda n: n*n, nums))
print(my_list)


# In[13]:


#I want 'n' for each 'n' in nums if 'n' is even
my_list=[]
for n in nums:
    if n%2==0:
        my_list.append(n)
print(my_list)


# In[16]:


#List Comprehension of above code
my_list = [n for n in nums if n%2==0]
print(my_list)


# In[18]:


#Using filter + lambda of above code
my_list = list(filter(lambda n: n%2 == 0, nums))
print(my_list)


# In[29]:


#I want a (letter,num) pair for each letter in 'abcd' and each number in '0123'
my_list=[]
for letter in 'abcd':
    for num in range(4):
        my_list.append((letter,num))
print(my_list)


# In[32]:


#List Comprehension of above code
my_list = [(letter,num) for letter in 'abcd' for num in range(4)]
print(my_list)


# In[38]:


#Dictionary Comprehensions
names= ['Bruce', 'Clarke', 'Peter', 'Tony', 'Logan', 'Wade']
heros=['Batman', 'Superman', 'Spiderman', 'Iron-man', 'Wolverine', 'Deadpool']


# In[39]:


#zip functions makes tuples matching one-o-one
print(list(zip(names,heros)))


# In[40]:


#I want a dict{'name': 'hero'} for each name in zip(names,heros)
my_dict={}
for name,hero in zip(names,heros):
    my_dict[name]=hero
print(my_dict)


# In[42]:


#Dictionary Comprehension of above code
my_dict={name:hero for name,hero in zip(names,heros)}
print(my_dict)


# In[50]:


#If name not equal to peter
my_dict={name:hero for name,hero in zip(names,heros) if name!= 'Peter' and hero!='Deadpool'}
print(my_dict)


# In[51]:


#Sets Comprehensions
nums=[1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]
my_set=set()
for n in nums:
    my_set.add(n)
print(my_set)


# In[52]:


#Set Comprehension of above code
my_set={n for n in nums}
print(my_set)


# In[53]:


#Generators Expressions
#I want to yield 'n+n' for each 'n' in nums
nums=[1,2,3,4,5,6,7,8,9,10]


# In[61]:


def gen_func(nums):
    for n in nums:
        yield n*n


# In[62]:


my_gen=gen_func(nums)


# In[63]:


for i in my_gen:
    print(i)


# In[70]:


#Above Code using Generator Expression
my_gen=(n*n for n in nums)
for i in my_gen:
    print(i)


# In[ ]:




