#!/usr/bin/env python
# coding: utf-8

# In[1]:


#First class functions: 
#If a function can be assigned to a variable or passed as object/variable to other function, that function is called as first class function
#All functions in Python are first-class functions. 
#To say that functions are first-class in a certain programming language means that they can be passed around and manipulated similarly to
#how you would pass around and manipulate other kinds of objects (like integers or strings).
#You can assign a function to a variable, pass it as an argument to another function, etc. 


# In[2]:


#Function Returning square of number
def square(x):
    return x * x


# In[7]:


f=square(5)
print(square)
print(f)


# In[8]:


#we don't wanna execute the function, we just wanna set variable f equal to function. i.e we havent use parenthesis after square while assigning value to f.
f=square
print(square)
print(f) #we can treat variable f as a function. 


# In[10]:


#now i can use variable as function and pass value to it.
print(f(5))


# In[11]:


def square(x):
    return x * x

#function taking another function and args_list as arguments.
def my_map(func,args_list):
    result=[]
    for i in args_list:
        result.append(func(i)) #square function is used to calculate square of number
    return result

squares= my_map(square,[1,2,3,4,5]) #function square is passed as an argument.

print(squares)


# In[14]:


#now if u want cube instead of square.. you just need some little changes.
def cube(x):
    return x * x * x

def my_map(func,args_list):
    result=[]
    for i in args_list:
        result.append(func(i)) 
    return result

cubes= my_map(cube,[1,2,3,4,5]) 

print(cubes)


# In[16]:


#Returning A function from another function.
def logger(msg):
    
    def log_message():
        print('Log!!', msg)
        
    return log_message

log_hi = logger('Hi')  #first logger function is executed and hi is passed as argument which return log_message and is stored in log_hi variable.
log_hi()               #now log_hi variable has log_message and as it is executed with parenthesis. it's a function log_message which is called. and print the sentence while remebering variable msg.


# In[18]:


#Another example of returning a function from another function
def html_tag(tag):
    
    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag,msg))
    return wrap_text

print_h1 = html_tag('h1')
print(print_h1)          #now print_h1 contains wrap_text function with value of tag=h1


# In[20]:


#passing value to wrap_text function
print_h1('Test Headline')
print_h1('Another Headline')


# In[21]:


print_p=html_tag('p')
print_p('Test Paragraph')

