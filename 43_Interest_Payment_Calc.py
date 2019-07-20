#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#A Calculator which will calculate amount left to pay of an EMI and Total Cost of Product with interest..


# In[1]:


import datetime
import calendar


# In[60]:


#Amount to be paid
balance = 26999
cost_of_product = balance
#Interest rate on that amount
interest_rate = 13 * .01
#(EMI) Equal Monthly Installment
monthly_payment = 3165


# In[61]:


#Purchase date of product, assuming we purchased it today
today = datetime.date.today() #today is 20july
#calendar.monthrange will return tuple of day of 1st of the month and number of days in month when year and month is passed in it.[works on leap year too]
days_in_current_month = calendar.monthrange(today.year, today.month)[1]
print(days_in_current_month) #this will be 31 as it is july
days_till_end_month = days_in_current_month - today.day
print(days_till_end_month)   #days left till next month


# In[62]:


#Assuming money is debited at every 1st of month
start_date = today + datetime.timedelta(days=days_till_end_month + 1) #1st of the next month, in my case 1st august
print(start_date) 
end_date = start_date


# In[63]:


print("Date\t\t Amount-Left")
interest_sum=0
while balance > 0:
    #on first iteration it will calculate the amount for the current month of purchase
    #to make interest rate monthly we have divided it by 12
    interest_charge = (interest_rate / 12) * balance
    interest_sum +=interest_charge
    balance += interest_charge  #same as balance = balance + interest_charge
    balance -= monthly_payment
    balance = round(balance, 2)
    if balance < 0:
        balance = 0
    
    #above 3 lines using ternary operator
    # balance = 0 if balance < 0 else round(balance, 2)   
    #print the date with amount left 
    print(end_date,"\t", balance)
    
    #number of dates in next iterated month
    days_in_current_month = calendar.monthrange(end_date.year, end_date.month)[1]
    #next date of payment
    end_date = end_date + datetime.timedelta(days=days_in_current_month)

print("Total Interest: ",interest_sum)
print("Total Cost of Product: ",cost_of_product+interest_sum)

