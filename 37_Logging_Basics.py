#!/usr/bin/env python
# coding: utf-8

# In[18]:


#Logging_Basics
#Logging to files, Setting Levels and Formatting
#Logging Levels: 5 types (by default only warning, error, critical is enabled by python)
# Debug: Detailed information, typically of interest only when diagnosing problems.
# Info: Confirmation that things are working as expected.
# Warning: An indication that something unexpected happened, or indicative of some problem in the nead future(e.g. 'disk space low'). The Software is still working as expected.
# Error: Due to a more serious problem, the software has not been able to perform some function.
# Critical: A serious error, indicating that the program itslef may be unable to continue running.


# In[19]:


def add(x,y):
    """Add Function"""
    return x + y
def subtract(x,y):
    """Subtract Function"""
    return x - y
def multiply(x,y):
    """Multiply Function"""
    return x * y
def divison(x,y):
    """Divide Function"""
    return x / y


# In[20]:


num_1=10
num_2=5


# In[21]:


#To check whether your code run correctly you need to print the output but instead of printing you can use logging
add_result= add(num_1,num_2)
print('Add: {} + {} = {}'.format(num_1,num_2,add_result))
sub_result= subtract(num_1,num_2)
print('Subtract: {} + {} = {}'.format(num_1,num_2,sub_result))
multiply_result= multiply(num_1,num_2)
print('Multiply: {} + {} = {}'.format(num_1,num_2,multiply_result))
divide_result= divison(num_1,num_2)
print('Divison: {} + {} = {}'.format(num_1,num_2,divide_result))


# In[6]:


import logging
import subprocess


# In[2]:


#configure logging root.. filename is used so that logs will be appending in file instead of showing on terminal, and we are setting logging level to debug
logging.basicConfig(filename='test.log',level=logging.DEBUG)


# In[3]:


def add(x,y):
    """Add Function"""
    return x + y
def subtract(x,y):
    """Subtract Function"""
    return x - y
def multiply(x,y):
    """Multiply Function"""
    return x * y
def divison(x,y):
    """Divide Function"""
    return x / y
num_1=10
num_2=5


# In[4]:


add_result= add(num_1,num_2)
logging.debug('Add: {} + {} = {}'.format(num_1,num_2,add_result))
sub_result= subtract(num_1,num_2)
logging.debug('Subtract: {} + {} = {}'.format(num_1,num_2,sub_result))
multiply_result= multiply(num_1,num_2)
logging.debug('Multiply: {} + {} = {}'.format(num_1,num_2,multiply_result))
divide_result= divison(num_1,num_2)
logging.debug('Divison: {} + {} = {}'.format(num_1,num_2,divide_result))
#logging file will be created


# In[8]:


#subprocess module is used to show data in file
subprocess.getoutput('cat test.log')
#imagine \n as new line.


# In[15]:


#Another Example which was used in 31_Property_Decorators
import logging

#you can set the format of log. and for more format option check python documentation
logging.basicConfig(filename='Employee.log',level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

class Employee:
    
    def __init__(self, first, last):
        self.first = first
        self.last = last
        
        logging.info("Employee Created: {} - {}".format(self.fullname,self.email))
        
    @property  
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @property
    def email(self):
        return "{}.{}@company.com".format(self.first,self.last)
    
emp_1 = Employee('Kushagra','Gupta')
emp_2 = Employee('Jane','Doe')
emp_3 = Employee('Sam','Williams')


# In[16]:


#subprocess module is used to show data in file
subprocess.getoutput('cat Employee.log')
#imagine \n as new line.


# In[ ]:




