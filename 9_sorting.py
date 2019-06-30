#!/usr/bin/env python
# coding: utf-8

# In[7]:


my_list=[9,1,8,2,7,3,6,4,5]


# In[8]:


#sorted function returns the sorted list
sort_list= sorted(my_list)


# In[13]:


print("Sorted List:\t",sort_list)


# In[14]:


print("Original List:\t", my_list)


# In[15]:


#To sort the original list, you can use sort method. It doesnot returns the list just sort the original one.
my_list.sort()


# In[16]:


#Original List gets sorted
print("Original List:\t", my_list)


# In[19]:


#To Sort in Descending Order with sorted function
my_list=[9,1,8,2,7,3,6,4,5]
sort_list= sorted(my_list, reverse=True)
print("Sorted List:\t",sort_list)


# In[20]:


#To Sort in Descending Order with sort method
my_list.sort(reverse=True)
print("Original List:\t", my_list)


# In[21]:


#tuples dont have sort method
my_tup=(9,1,8,2,7,3,6,4,5)
my_tup.sort()


# In[23]:


#you can use sorted function to sort but it will return it as a list
my_tup=(9,1,8,2,7,3,6,4,5)
sorted_tup = sorted(my_tup)
print("Tuple:\t",sorted_tup)


# In[27]:


#Dictionary
#you can use sorted function to sort but it will return it as a list of keys
my_dic={'name':'Kushagra','age':23, 'phone':9878856899,'location':'delhi'}
sorted_dic = sorted(my_dic)
print("Sorted Dic:\t", sorted_dic)


# In[25]:


#Dictionary dont have sort method
my_dic.sort()


# In[28]:


li=[-6,-5,-4,1,2,3]
s_li=sorted(li)
print(s_li)


# In[29]:


#using abs, you can ignore -ve sign
s_li=sorted(li,key=abs)
print(s_li)


# In[30]:


##################


# In[31]:


class Employee():
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
        
    def __repr__(self):
        return f"({self.name}, {self.age}, ${self.salary})"
    
e1=Employee('Carl',37,70000)
e2=Employee('Sarah',29,80000)
e3=Employee('John',43,90000)

employees=[e1,e2,e3]
print(employees)


# In[32]:


#this won't work because it doesnot know on which element to sort
s_employees=sorted(employees)
print(s_employees)


# In[33]:


#making a sort function to used in a key
def e_sort(emp):
    return emp.name

s_employees=sorted(employees,key=e_sort)
print(s_employees)


# In[37]:


#using lambda function
s_employees=sorted(employees,key=lambda e:e.salary, reverse=True)
print(s_employees)


# In[36]:


#using attrgetter
from operator import attrgetter
s_employees=sorted(employees,key=attrgetter('age'))
print(s_employees)

