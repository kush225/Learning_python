#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#SQLite [Case Sensitive]
#SQLite is a C library that provides a lightweight disk-based database that doesn't require a separate server process and allows accessing the database using a nonstandard variant of the SQL query language. Usually your SQL operations will need to use values from Python variables.
#DATATYPES
#1.NULL - for null values
#2.INTEGER - for integer values 
#3.REAL - for floating values
#4.TEXT -for text strings 
#5.BLOB - stores exactly as it was input


# In[5]:


#A sample class employee
get_ipython().system('cat employee.py')


# In[31]:


import sqlite3
conn = sqlite3.connect('employee2.db') #connecting to db resides in file employee.db
#or for testing we can use
#conn = sqlite3.connect(':memory:') #connecting to db which resides in ram
#this should create a file employee.db in current directory


# In[32]:


#we can see file is created
get_ipython().system('ls employee2.db')


# In[33]:


c = conn.cursor() #this will create a cursor and now we can run sql commands

c.execute("""CREATE TABLE employee (
            first text,
            last text,
            pay integer
            )""")


# In[18]:


#this commits the current transaction
conn.commit()
#our employee table is created, lets add data to it


# In[37]:


#Inserting data into DB
c.execute("INSERT INTO employee VALUES ('Sam','Williams',40000)")
conn.commit()
c.execute("INSERT INTO employee VALUES ('Sam','Smith',40000)")
c.execute("INSERT INTO employee VALUES ('Sam','James',40000)")
#c.fetchone() #will get the next row in our results and only return that row, null if no more row available.
#c.fetchmany(5) #will return 5 number of row as a list, if no more rows returns empty list
#c.fetchall() #will return remaining rows as a list, if no more rows returns empty list


# In[39]:


#c.fetchone() #will get the next row in our results and only return that row, null if no more row available.
#c.fetchmany(5) #will return 5 number of row as a list, if no more rows returns empty list
#c.fetchall() #will return remaining rows as a list, if no more rows returns empty list
c.execute("SELECT * FROM employee WHERE first='Sam'")

print(c.fetchone())
print()
print(c.fetchall())
#some entries are runned twice ie they are showing multiple times


# In[40]:


#importing Employee class from employee.py which was shown above
from employee import Employee

#making instance of class
emp_1 = Employee('John', 'Doe', 80000)
emp_2 = Employee('James', 'Damen', 80000)

print(emp_1.first)
print(emp_1.last)
print(emp_1.pay)


# In[41]:


#Inserting Python objects to DB

#you may be tempting to use this way of inserting but you shouldn't as anyone can do sqlinjection on this
#c.execute("INSERT INTO employee VALUES ('{}','{}',{})".format(emp_1.first,emp_1.last,emp_1.pay))

#Correct way #1
#in this we are passing tuple of objects
c.execute("INSERT INTO employee VALUES (?,?,?)",(emp_1.first,emp_1.last,emp_1.pay))

#Correct way #2
#in this we are passing dictionary of objects
c.execute("INSERT INTO employee VALUES (:first,:last,:pay)",{'first':emp_2.first,'last':emp_2.last,'pay':emp_2.pay})


# In[46]:


#we need to pass a tuple and for single value tuple we need to pass "," with it
#1
c.execute("SELECT * FROM employee WHERE first=?",('Sam',))
print(c.fetchall())
#2 Better way
c.execute("SELECT * FROM employee WHERE last=:last",{'last':'Doe'})
print(c.fetchall())


# In[64]:


#Using Function to make SQL Operation Pythonic

import sqlite3
from employee import Employee

conn = sqlite3.connect(':memory:')
c = conn.cursor()

c.execute("""CREATE TABLE employee (
            first text,
            last text,
            pay integer
            )""")

def insert_emp(emp):
    with conn:  #context manager
        c.execute("INSERT INTO employee VALUES (:first,:last,:pay)",{'first':emp.first,'last':emp.last,'pay':emp.pay})
        #will insert for any employee that is passed

def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employee WHERE last=:last",{'last':lastname})
    return c.fetchall()

def update_pay(emp,pay):
    with conn:  #context manager
        c.execute("""UPDATE employee SET pay = :pay
                   WHERE first = :first and last = :last""",
                 {'first':emp.first,'last':emp.last,'pay':pay})
    
def remove_emp(emp):
    with conn:  #context manager
        c.execute("DELETE from employee WHERE first =:first and last =:last",
                  {'first':emp.first,'last':emp.last})
        
#in some function we are using context manager as we are altering db so to auto commit our transaction and also for rollover in case of failure.

emp_1 = Employee('John', 'Doe',80000)
emp_2 = Employee('Jane','Doe',50000)


# In[66]:


#Inserting employee using our function
insert_emp(emp_1)
insert_emp(emp_2)


# In[67]:


#printing those employees whose last is Doe
emps = get_emps_by_name('Doe')
print(emps)


# In[68]:


#Update pay of one of our employee
update_pay(emp_2,100000)
#remove employee 1
remove_emp(emp_1)


# In[70]:


#rerunning above print statement
emps = get_emps_by_name('Doe')
print(emps)
#now employee2 pay has updated and employee 1 is deleted.


# In[71]:


#good practice to close the connection
conn.close()

