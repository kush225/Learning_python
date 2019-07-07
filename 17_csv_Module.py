#!/usr/bin/env python
# coding: utf-8

# In[5]:


import csv


# In[13]:


#Sample CSV[comma seperated values]file
with open('sample.csv','r') as csv_file:
    for line in csv_file:
        print(line)


# In[14]:


#this will read the line and store it in a list
with open('sample.csv','r') as csv_file:
    csv_reader=csv.reader(csv_file)
    for line in csv_reader:
        print(line)


# In[15]:


#you can remove the header using generator
with open('sample.csv','r') as csv_file:
    csv_reader=csv.reader(csv_file)
    next(csv_file)
    for line in csv_reader:
        print(line)


# In[16]:


#To only print the email-address
with open('sample.csv','r') as csv_file:
    csv_reader=csv.reader(csv_file)
    next(csv_file)
    for line in csv_reader:
        print(line[2])


# In[17]:


#Making a copy of csv with different delimiter
with open('sample.csv','r') as csv_file:
    csv_reader=csv.reader(csv_file)
    with open('sample2.csv','w') as csv_copy:
        csv_writer=csv.writer(csv_copy,delimiter='-')
        
        for line in csv_reader:
            csv_writer.writerow(line)


# In[18]:


#Content of the file with '-' as a delimiter
with open('sample2.csv','r') as csv_file:
    for line in csv_file:
        print(line)


# In[25]:


#we can see in above output csv writer put "" around the text which already contain "-" so when we read back, it won't consider those '-' as delimiter.
#we have to specify the delimiter while reading the file if delimiter is not ','. Otherwise it will treat it as a single line
with open('sample2.csv','r') as csv_file:
    csv_reader=csv.reader(csv_file, delimiter='-')
    with open('sample3.csv','w') as csv_copy:
        csv_writer=csv.writer(csv_copy,delimiter='\t')
        
        for line in csv_reader:
            csv_writer.writerow(line)

with open('sample3.csv','r') as csv_file:
    for line in csv_file:
        print(line)


# In[26]:


#Reading csv using DictReader 
with open('sample.csv','r') as csv_file:
    csv_Dict_reader=csv.DictReader(csv_file)
    for line in csv_Dict_reader:
        print(line)


# In[27]:


#so now if someone wants email, he can simply pass email without knowing the index of that element.#
with open('sample.csv','r') as csv_file:
    csv_Dict_reader=csv.DictReader(csv_file)
    for line in csv_Dict_reader:
        print(line['email'])


# In[34]:


#Writing using DictWriter
with open('sample.csv','r') as csv_file:
    csv_reader=csv.DictReader(csv_file)
    with open('sample4.csv','w') as csv_copy:
        field_names=['first_name', 'last_name','email']
        csv_Dict_Writer=csv.DictWriter(csv_copy,fieldnames=field_names,delimiter=';')
        
        #function used to write header
        csv_Dict_Writer.writeheader()
        
        for line in csv_reader:
            csv_Dict_Writer.writerow(line)


# In[35]:


#Contents of new csv
with open('sample4.csv','r') as file:
    for line in file:
        print(line)


# In[36]:


#writing only first_name and last_name
with open('sample.csv','r') as csv_file:
    csv_reader=csv.DictReader(csv_file)
    with open('sample5.csv','w') as csv_copy:
        field_names=['first_name', 'last_name']
        csv_Dict_Writer=csv.DictWriter(csv_copy,fieldnames=field_names,delimiter=';')
        
        #function used to write header
        csv_Dict_Writer.writeheader()
        
        for line in csv_reader:
            del line['email']
            csv_Dict_Writer.writerow(line)
            
with open('sample5.csv','r') as file:
    for line in file:
        print(line)

