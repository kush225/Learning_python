#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Requests Module
#The requests library is the de facto standard for making HTTP requests in Python. It abstracts the complexities of making requests behind a beautiful, simple API so that you can focus on interacting with services and consuming data in your application.


# In[2]:


import requests


# In[3]:


r = requests.get('https://xkcd.com/353/')
print(r) #will give the status code of response


# In[4]:


#to know about attributes and method that we can access within response object
print(dir(r))


# In[5]:


#to get information about each attribute and method we can use help
#print(help(r))


# In[6]:


#It will give content of the response in unicode
print(r.text)


# In[8]:


#URL of an image
r= requests.get('https://imgs.xkcd.com/comics/python.png')
#To download the image
with open('comic.png','wb') as f: #wb is used for image which means writebyte
    f.write(r.content)


# In[9]:


#To check status code
print(r.status_code) #200 is for success, 300 is for redirects, 400 is for client error, 500 are for server error


# In[11]:


#for anything less than 400 status code it will print True or only for client and server error it will print False
print(r.ok)


# In[12]:


#will print the response headers
print(r.headers)


# In[13]:


#dictionary of parameters to pass in url
payload={ 'page':2, 'count':25}
#httpbin is a testing website develop by developer of request module
r= requests.get('https://httpbin.org/get', params=payload)  
print(r.text)


# In[14]:


print(r.url) #request module set the url correctly so it's always better to add parameter this way than manually.


# In[15]:


#To make post request
payload={ 'username':'corey', 'password':'text'}
r= requests.post('https://httpbin.org/post', data=payload)  
print(r.text)
#we are getting json as reponse so it's better to use json method for that


# In[18]:


#It will give the json response in form of dictionary
r_dict=r.json()
print(r_dict)


# In[19]:


#To print only the form
print(r_dict['form'])


# In[20]:


#Basic Authentication

r =requests.get('https://httpbin.org/basic-auth/kushagra/12345678',auth=('kushagra',12345678))
#auth is tuple of id,password
print(r.text)


# In[21]:


print(r)  #status code 200 means success


# In[22]:


#with wrong password
r =requests.get('https://httpbin.org/basic-auth/kushagra/12345678',auth=('kushagra',123456))
print(r) #401 means authentication error


# In[32]:


#URl that will give response after 1sec
r =requests.get('https://httpbin.org/delay/1',timeout=3) #timeout means it will wait for max 3 sec to get reponse
print(r)  #as response came in lesser time than timeout hence success 


# In[38]:


#URl that will give response after 5secs
try:
    r =requests.get('https://httpbin.org/delay/5',timeout=3)
except Exception as e:
    print(e)
else:
    print(r)
#Exception is raised as timeout is lesser than response time.

