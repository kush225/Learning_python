#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Comprehension
#Comprehensions in Python provide us with a short and concise way to construct new sequences (such as lists, set, dictionary etc.) using sequences which have been already defined.


# In[1]:


#List Comprehension
#List comprehensions are used for creating new list from another iterables. As list comprehension returns list, they consists of brackets containing the expression which needs to be executed for each element along with the for loop to iterate over each element.


# In[2]:


#list
nums=[1,2,3,4,5,6,7,8,9,10]


# In[3]:


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


# In[6]:


#List Comprehension of above code
my_list=[n*n for n in nums]
print(my_list)


# In[7]:


#Using map + lambda of above code
my_list= list(map(lambda n: n*n, nums))
print(my_list)


# In[8]:


#I want 'n' for each 'n' in nums if 'n' is even
my_list=[]
for n in nums:
    if n%2==0:
        my_list.append(n)
print(my_list)


# In[9]:


#List Comprehension of above code
my_list = [n for n in nums if n%2==0]
print(my_list)


# In[10]:


#Using filter + lambda of above code
my_list = list(filter(lambda n: n%2 == 0, nums))
print(my_list)


# In[11]:


#I want a (letter,num) pair for each letter in 'abcd' and each number in '0123'
my_list=[]
for letter in 'abcd':
    for num in range(4):
        my_list.append((letter,num))
print(my_list)


# In[12]:


#List Comprehension of above code
my_list = [(letter,num) for letter in 'abcd' for num in range(4)]
print(my_list)


# In[13]:


#Dictionary Comprehensions
#Dict comprehension is defined with a similar syntax as of list comprehension, but with a key:value pair in expression


# In[14]:


#Dictionary
names= ['Bruce', 'Clarke', 'Peter', 'Tony', 'Logan', 'Wade']
heros=['Batman', 'Superman', 'Spiderman', 'Iron-man', 'Wolverine', 'Deadpool']


# In[15]:


#zip functions makes tuples matching one-o-one
print(list(zip(names,heros)))


# In[16]:


#I want a dict{'name': 'hero'} for each name in zip(names,heros)
my_dict={}
for name,hero in zip(names,heros):
    my_dict[name]=hero
print(my_dict)


# In[17]:


#Dictionary Comprehension of above code
my_dict={name:hero for name,hero in zip(names,heros)}
print(my_dict)


# In[18]:


#If name not equal to peter
my_dict={name:hero for name,hero in zip(names,heros) if name!= 'Peter' and hero!='Deadpool'}
print(my_dict)


# In[20]:


#Sets Comprehensions


# In[21]:


#list
nums=[1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]
#empty set
my_set=set()
for n in nums:
    my_set.add(n)
print(my_set)


# In[22]:


#Set Comprehension of above code
my_set={n for n in nums}
print(my_set)


# In[23]:


#Generators Expressions
#List
nums=[1,2,3,4,5,6,7,8,9,10]


# In[24]:


#I want to yield 'n+n' for each 'n' in nums
def gen_func(nums):
    for n in nums:
        yield n*n


# In[25]:


#creates a generator object
my_gen=gen_func(nums)


# In[26]:


#printing each element from generator object
for i in my_gen:
    print(i)


# In[27]:


#Above Code using Generator Expression
my_gen=(n*n for n in nums)
for i in my_gen:
    print(i)

