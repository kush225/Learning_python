#!/usr/bin/env python
# coding: utf-8

# In[25]:


#Python Object-Oriented Programming
#Special Methods(Magic/Dunder)
#Dunder or magic methods in Python are the methods having two prefix and suffix underscores in the method name. Dunder here means “Double Under (Underscores)”. These are commonly used for operator overloading. Few examples for magic methods are: __init__, __add__, __len__, __repr__ etc.


# In[3]:


#so according to what objects you are working on addition have different behavior
#On integers it simply adds
print(1+2)
#On strings it concatenates
print('a'+'b')


# In[4]:


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

print(emp_1)
#this print employee object but this is not understandable. Using Special methods we will be able to print something userfriendly. By Defining our special method we will be able to change this built-in behavior.


# In[7]:


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
        
    def __repr__(self):   #__ means dunder
        return "Employee('{}', '{}', '{}'')".format(self.first,self.last,self.pay)
    
    def __str__(self):     
        return "{} - {}".format(self.fullname(),self.email)
emp_1 = Employee('Kushagra','Gupta',50000)
emp_2 = Employee('Sam','White',30000)

#now this will be more readable to end user.
print(emp_2)


# In[10]:


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
        
    def __repr__(self):   #__ means dunder
        return "Employee('{}', '{}', '{}'')".format(self.first,self.last,self.pay)
    
    def __str__(self):     
        return "{} - {}".format(self.fullname(),self.email)
emp_1 = Employee('Kushagra','Gupta',50000)
emp_2 = Employee('Sam','White',30000)

#now after defining __str__ this will use __str__ insed of __repr__
print(emp_2)


# In[11]:


#to access __repr__ and __str__ specifically, we can use
print(repr(emp_1)) 
print(str(emp_1))


# In[12]:


# above two print line is equivalent to these and in background it interprets this way
print(emp_1.__repr__())
print(emp_1.__str__())


# In[15]:


print(1+2)
#is equivalent to
print(int.__add__(1,2))
#whereas
print('a'+'b')
#is equivalent to 
print(str.__add__('a','b'))


# In[16]:


#It doesn't know how to add to Employee
print(emp_1 + emp_2)
#so we will make a function dunder add for that (__add__)


# In[17]:


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
        
    def __repr__(self):   #__ means dunder
        return "Employee('{}', '{}', '{}'')".format(self.first,self.last,self.pay)
    
    def __str__(self):     
        return "{} - {}".format(self.fullname(),self.email)
    
    def __add__(self, other):
        return self.pay + other.pay
    
emp_1 = Employee('Kushagra','Gupta',50000)
emp_2 = Employee('Sam','White',30000)

print(emp_1+emp_2)


# In[23]:


print(len('test'))
#is equivalent to dunder len (__len__)
print('test'.__len__())

#this will give error as employee doesn't have any method to handle this. so we will make one.
print(len(emp_1))


# In[24]:


#So suppose when we run dunder len(__len__) method in employee instance it will written total no. of characters in their fullname.
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
        
    def __repr__(self):   #__ means dunder
        return "Employee('{}', '{}', '{}'')".format(self.first,self.last,self.pay)
    
    def __str__(self):     
        return "{} - {}".format(self.fullname(),self.email)
    
    def __add__(self, other):
        return self.pay + other.pay
    
    def __len__(self):
        return self.fullname().__len__()
        #or return len(self.fullname())
    
    
emp_1 = Employee('Kushagra','Gupta',50000)
emp_2 = Employee('Sam','White',30000)

#this will print number of characters in fullname of employee.
print(len(emp_1))

