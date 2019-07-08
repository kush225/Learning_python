#!/usr/bin/env python
# coding: utf-8

# In[2]:


'''
LEGB
Local, Enclosing, Global, Built-in
'''
#The scopes are listed below in terms of hierarchy(highest to lowest/narrowest to broadest):

#Local(L): Defined inside function/class
#Enclosed(E): Defined inside enclosing functions(Nested function concept)
#Global(G): Defined at the uppermost level
#Built-in(B): Reserved names in Python builtin modules


# In[3]:


import builtins


# In[8]:


#Local and Global Scope
x='global x'
def test():
    y='local y'
    print(y)
    print(x)
test()
#when we print y it checks the local scope and as it was there in local scope it printed the value, same goes for x but x was not in local scope, so python checks it in first enclosing scope [which is not there] and then in global scope and print the global value.


# In[9]:


#y variable is defined inside a function so it has a local scope even we have called the function test but we can't access outside it's scope.
x='global x'
def test():
    y='local y'
    print(y)
test()
print(y)


# In[11]:


#As x variable is defined globally, we can access it from inside the function or outside the  function.
x='global x'
def test():
    y='local y'
    print(y)
test()
print(x)


# In[12]:


#you may be thinking that x variable is overwritten in the function but that's not the case.. when x is called function checks whether it exist locally, as it does it didn't need to check globally.
x='global x'
def test():
    x='local x'
    print(x)
test()
print(x)


# In[14]:


#Setting global value from inside the function
x='global x'
def test():
    global x
    x='local x'
    print(x)
test()
print(x)


# In[15]:


#you don't need x to be defined outside function to call it.
def test():
    global x
    x='local x'
    print(x)
test()
print(x)


# In[17]:


def test(z):
    #global x
    x='local x'
    print(z)
test('local z')
print(z)
#because z is local to test function.


# In[22]:


#BUILT-INS
#we are able to use min as it is a built-in function in python
m=min([5,4,2,1,3])
print(m)


# In[21]:


#dir gives attributes of given object
print(dir(builtins))


# In[23]:


#you can override the built-ins
def min():
    pass
m=min([5,4,2,1,3])
print(m)
#when we ran the min function, python found out the min function in global scope before checking the built-in scope.


# In[25]:


#Enclosing Scope
def outer():
    x = 'outer x' #local to outer function
    def inner():
        x='inner x' #local to inner function
        print(x)
    inner()
    print(x)
outer()


# In[26]:


#first inner function will check if it has any local variable, if not then it will look in enclosing scope. then in global then in builtin.. we have x variable in enclosing scope.
def outer():
    x = 'outer x' #enclosing to inner function, #local to outer
    def inner():
        #x='inner x'
        print(x)
    inner()
    print(x)
outer()


# In[27]:


def outer():
    x = 'outer x' #enclosing to inner function, #local to outer
    def inner():
        nonlocal x #this means we are affecting the enclosing variable of inner function.
        x='inner x'
        print(x)
    inner()
    print(x)
outer()


# In[28]:


x='global x'
def outer():
    #x = 'outer x' 
    def inner():
     #   x='inner x'
        print(x)
    inner()
    print(x)
outer()
print(x)

