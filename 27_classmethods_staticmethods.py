#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Python Object-Oriented Programming
#classmethods and staticmethods


# In[2]:


#regular methods take instance as a 1st argument and by convention we were calling it as self,
class Employee:
    num_of_emps=0
    raise_amount=1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    
        Employee.num_of_emps +=1
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay=int(self.pay * self.raise_amount)  

emp_1 = Employee('Kushagra','Gupta',50000)
emp_2 = Employee('Sam','White',30000)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)


#so how to change that it will take class as 1st argument to do that we will use classmethods


# In[5]:


#classmethod

class Employee:
    num_of_emps=0
    raise_amount=1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    
        Employee.num_of_emps +=1
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay=int(self.pay * self.raise_amount)  
    
    @classmethod #Decorator
    def set_raise_amt(cls,amount): #by convention we use cls in class method like we use self.
        cls.raise_amount=amount
        
emp_1 = Employee('Kushagra','Gupta',50000)
emp_2 = Employee('Sam','White',30000)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

Employee.set_raise_amt(1.05) #this will set the raise amount to 1.05
#same as saying Employee.raise_amount=1.05

#emp_1.set_raise_amt(1.05) #will work same as above changes class variable for all instances,
#but that doesnot make any sense.

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)


# In[6]:


#suppose we have employee details spliting by '-' and we want to add in employee class

emp_str_1 ='John-wick-70000'
emp_str_2 ='bruce-wayne-100000'

first, last, pay = emp_str_1.split('-')

new_emp_1 = Employee(first, last, pay)

print(new_emp_1.email)
print(new_emp_1.pay)


# In[10]:


#classmethod as alternative constructor
#we can create an alternative constructor so we don't have to do above steps manually

class Employee:
    num_of_emps=0
    raise_amount=1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    
        Employee.num_of_emps +=1
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay=int(self.pay * self.raise_amount)  
    
    @classmethod #Decorator
    def set_raise_amt(cls,amount): #by convention we use cls in class method like we use self.
        cls.raise_amount=amount
        
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
emp_1 = Employee('Kushagra','Gupta',50000)
emp_2 = Employee('Sam','White',30000)
    
emp_str_1 ='John-wick-70000'
emp_str_2 ='bruce-wayne-100000'

new_emp_1 =Employee.from_string(emp_str_1)
new_emp_2 =Employee.from_string(emp_str_2)

print(new_emp_1.email)
print(new_emp_2.email)


# In[9]:


#staticmethod
#these method don't pass anything automatically like regular methods automatically pass instance
#we call that self.. class methods automatically pass class we call that cls.
#staticmethod works like regular function


# In[12]:


#we want a simple function that would take a date and return whether it's a workday or not.
#this has a logical connection to our employee class but it doesn't depend on any instance
#or class variable

class Employee:
    num_of_emps=0
    raise_amount=1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    
        Employee.num_of_emps +=1
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay=int(self.pay * self.raise_amount)  
    
    @classmethod #Decorator
    def set_raise_amt(cls,amount): #by convention we use cls in class method like we use self.
        cls.raise_amount=amount
        
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() ==5 or day.weekday() ==6: #5 means saturday and 6 means sunday
            return False
        return True

emp_1 = Employee('Kushagra','Gupta',50000)
emp_2 = Employee('Sam','White',30000)

import datetime #module to create date
my_date= datetime.date(2016,7,10)

print(Employee.is_workday(my_date)) #False as sunday

my_date= datetime.date(2016,7,11)

print(Employee.is_workday(my_date)) #True as monday

