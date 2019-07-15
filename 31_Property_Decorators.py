#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Python Object-Oriented Programming
#Property Decorators - Getters, Setters and Deleters


# In[7]:


class Employee:
    raise_amount=1.04
    
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
emp_1 = Employee('Kushagra','Gupta')

print(emp_1.first)
print(emp_1.last)
#email is combination of first name and last name
print(emp_1.email)
print(emp_1.fullname())


# In[9]:


#so if now i will change the first name

emp_1.first = "Jim" 

#first name got changed
print(emp_1.first)
#But email which was dependent on first and last name is same as previous name.
print(emp_1.email)
#But fullname doesn't have this problem. becoz everytime fullname is called it goes back to class and rerun the fullname method
print(emp_1.fullname())

#To workaround this email issue you will be thinking just to make another method that will print email like fullname. But problem with that it will break the code for everyone who is using class they have to change the code from email attribute to email method.


# In[10]:


#the above problem can be solved using getter and setter but in python it can be solved using property decorator.
#The main purpose of any decorator is to change your class methods or attributes in such a way so that the user of your class no need to make any change in their code.

class Employee:
    raise_amount=1.04
    
    def __init__(self, first, last):
        self.first = first
        self.last = last
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def email(self):
        return "{}.{}@company.com".format(self.first,self.last)
    
emp_1 = Employee('Kushagra','Gupta')
print(emp_1.email())
emp_1.first = "Jim" 
print(emp_1.email())
#this will work but we don't want to change code for every email attribute to email method


# In[15]:


#so to keep accessing email method as attribute, we need to add property decorator above email method.
#Getters

class Employee:
    raise_amount=1.04
    
    def __init__(self, first, last):
        self.first = first
        self.last = last
    @property  
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @property
    def email(self):
        return "{}.{}@company.com".format(self.first,self.last)
    
emp_1 = Employee('Kushagra','Gupta')
print(emp_1.email)
emp_1.first = "Jim" 
print(emp_1.email)

#we are defining email as a method but accessing it as an attribute.


# In[16]:


#so now if i want to change an attribute like

emp_1.fullname ="Jim harper"
print(emp_1.fullname)
print(emp_1.email)

#it will throw error "can't set attribute"


# In[17]:


#so to change value of attribute we will be needing setter.
#Setters
class Employee:
    raise_amount=1.04
    
    def __init__(self, first, last):
        self.first = first
        self.last = last
    @property  
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @property
    def email(self):
        return "{}.{}@company.com".format(self.first,self.last)
    
    @fullname.setter  #we need to name the decorator with the method which we want to change+ '.setter'
    def fullname(self,name): #another method with same name
        first, last = name.split(' ')
        self.first = first
        self.last = last

emp_1 = Employee('Kushagra','Gupta')

print(emp_1.fullname)
print(emp_1.email)
emp_1.fullname ="Jim harper"
print(emp_1.fullname)
print(emp_1.email)
#so what happen here is when we set fullname equal to name given, it came to our setter their and parse the names we want to set from out string and since we set first name and last name even we have printed out our email, it came above and printed the correct email. 


# In[21]:


#Deleters

class Employee:
    raise_amount=1.04
    
    def __init__(self, first, last):
        self.first = first
        self.last = last
    @property  
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @property
    def email(self):
        return "{}.{}@company.com".format(self.first,self.last)
    
    @fullname.setter  
    def fullname(self,name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
        
    @fullname.deleter  
    def fullname(self):
        print("Name Deleted!")
        self.first = None
        self.last = None

emp_1 = Employee('Kushagra','Gupta')

print(emp_1.first)
print(emp_1.fullname)
print(emp_1.email)
#this will delete our fullname 
del emp_1.fullname
print(emp_1.fullname)

