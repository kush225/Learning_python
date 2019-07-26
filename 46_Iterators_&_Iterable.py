#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Iterators and Iterable
#Iterable means something that can be looped over or specifically object needs to return iterable object from its dunder iter method and the iterator thats returning must find dunder next method which access elements in container one at a time. 
#Something thats Iteratable doesnot mean it's a iterator
#Iterator means it's an object with a state, so it remembers where's at during it's iteration, knows how to fetch next value using __next method and when doesn't have next value it raises StopIteration exception.


# In[2]:


nums = [1,2,3]


# In[3]:


for num in nums:
    print(num)


# In[4]:


#something can be iteratable if it has __iter__ method.
print(dir(nums))
#we can see list has this method


# In[5]:


print(next(nums))
#it actually tries to run dunder next method on that object and list doesnot have dunder next method
#when we ran dunder iter method, it returns iterators for us


# In[11]:


i_nums = nums.__iter__() # or iter(nums)
print(i_nums)
print(dir(i_nums))


# In[12]:


print(next(i_nums))
print(next(i_nums))


# In[13]:


#iterators can only go forward and can't be reset
nums = [1,2,3]
i_nums = iter(nums)
while True:
    try:
        print(next(i_nums))
    except StopIteration:
        break


# In[15]:


class MYRange():
    
    def __init__(self,start,end):
        self.start = start
        self.end = end
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        current = self.start
        self.start += 1
        return current
            


# In[24]:


nums = MYRange(1,10)


# In[17]:


for num in nums:
    print(num)


# In[25]:


print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))


# In[8]:


#same problem using generator
def gen_func(start,end):
    current = start
    while current < end:
        yield current
        current += 1


# In[9]:


my_var = gen_func(1,10)


# In[3]:


for v in my_var:
    print(v)


# In[10]:


print(next(my_var))
print(next(my_var))
print(next(my_var))
print(next(my_var))
print(next(my_var))


# In[9]:


#splitting words from sentence
class Sentence():
    
    def __init__(self,sent):
        self.sent = sent
        self.index = 0
        self.words = self.sent.split()
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        index = self.index
        self.index += 1
        return self.words[index]

words = Sentence("This is a test")


# In[10]:


for word in words:
    print(word)


# In[6]:


#using next method
print(next(words))
print(next(words))
print(next(words))
print(next(words))


# In[20]:


#same problem using generator
def my_gen(sent):
    for word in sent.split():
        yield word


# In[21]:


words = my_gen("this is a test")


# In[19]:


for word in words:
    print(word)


# In[22]:


print(next(words))
print(next(words))
print(next(words))

