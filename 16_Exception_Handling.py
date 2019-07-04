#!/usr/bin/env python
# coding: utf-8

# In[5]:


#As file is not present. It will raise the exception
f=open('yo.txt')


# In[4]:


#Exception Handled using try and except block, in this code we gave Exception in except block. which will handled any type of exception and print file doesn't exist. 
#But it's always better to give the exception name and print message accordingly.
try:
    f=open("yo.txt")
except Exception:
    print("Sorry the file doesn't exist")


# In[7]:


#To show you why not except every exception, i will create a file yo.txt and not set 000 permission of file.
f=open('yo.txt')
#this time it gave as PermissionError


# In[10]:


#Now when we run above try and except block
try:
    f=open("yo.txt")
except Exception:
    print("Sorry the file doesn't exist")
#It will print exact same error for every exception
#Goal of try and except is not to work around all the exception which we may run to, its to handle the exception and print accordingly.


# In[11]:


#when file is not present, exception FileNotFoundError exception handled
try:
    f=open("yo.txt")
except FileNotFoundError:
    print("Sorry the file doesn't exist")


# In[12]:


#when permission exception is raise in above code, which is a good thing
try:
    f=open("yo.txt")
except FileNotFoundError:
    print("Sorry the file doesn't exist")


# In[14]:


#you can handle as many exception as you want and print message accordingly. but always except general exception at last.
#you can also print exact exception instead of custom messages
try:
    f=open("yo.txt")
except FileNotFoundError:
    print("Sorry the file doesn't exist")
except PermissionError as e:
    print(e)
except Exception:
    print("Sorry something went wrong")


# In[16]:


#if you dont want custom message for any exception. you can always do this.
try:
    f=open("yo.txt")
except Exception as e:
    print(e)


# In[17]:


#else will execute the code if try block doesnt raise the exception
try:
    f=open("yo.txt")
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()


# In[18]:


#Regardless of what happen in try and catch block, finally block always get executed.
try:
    f=open("yo.txt")
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print("This blocks contain something thats need to be done, no matter what, like closing the DB")


# In[19]:


#Above code with exception
try:
    f=open("yo.txt")
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print("This blocks contain something thats need to be done, no matter what, like closing the DB")


# In[23]:


#TO manually raise exception
try:
    f=open("corrupte_file.txt")
    if f.name=='corrupte_file.txt':
        raise Exception
except FileNotFoundError:
    print("Sorry the file doesn't exist")
except PermissionError as e:
    print(e)
except Exception as e:
    print("File Corrupted!!!!!")

