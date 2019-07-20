#!/usr/bin/env python
# coding: utf-8

# In[1]:


#There are four collection data types in the Python programming language:

#LIST
#It is a collection which is ordered and mutable(changeable) which Allows duplicate members.

#TUPLES
#It is a collection which is ordered and unmutable(unchangeable) which Allows duplicate members.

#SETS
#It is a collection which is unordered and unindexed which doesn't Allow duplicate members.

#DICTIONARY
#It is a collection which is unordered, changeable and indexed which doesn't Allow duplicate mem


# In[2]:


#courses is list containing elements history, physics, maths and english
courses =['History' , 'Physics' , 'Maths', 'English']
courses2 = ['Art', 'Education']


# In[3]:


#this will print the whole list
print(courses)


# In[4]:


#you can access any element of list using index number which begins from 0.
#to print maths which is at index 2, simply write list[index_no]
print(courses[2])


# In[5]:


#insert method is used add element at given index
#in this courses2 list is added to courses list at index 0.
courses.insert(0, courses2)


# In[7]:


#list gets appended inside list. to avoid this we can use extend method.
print(courses)


# In[8]:


#extend is used so list wont get appended inside list
courses =['History' , 'Physics' , 'Maths', 'English']
courses.extend(courses2)


# In[9]:


#new list
print(courses)


# In[10]:


#pop() removes last item and we can store it in a variable
popped= courses.pop()
print(popped)


# In[11]:


#reverse the order using reverse method
courses.reverse()
print(courses)


# In[12]:


#sort the list in desc order when reverse is true
courses.sort(reverse=True)
print(courses)


# In[14]:


#sorted version of list is not reflected in original list
print(sorted(courses))
#order remains same as it was before using sorted method
print(courses)


# In[15]:


#finding index
print(courses.index('Maths'))


# In[16]:


#finding element in list, True if there and False is not
print('English' in courses)


# In[17]:


#Printing each element of list
for course in courses:
    print(course)


# In[18]:


#Printing each element with index
for index, course in enumerate(courses, start=1): 
#as start=1, index will be start from 1, default is 0
    print(index,course)


# In[19]:


#Making String from list
course_str = ', '.join(courses)
print(course_str)


# In[20]:


#Making List from String
new_list= course_str.split(', ')
print(new_list)


# In[21]:


#Set
cs_courses={'Maths', 'Physics', 'English', 'Sports','Chemistry' }
art_courses={'Maths', 'Art', 'English', 'Sports','Hindi' }


# In[22]:


#Common in both the sets
print(cs_courses.intersection(art_courses))


# In[23]:


#Element in set1 but not in set2
print(cs_courses.difference(art_courses))


# In[24]:


#All Elements combined from both the set
print(cs_courses.union(art_courses))


# In[25]:


#Creating empty list, tuple, set, dictionary
#Empty list
empty_list = []
empty_list = list()

#Empty Tuple
empty_tuple = ()
empty_tuple = tuple()

#Empty Set
empty_set = {} #this is wrong, this will create empty dictionary
empty_set = set()

