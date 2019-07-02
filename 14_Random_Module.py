#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[23]:


#random() generates floating value between 0 and 1. where 0 is exclusive and 1 is inclusive.
value=random.random()
print(value)


# In[30]:


#uniform() generates floating value between provided range. where 0 is exclusive and 10 is inclusive.
value=random.uniform(1,10)
print(value)


# In[39]:


#randint() generates integer value between provided. range where both are inclusive.
value=random.randint(1,6)
print(value)


# In[53]:


#choice() generates value from the given list
greetings= ['Hello', 'Hi', 'Hey', 'Hola', 'Howdy']
value=random.choice(greetings)
print(value + ', Kushagra!')


# In[54]:


#choices() generates multiple values from the list
#k represent the number of times you want the result to generated. here it generates the list of results.
colors=['Red', 'Black', 'Green']
results= random.choices(colors, k=10)
print(results)


# In[62]:


#using weight we can assign the weightage to each element. here it means 18Red balls, 18 Black balls, 4 Green balls.Total=40balls
colors=['Red', 'Black', 'Green']
results= random.choices(colors,weights=[18,18,4], k=10)
print(results)


# In[64]:


#53 is not inclusive
deck =list(range(1,53))
print(deck)


# In[65]:


#shuffle will shuffle the deck
random.shuffle(deck)
print(deck)


# In[70]:


#sample() will generate not repeated values
hand=random.sample(deck, k=5)
print(hand)

