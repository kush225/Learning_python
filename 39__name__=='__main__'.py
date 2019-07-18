#!/usr/bin/env python
# coding: utf-8

# In[9]:


#when we run python program some variables are first set up by default.
#__name__ is one of variable which is set to __main__ when run directly but if we import the module it will take the value of module name
print("Name: {}".format(__name__))


# In[10]:


#Example
import subprocess
subprocess.getoutput("cat module.py")
#we can see that module.py has same code as above statement. and now if i import it 


# In[15]:


import module
#in place of "__name__" module is there as are not running it directly we are importing it.


# In[17]:


#In python this is used alot
def main():
    print("Name: {}".format(__name__))

if __name__ == '__main__':  
#we set the condition checks whether the file is directly run by python or imported.
    main()

#we can see our print statement gets executed as we are running it directly.


# In[18]:


#this file has same code as above code block.
subprocess.getoutput("cat second_module.py")
#image \n as next line.. 


# In[19]:


#when i import this code
import second_module
#print doesn't as executed as if statement get failed.


# In[ ]:




