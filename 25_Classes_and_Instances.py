#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Python Object-Oriented Programming
#Classes and Instances


# In[2]:


#Why to Use Class?
#1) they allow us to logically group our data(attributes) and function(methods) in a way to easy to reuse and easy to build upon if need.
#methods- function associated with class
#attributes- data associated with class


# In[3]:


class Employee: #A class is a blueprint for creating instances.
    pass

#Instance Variable
#Each of this are own unique instances of class Employee
emp_1 = Employee()
emp_2 = Employee()

#Both are unique as both have different location
print(emp_1)
print(emp_2)

#Instance Variable are those who contain data unique to each Instance.


# In[4]:


#we don't get any benefit of classes, if we do it this way. and the better way is to use init method(constructor)
emp_1.first = 'Kushagra'
emp_1.last = 'Gupta'
emp_1.email = 'Kushagra.Gupta@company.com'
emp_1.pay = 50000

emp_2.first = 'Sam'
emp_2.last = 'White'
emp_2.email = 'Sam.White@company.com'
emp_2.pay = 30000

print(emp_1.email)

print(emp_2.email)


# In[7]:


#init method(constructor)
#when we create method within a class they received the instance as the first argument automatically.
#you can call the instance anything but by convention we call it as self.
class Employee:
    def __init__(self, first, last, pay):
        self.first = first   # same as saying emp_1.first = 'Kushagra'
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
emp_1 = Employee('Kushagra','Gupta',50000)
#init method will be run automatically and emp_1 will be passed as self and set all the attributes
#like emp_1.last ='Gupta'
emp_2 = Employee('Sam','White',30000)

print(emp_1.email)

print(emp_2.email)
#we can get full name 
print('{} {}'.format(emp_1.first, emp_1.last))


# In[30]:


#Better way to get fullname by creating a method for that
class Employee:
    def __init__(self, first, last, pay):
        self.first = first   # same as saying emp_1.first = 'Kushagra'
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
emp_1 = Employee('Kushagra','Gupta',50000)
emp_2 = Employee('Sam','White',30000)
    
print(emp_2.fullname) #prints method not it's return value
print(emp_2.fullname()) #we need parenthesis as it's method not attribute


# In[27]:


class Employee:
    def __init__(self, first, last, pay):
        self.first = first   # same as saying emp_1.first = 'Kushagra'
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
    def fullname():
        return '{} {}'.format(self.first, self.last)
    
emp_1 = Employee('Kushagra','Gupta',50000)
emp_2 = Employee('Sam','White',30000)
    
print(emp_1.fullname())
#fullname() takes 0 positional arguments but 1 was given. when we emp_1.fullname()
#it means emp_1 is automatically passed like fullname(emp_1) as an argument but
#fullname method doesnot have place for any argument so we have to add self
#as an argument in fullname method


# In[33]:


class Employee:
    def __init__(self, first, last, pay):
        self.first = first   # same as saying emp_1.first = 'Kushagra'
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
emp_1 = Employee('Kushagra','Gupta',50000)
emp_2 = Employee('Sam','White',30000)

print(Employee.fullname(emp_1))
print(emp_1.fullname())  #In background this transform as this print(Employee.fullname(emp_1))
#Both works the same but on first case it i have to pass instance manually as it doesn't know 
#which instance to use.. In second case self is passed automatically

