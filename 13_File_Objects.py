#!/usr/bin/env python
# coding: utf-8

# In[1]:


#File Objects
#A file object allows us to use, access and manipulate all the user accessible files. One can read and write any such files. 


# In[7]:


#not a python command.. just to show the file contents
get_ipython().system('cat test.txt')


# In[4]:


#no path is needed as file is present in same directory otherwise fullpath to file would be given, r represent file is open for reading which is default mode. so if you don't specify it will open in read mode only.
# r = read
# a = append
# w = write
# r+= read+write
f = open('test.txt','r')


# In[5]:


#It will print the name of file
print(f.name)

#It will print the mode used
print(f.mode)


# In[6]:


#Closing the file
f.close()


# In[8]:


#using Context Manager [Benefit is that it will automatically close the file so it will provide memory leak]
#read will display all the lines of file. [use in case of small files]
with open('test.txt', 'r') as f:
    f_contents = f.read()
    print(f_contents)


# In[9]:


#readlines will show lines in the form of list
with open('test.txt', 'r') as f:
    f_contents = f.readlines()
    print(f_contents)


# In[15]:


#readline will display, one line at a time and move cursor to next line and when readline is invoked again then it will print the other line.
#print by default adds a newline.. that's why end='' is used so wont't create a new line.
with open('test.txt', 'r') as f:
    f_contents = f.readline()
    print(f_contents)
    
    f_contents = f.readline()
    print(f_contents, end='')
    
    f_contents = f.readline()
    print(f_contents)
    


# In[40]:


#This is better than read as this will not read all lines at once and helps with memory consumption
with open('test.txt', 'r') as f:
    for line in f:
        print(line,end='')


# In[42]:


#you can limit the amount of data to read. by passing it in the read method. I.n this case 100 characters gets read
with open('test.txt', 'r') as f:
    f_contents = f.read(100)
    print(f_contents)
    
    f_contents = f.read(100)
    print(f_contents)


# In[47]:


#A better way to use read.
with open('test.txt', 'r') as f:
    
    size_to_read=100 #no of characters to read
    f_contents=f.read(size_to_read)
    #At every Iteration printing 100 characters
    while (len(f_contents)) > 0:
        print(f_contents,end='')
        f_contents=f.read(size_to_read)


# In[48]:


#Using * at the end, we can see this is looping again and again

with open('test.txt', 'r') as f:
    
    size_to_read=10
    f_contents=f.read(size_to_read)
    
    while (len(f_contents)) > 0:
        print(f_contents,end='*')
        f_contents=f.read(size_to_read)


# In[49]:


#tell() tells the location of pointer
with open('test.txt', 'r') as f:
    
    size_to_read=10
    f_contents=f.read(size_to_read)
    print(f.tell())


# In[58]:


#using seek() we can set the location of pointer. In this case we first print the 10 lines. set the pointer again at begin and then print the 10 lines.
with open('test.txt', 'r') as f:
    
    size_to_read=10
    
    f_contents=f.read(size_to_read)
    print(f_contents)
    
    f.seek(0)
    
    f_contents=f.read(size_to_read)
    print(f_contents)


# In[60]:


#Write Mode
#Error because we are trying to write in file using read mode
with open('test.txt', 'r') as f:
    f.write("yo")


# In[61]:


#if file2.txt doesnot exist then it will create it.
#if file2.txt exist then it will overwrite it. you will lose data of that file.
#you can open file2.txt in append mode so you don't lose data of that file.

with open('file2.txt', 'w') as f:
    pass
#this will create the file if it didn't already exist. you don't have to write anything to create a file


# In[62]:


with open('file2.txt', 'w') as f:
    f.write('Test')


# In[63]:


#file2.txt is a file containg data, shown using cat command
subprocess.getoutput("cat file2.txt")


# In[65]:


#This will also left the pointer at last position and when writing again it will begin from there only. you can use seek() here also.
with open('file2.txt', 'w') as f:
    f.write('Test')
    f.write('Test')
    
subprocess.getoutput("cat file2.txt")


# In[67]:


#first we wrote Test, then move the pointer to begin and wrote R. 
with open('file2.txt', 'w') as f:
    f.write('Test')
    f.seek(0)
    f.write('R')
    
subprocess.getoutput("cat file2.txt")


# In[68]:


#Making a copy of file using File_Objects. you can even make copy of images. but for that you need to read and write in binary mode. just add b with r and w mode.
# eg. with open('test.txt', 'rb') as rf:

with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)


# In[69]:


#Output of test_copy.txt file
subprocess.getoutput("cat test_copy.txt")


# In[70]:


#You can also make a copy using chunks of data by combining the 2 above codes
with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        
        chunk_size=4096
        rf_chunk=rf.read(chunk_size)
        
        while (len(rf_chunk)) > 0:
            
            wf.write(rf_chunk)
            rf_chunk=rf.read(chunk_size)

