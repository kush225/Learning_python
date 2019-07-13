#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Named Tuple
#A named tuple is exactly like a normal tuple, except that the fields can also be accessed by .fieldname. 
#Named tuples are still immutable, you can still index elements with integers, and you can iterate over the elements


# In[1]:


##Tuple
#color RGB
color = (55,155,255)
#if i want red color from tuple, i will simply print
print(color[0])
#but that's not understandable if someone look at this or even if i look at this later. so instead of this we can use dictionary.


# In[3]:


##Dictionary
#color RGB
color ={'red':55,'green':155,'blue':255}
#if i want red color from tuple, i will simply print
print(color['red'])
#we can do this, its understandable to others but it requires more typing.. and also this are mutable. what if we want immutable, then we can use named_tuple.


# In[6]:


##Named_Tuple
from collections import namedtuple
#color RGB
Color=namedtuple('Color',['red','green','blue'])
color=Color(55,155,255)
print(color[0]) # i can use this as regular tuple and print like i did before
print(color.red) # or i can call it by name.

#this is more readable


# In[9]:


Color=namedtuple('Color',['red','green','blue'])
color=Color(green=55,red=155,blue=255) #you can be explicit for more clarity.
print(color.red)

