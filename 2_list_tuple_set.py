#!/usr/bin/env python
# coding: utf-8

# In[1]:


courses =['History' , 'Physics' , 'Maths', 'English']
courses2 = ['Art', 'Education']


# In[2]:


courses.append('Art')


# In[4]:


print(courses)


# In[5]:


courses.insert(0, courses2)


# In[6]:


print(courses)


# In[20]:


#extend is used so list wont get appended inside list
courses =['History' , 'Physics' , 'Maths', 'English']
courses.extend(courses2)


# In[21]:


print(courses)


# In[22]:


#removes last item and stored in a variable
popped= courses.pop()
print(popped)


# In[29]:


#reverse the order
courses.reverse()
print(courses)


# In[31]:


#sort the list in desc order when reverse is true
courses.sort(reverse=True)
print(courses)


# In[33]:


#sorted version of list is not reflected in original list
print(sorted(courses))


# In[34]:


#finding index

print(courses.index('Maths'))


# In[35]:


#finding element in list

print('English' in courses)


# In[36]:


#Printing each element of list
for course in courses:
    print(course)


# In[37]:


#Printing each element with index
for index, course in enumerate(courses, start=1):
    print(index,course)


# In[40]:


#Making String from list
course_str = ', '.join(courses)

print(course_str)


# In[42]:


#Making List from String
new_list= course_str.split(', ')

print(new_list)


# In[43]:


cs_courses={'Maths', 'Physics', 'English', 'Sports','Chemistry' }
art_courses={'Maths', 'Art', 'English', 'Sports','Hindi' }


# In[44]:


#Common in both the lists
print(cs_courses.intersection(art_courses))


# In[45]:


#Element in list1 but not in list2
print(cs_courses.difference(art_courses))


# In[46]:


#All Elements combined from both the list
print(cs_courses.union(art_courses))


# In[47]:


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

