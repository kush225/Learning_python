#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Logging_Advance
#Loggers, Handlers, Formatters


# In[23]:


import logging
import subprocess


# In[3]:


logger = logging.getLogger(__name__)
#you can specify any name you want but benefit of using __name__ is that it will use the module name if the code is executed from an import else it will use __main__ when run directly.
#if the logger doesn't exist it will get created.

logging.basicConfig(filename='test.log',level=logging.DEBUG)
#this configures root
#logging works in hierarchy so if something is not configure in our logger than it will access from root
#In this case filename and level is used from root and logger name from our logger


# In[29]:


#lets setup our logger so we don't need root configuration
logger = logging.getLogger(__name__)

#setting up log level
logger.setLevel(logging.INFO)

#setting up our log file name
file_handler = logging.FileHandler('calculation.log')

#setting up our log file format
formatter= logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')

#setting up a stream handler, so that we can see debug statements at terminal and only error in error logs
stream_handler = logging.StreamHandler()

#adding formatter to handler, formatter is added to handler not logger
file_handler.setFormatter(formatter)

#note if you want formatting of stream handler same as file handler you can set like this
stream_handler.setFormatter(formatter)

#adding stream handler to our logger
logger.addHandler(stream_handler)

#suppose i want to keep my logger level to debug but only want to capture error statement and above specific filehandler, then we can do
file_handler.setLevel(logging.ERROR)

#adding our filename to logger
logger.addHandler(file_handler)


# In[25]:


def add(x,y):
    """Add Function"""
    return x + y
def subtract(x,y):
    """Subtract Function"""
    return x - y
def multiply(x,y):
    """Multiply Function"""
    return x * y
def divison(x,y):
    """Divide Function"""
    try:
        result = x / y
    except Exception:
        #logger.error('Tried to Divide by Zero') #this will just print the error when it occurs
        logger.exception('Tried to Divide by Zero') #this will print the traceback so we can know where it occured.
    else:
        return result


# In[26]:


num_1=10
num_2=0


# In[30]:


#since we are using custom logger we need to call logger.debug instead of logging.debug 
add_result= add(num_1,num_2)
logger.debug('Add: {} + {} = {}'.format(num_1,num_2,add_result))
sub_result= subtract(num_1,num_2)
logger.debug('Subtract: {} + {} = {}'.format(num_1,num_2,sub_result))
multiply_result= multiply(num_1,num_2)
logger.debug('Multiply: {} + {} = {}'.format(num_1,num_2,multiply_result))
divide_result= divison(num_1,num_2)
logger.debug('Divison: {} + {} = {}'.format(num_1,num_2,divide_result))


# In[28]:


#subprocess module is used to show data in file
subprocess.getoutput('cat calculation.log')
#imagine \n as new line.
#we can see logger name coming __main__ bcoz we ran code directly not by importing.


# In[ ]:




