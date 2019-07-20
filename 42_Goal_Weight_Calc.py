#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#A calculator which will calculate weeks to reach our goal weight.


# In[1]:


import datetime


# In[2]:


current_weight = 75 #kg
goal_weight = 65    #kg
avg_kg_week = 0.6   #losing weight at rate of 0.6kg per week


# In[9]:


#Start_date having weight of 75kg
start_date = datetime.date.today()
end_date = start_date 


# In[17]:


while current_weight > goal_weight:
    #At every loop end_date is incremented by 7
    end_date += datetime.timedelta(days=7)
    #At every loop current_weight is decremented by avg weight lose per week
    current_weight -=avg_kg_week
    
print(f'Reached Goal Weight in {(end_date - start_date).days // 7} weeks on {end_date}.')

