#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Decorators
#must know Firstclass Function and closure. 
#A Decorator is just a function takes another function as arguments, adds some kind of functionality then returns another function,
#all of this without altering the source code of tne original function you passed in.


# In[13]:


def decorator_func(original_func):
    def wrapper_func():
        print('wrapper function ran before {0}'.format(original_func.__name__))
        return original_func()
    return wrapper_func

def display_func():
    print('Display Function Ran')


# In[16]:


decorated_display=decorator_func(display_func)   
#first decorator_func gets executed and assigning display_func to original_func and returns wrapper_func object and 
#gets stored in decorated_display function.


# In[15]:


decorated_display()
#when decorated_display func which is wrapper_func gets executed printing the message inside wrapper_func and 
#executing original function which is display_func and printing the code inside it.


# In[20]:


#same as above 
def decorator_function(original_function):
    def wrapper_function():
        print('wrapper function ran before {0}'.format(original_function.__name__))
        return original_function()
    return wrapper_function

@decorator_function    #same as, display =decorator_function(display)
def display():
    print('Display Function Ran')

display()


# In[23]:


def decorator_function(original_function):
    def wrapper_function():
        print('wrapper function ran before {0}'.format(original_function.__name__))
        return original_function()
    return wrapper_function
    
@decorator_function
def display_info(name,age):
    print('display_info ran with arguments ({0} {1})'.format(name,age))
    
display_info('kushagra',23)
#will display error " wrapper_function() takes 0 positional arguments but 2 were given" bcoz wrapper_function doesnt take any argument.


# In[26]:


def decorator_function(original_function):
    def wrapper_function(*args,**kwargs):
        #by adding argument *args and **kwargs.. function will take any number of positional argument and keyord arguemnts
        print('wrapper function ran before {0}'.format(original_function.__name__))
        return original_function(*args,**kwargs)
    return wrapper_function

@decorator_function    #same as, display =decorator_function(display)
def display():
    print('Display Function Ran')
    
@decorator_function
def display_info(name,age):
    print('display_info ran with arguments ({0} {1})'.format(name,age))
    
display()

display_info('kushagra',23)


# In[30]:


#Using Decorator Class instead of Decorator Function

class decorator_class(object):
    def __init__(self, original_function):
        self.original_function= original_function
        
    def __call__(self, *args, **kwargs):
        print('class method ran before {0}'.format(self.original_function.__name__))
        return self.original_function(*args,**kwargs)
    
@decorator_class  
def display():
    print('Display Function Ran')
    
@decorator_class
def display_info(name,age):
    print('display_info ran with arguments ({0} {1})'.format(name,age))
    
display()

display_info('kushagra',23)
        


# In[33]:


#Usecase example
def my_timer(original_func):
    import time
    
    def wrapper_func(*args, **kwargs):
        t1=time.time()
        result=original_func(*args,**kwargs)
        t2=time.time() - t1
        print('{} ran in {} sec'.format(original_func.__name__,t2))
        return result
    return wrapper_func


@my_timer
def display_info(name,age):
    import time
    time.sleep(1)
    print('display_info ran with arguments ({0} {1})'.format(name,age))

display_info('kushagra',23)


# #Summary
# @decorator
# def function():
#     pass
# is equivalent to
# function = decorator(function)

# In[46]:


#Decorators with Arguments

def prefix_decorator(prefix):
    def decorator_func(original_func):
        def wrapper_func(*args,**kwargs):
            print(prefix, 'Executed before:', original_func.__name__)
            result=original_func(*args,**kwargs)
            print(prefix, 'Executed after:', original_func.__name__)
            return result
        return wrapper_func
    return decorator_func

@prefix_decorator('LOG')
def display_info(name,age):
    print('display_info ran with arguments ({0} {1})'.format(name,age))

display_info('kushagra', 30)


# In[44]:


#for better understanding decorator
display1=prefix_decorator('LOG') #first prefic_decorator func gets executed with LOG as an argument returning decorator_func and storing as an object in display1 variable.
display2=display1(display_info) #display1 function which is decorator_func is executed with argument display_info function. original_func equals to  display_info func. and returns wrapper_func.
display2('yo',24) #wrapper func takes arguments print "executed before" and pass it to original func which is display function prints display_function and prints "executed after"


# In[45]:


#you can but you shouldn't write this way
prefix_decorator('LOG')(display_info)('yo',24)

