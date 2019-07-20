#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#datetime module
#Python has a module named datetime to work with dates and times.


# In[1]:


import datetime


# In[2]:


#Working with Dates
d=datetime.date(2017,4,3)
print(d)


# In[3]:


#today will print today's date
tday=datetime.date.today()
print(tday)


# In[13]:


#can print only day,month,year
print(tday.day)


# In[10]:


#for weekday monday is 0 and sunday is 6
print(tday.weekday())


# In[11]:


#for isoweekday monday is 1 and sunday is 7
print(tday.isoweekday())


# In[16]:


#Time Deltas=Difference Between two Dates of time
t_delta=datetime.timedelta(days=7)


# In[17]:


#Date After 7days
print(tday+t_delta)


# In[22]:


#date2= date1 + timedelta
#timedelta = date2 -date1

#Days remaining in my Birthday
my_birthday=datetime.date(2020,1,2)
tday=datetime.date.today()
till_bday=my_birthday-tday
print(till_bday.days)

#you can do a countdown
print(till_bday.total_seconds())


# In[23]:


#Working with Time
t = datetime.time(9,30,45,10000)
print(t)


# In[25]:


#Working with DateTime
dt = datetime.datetime(2017,3,4, 1,0,0,100000)
print(dt)


# In[26]:


#Still grab only date
print(dt.date())

#or only time
print(dt.time())


# In[29]:


#Time remaining in my Birthday
my_birthday=datetime.datetime(2020,1,2,12,0,0)
tday=datetime.datetime.today()
till_bday=my_birthday-tday
print(till_bday)


# In[30]:


dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()


# In[31]:


#Returns Current local datetime with timezone of none
print(dt_today)


# In[32]:


#now() gives a option to pass timezone, if you leave it empty it works as today()
print(dt_now)


# In[34]:


#for using timezones
import pytz


# In[35]:


dt = datetime.datetime(2016,7,27,12,30,45, tzinfo=pytz.UTC)
print(dt)


# In[59]:


#Getting current Time in UTC timezone
dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow)


# In[60]:


#Converting UTC time to particular timezone
dt_mtn= dt_utcnow.astimezone(pytz.timezone('Asia/Kolkata'))


# In[61]:


print(dt_mtn)


# In[62]:


#PRINTING ALL TIMEZONES
my_list=[]
for tz in pytz.all_timezones:
    my_list.append(tz)
print(my_list)


# In[63]:


#Local time without timezone awareness or naive datetime
dt_mtn=datetime.datetime.now()
print(dt_mtn)


# In[64]:


#Assigning Timezone to naive datetime
mtn_tz=pytz.timezone('US/Mountain')
dt_mtn_aware=mtn_tz.localize(dt_mtn)
print(dt_mtn_aware)


# In[65]:


#Converting timezones
dt_east=dt_mtn.astimezone(pytz.timezone('US/Eastern'))
print(dt_east)


# In[69]:


#Converting String to DateTime
dt_str = 'July 26, 2016'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)


# In[70]:


#Coverting Datetime ot String
dt_mtn=datetime.datetime.now()
dt= dt_mtn.strftime('%B %d, %Y')
print(dt)


# In[71]:


#strftime= Datetime to String
#strptime= String to Datetime

