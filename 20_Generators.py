#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Generators are simple functions which return an iterable set of items, one at a time, in a special way.


# In[1]:


#Normal Function returning square of numbers
def square_numbers(nums):
    result=[]
    for i in nums:
        result.append(i*i)
    return result

my_nums=square_numbers([1,2,3,4,5])
print(my_nums)


# In[7]:


#Same code using Generators
def square_numbers(nums):
    for i in nums:
        yield(i*i)

my_nums=square_numbers([1,2,3,4,5])
print(my_nums) 

#values will only be calculated when called
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))


# In[8]:


#All values are exhausted, so it will raise exception
print(next(my_nums))


# In[14]:


#you can use for loop to iterate through generator
my_nums=square_numbers([1,2,3,4,5])
for num in my_nums:
    print(num)


# In[15]:


#Advantages:
#Better readablity
#Better Performance as not holding all values in memory


# In[16]:


#Same using List Comprehension
my_nums=[x*x for x in [1,2,3,4,5]]
print(my_nums)


# In[18]:


#Generator written like list comprehension
my_nums=(x*x for x in [1,2,3,4,5])
print(my_nums)

for num in my_nums:
    print(num)


# In[21]:


#Converting Generator object to list
my_nums=(x*x for x in [1,2,3,4,5]) 
print(list(my_nums))   #when you convert generator to list, you lose benefits of generator#


# In[22]:


#Example why to use generators


# In[1]:


import resource
import random
import time

names=['john', 'corey','adam', 'steve','rick','thomas']
majors=['math','engineering','compsci','arts','business']

print(f'Memory (Before): {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}')

#Function using list
def people_list(num_people):
    result=[]
    for i in range(num_people):
        person={
                'id':i,
                'name':random.choice(names),
                'major':random.choice(majors)
                }
        result.append(person)
    return result



t1=time.time()
people=people_list(1000000)
t2=time.time()

print(f'Memory (After): {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}')
print(f'Took {t2-t1} seconds')


# In[11]:


import resource
import random
import time

names=['john', 'corey','adam', 'steve','rick','thomas']
majors=['math','engineering','compsci','arts','business']

print(f'Memory (Before): {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}')


#Function using generators
def people_generator(num_people):
    for i in range(num_people):
        person={
                'id':i,
                'name':random.choice(names),
                'major':random.choice(majors)
                }
        yield(person)



t1=time.time()
people=people_generator(1000000)
t2=time.time()

print(f'Memory (After): {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}')
print(f'Took {t2-t1} seconds')

#but if we iterator over every item, elapsed time would be getter than that of list but memory consumption would be much lesser than that of list 

