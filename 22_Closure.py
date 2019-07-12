#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Closures
#In Simple Terms, Closure is a inner function that remembers and
#has access to variables in the local scope in which they are created even after the outer function has finished executing.


# In[2]:


def outer_func():
    msg='Hola'
    
    def inner_func():
        print(msg)
        
    return inner_func()

outer_func()
#first outer_function gets executed which assigns 'Hola' to variable msg. then inner_func() is called.
#it prints msg variable which is not in it's local scope, so it checks it in enclosing scope and prints the value


# In[3]:


#same above example with some modification

def outer_func():
    msg='Hola'
    
    def inner_func():
        print(msg)
        
    return inner_func

my_func=outer_func()  #now my_func is a function containing value of function "inner_func"


# In[4]:


print(my_func)
print(my_func.__name__)


# In[5]:


#now if i execute my_func as function
my_func()              
#it will print the msg value as like above example. my_func was equal to outer_func whose execution was over but inner_func whic is return still have access to msg variable, thats what a closure is.


# In[8]:


#Closure example with parameters
def outer_func(message):
    msg=message
    
    def inner_func():
        print(msg+' kushagra')
        
    return inner_func

hi_func=outer_func("hi")
hi_func()
hello_func=outer_func("hello")
hello_func()

