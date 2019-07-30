#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Subprocess Module
#The subprocess module is used to run new applications or programs through Python code by creating new processes. It also helps to obtain the input/output/error pipes as well as the exit codes of various commands.


# In[2]:


import subprocess


# In[5]:


#it will run ls command and will print the output
subprocess.run('ls')


# In[7]:


#To use the suboptions of command you need to pass shell=True parameter also in subprocess.run
subprocess.run('ls -la',shell=True)


# In[8]:


#If you don't want to pass shell=True, you can pass it a list of arguments
subprocess.run(['ls','-la'])


# In[9]:


#this will print the command output in screen and will store CompletedProcess(args=['ls', '-la'], returncode=0)
p = subprocess.run(['ls','-la']) 


# In[10]:


#we can check arguments and return code, 0 meaning run with 0 errors
print(p.args)
print(p.returncode)


# In[27]:


#To store the standoutput and error in variable use capture_output=True
p = subprocess.run(['ls', '/home/kushagra/Desktop/udemy'],capture_output=True) 


# In[28]:


print(p)


# In[29]:


#if only want stdout without args and returncode
print(p.stdout)


# In[30]:


#we can decode this by using decode 
# it will print the output same as linux command would have done
print(p.stdout.decode())


# In[25]:


#another way is that instead of using decode we can use
p = subprocess.run(['ls','/home/kushagra/Desktop/udemy'],capture_output=True,text=True) 


# In[26]:


print(p.stdout)


# In[31]:


#To store Standard Output and not error
p = subprocess.run(['ls','/home/kushagra/Desktop/udemy'],stdout=subprocess.PIPE,text=True) 


# In[32]:


#will result as above
print(p.stdout)


# In[33]:


#we can also pipe the out to file. [can be used for logging purposes]
with open('output.txt','w') as f:
    p = subprocess.run(['ls','/home/kushagra/Desktop/udemy'],stdout=f,text=True) 


# In[34]:


#we can see that the output of the command is now saved in the file.
get_ipython().system('cat output.txt')


# In[41]:


#listing the contents of file that doesnot exist.
p = subprocess.run(['ls','-la','den'],capture_output=True,text=True) 


# In[42]:


#will give the returncode if not 0 means error
print(p.returncode)
#for checking the error
print(p.stderr)


# In[46]:


#python won't throw exception if external command fails.. if you want python to do that you can pass check=True parameter in subprocess.run
p = subprocess.run(['ls','den'],capture_output=True,check=True,text=True) 
#we can see now python throws the exception which might be useful in some case.


# In[47]:


#we can redirect out standard error to /dev/null if you don't wish to see any error message
p = subprocess.run(['ls','den'],stderr=subprocess.DEVNULL) 


# In[48]:


#we can see no error here.
print(p.stderr)


# In[53]:


#case when we want to transfer output of one command to input of another. [output redirection]
p1 = subprocess.run(['cat','yo.txt'],capture_output=True,text=True) 


# In[56]:


#contents of file
print(p1.stdout)


# In[58]:


#using the output of p1 in p2
p2= subprocess.run(['grep','-n','test'],capture_output=True,text=True,input=p1.stdout) 


# In[59]:


#printing result of grep command
print(p2.stdout)


# In[60]:


#or we can directly use this we are not going to use parsing between commands anywhere else.
p1 = subprocess.run('cat yo.txt | grep -n test',capture_output=True,text=True,shell=True) 


# In[61]:


print(p1.stdout)

