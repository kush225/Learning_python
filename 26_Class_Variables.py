#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Python Object-Oriented Programming
#Class Variables
#class variables are variables which are shared among all instances of class. whereas
#instance variables are variables which are unique to instances like name, email, pay.


# In[1]:


#Suppose in a class employee we want a raise, as raise will be same for all employees.
#But we are hard coding raise_amount to 1.04%
class Employee:
    def __init__(self, first, last, pay):
        self.first = first   # same as saying emp_1.first = 'Kushagra'
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay=int(self.pay * 1.04)
    
emp_1 = Employee('Kushagra','Gupta',50000)
emp_2 = Employee('Sam','White',30000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)


# In[3]:


#Using Class Variable
class Employee:
    raise_amount=1.04
    
    def __init__(self, first, last, pay):
        self.first = first   # same as saying emp_1.first = 'Kushagra'
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        #self.pay=int(self.pay * raise_amount) #will give error "name 'raise_amount' is not defined"
        self.pay=int(self.pay * Employee.raise_amount) 
        #self.pay=int(self.pay * self.raise_amount) #will work same as above
        
emp_1 = Employee('Kushagra','Gupta',50000)
emp_2 = Employee('Sam','White',30000)
        
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)


# In[5]:


class Employee:
    raise_amount=1.04
    
    def __init__(self, first, last, pay):
        self.first = first   # same as saying emp_1.first = 'Kushagra'
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay=int(self.pay * self.raise_amount) 
        
emp_1 = Employee('Kushagra','Gupta',50000)
emp_2 = Employee('Sam','White',30000)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
#We can access Class Variables both from class and it's instances
#When we try to access an attribute on an instance, it first checks if that instance contain that
#attribute and if it doesn't then it checks whether the class or any class that it inherit from 
#contains that attribute. so when we access raise_amount from instances like emp_1.raise_amount
#or emp_2.raise_amount. they don't have attribute to themselves they are accessing classes
#raise_amount attribute.


# In[6]:


print(emp_1.__dict__) #you can see there is no raise_amount in here


# In[7]:


print(Employee.__dict__) #we can see raise_amount attribute is there in class


# In[8]:


Employee.raise_amount=1.05 #this will change raise amount for the class and all the instances.

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)


# In[11]:


emp_1.raise_amount=1.1 #this will create namespace of raise_amount in emp_1

print(emp_1.__dict__) #raise_amount will be in the namespace of emp1
print(emp_2.__dict__) #but not in emp_2 as it still using Employee's.
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)


# In[13]:


class Employee:
    num_of_emps=0
    raise_amount=1.04
    
    def __init__(self, first, last, pay):
        self.first = first   # same as saying emp_1.first = 'Kushagra'
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
        Employee.num_of_emps +=1
    #here we use Employee not self because there is not use case where we want total no. of employee
    #different for different instances
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay=int(self.pay * self.raise_amount)  
#here using self.raise_amount instead of Employee.raise_amount will give us ability to change 
#raise amount for different instances. Otherwise it will be same for all instances

print(Employee.num_of_emps) #this will result zero as we have not initiated Employee.

emp_1 = Employee('Kushagra','Gupta',50000)
emp_2 = Employee('Sam','White',30000)

print(Employee.num_of_emps)  #this will result two as we have nitiated Employee twice.

