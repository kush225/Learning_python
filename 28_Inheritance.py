#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Python Object-Oriented Programming
#Inheritance - Creating Subclasses
#Inheritance allows to inherit attributes and methods from parent class and now this is useful
#because we create subclasses with all the functionality of parent class and we can overwrite
#or add new functionality without affecting parent class in any way.


# In[4]:


class Employee:
    raise_amount=1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay=int(self.pay * self.raise_amount)  


# In[8]:


#Creating Developer class by inheriting from Employee class
class Developer(Employee):
    pass

#we don't have anything in our developer class but still we have inherit from employee class 
dev_1 = Developer('Kushagra','Gupta',50000)
dev_2 = Developer('Sam','White',30000)

print(dev_1.email)
print(dev_2.email)

print(help(Developer))
#python first checks in Developer class then Employee class and then builtins.object
#this is method resolution order


# In[9]:


print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)


# In[14]:


#changing value in subclass
class Employee:
    raise_amount=1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay=int(self.pay * self.raise_amount)  

class Developer(Employee):
    raise_amount= 1.10  #changing raise value for developers

dev_1 = Developer('Kushagra','Gupta',50000)
dev_2 = Developer('Sam','White',30000)

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)


# In[17]:


#sometimes we want to give subclasses more information then parent classes
#suppose we also want to pass programming language with first name,last name, pay
#for that we have to give Developer class it's own init method.

class Developer(Employee):
    raise_amount= 1.10
    
    def __init__(self, first, last, pay, prog_language):
        super().__init__(first,last,pay) 
        #super.__init__ will allow Employee class to pass first, last, pay
        #or you can use Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_language
    
dev_1 = Developer('Kushagra','Gupta',50000,'python')
dev_2 = Developer('Sam','White',30000,'java')

print(dev_1.email)
print(dev_1.prog_lang)
print(dev_2.prog_lang)


# In[23]:


#A Manager class inheriting from Employee class
class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first,last,pay) 
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    #method to add employee
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    #method to remove employee
    def rem_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
    #method to print employee      
    def print_emp(self):
        for emp in self.employees:
            print('-->',emp.fullname())
            
mgr_1 = Manager('Sue','Smith',90000,[dev_1])

print(mgr_1.email)
mgr_1.print_emp()

print()
mgr_1.add_emp(dev_2)
mgr_1.print_emp()


# In[27]:


#isinstance will tell if an object is an instance of class.
#clearly mgr_1 is an instance of Manager and Employee class but not of Developer Class.
print(isinstance(mgr_1, Manager)) 
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))


# In[29]:


#issubclass will tell if a class is a subclass of another
print(issubclass(Developer,Employee))
print(issubclass(Manager,Employee))
print(issubclass(Developer,Manager))
print(issubclass(Developer,Developer))

