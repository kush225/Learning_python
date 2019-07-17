#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json


# In[2]:


#string containing json data
people_string = '''
{
"people":[
    {
    "name":"kushagra gupta",
    "phone":"9876543210",
    "emails":["kushagra224@gmail.com","kushagra225@gmail.com"],
    "has_license":false
    },
    {
    "name":"Jane Doe",
    "phone":"1234567890",
    "emails":null,
    "has_license":true
    }
  ]
}
'''


# In[9]:


#loading json into python
data =json.loads(people_string)
#printing json data
print(data)
#it looks like python dictionary, let's check it's type


# In[4]:


print(type(data))


# In[5]:


#that's bcz python converts the follow
#json          python
#object        dict
#array         list
#string        str
#number(int)   int
#number(real)  float
#true          True
#false         False
#null          None


#you can check the conversion in the above output statement.


# In[6]:


print(type(data['people']))


# In[7]:


for person in data['people']:
    print(person)


# In[8]:


for person in data['people']:
    print(person['name'])


# In[10]:


#Loading python data in json
#first deleting phone numbers from our data
for person in data['people']:
    del person['phone']


# In[16]:


#now dumping python data in json
new_string = json.dumps(data, indent=2, sort_keys=True)  #indent is to indent the data and sort_keys is to sort the data

#new json string without phone
print(new_string)


# In[22]:


#Loading Json file from system
with open('sample_states.json') as f:
    data = json.load(f)
for state in data['states']:
    print(state)
    print(state['name'],state['abbreviation'])


# In[19]:


#removing abbrevation from json data
for state in data['states']:
    del state['abbreviation']


# In[21]:


#saving new json object in file
with open('new_states.json','w') as f:
    json.dump(data, f,indent=2)
    
# If you want to dump the JSON into a file/socket or whatever, then you should go for dump(). If you only need it as a string (for printing, parsing or whatever) then use dumps() (dump string)


# In[ ]:


#working with real json data
import json
from urllib.request import urlopen

#API to get finance data from yahoo
with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
    source = response.read()

#print the data we get
#print(source)
 
data = json.loads(source)
usd_rates=dict()


# In[ ]:


for item in data['list']['resoureces']:
    name = item['resource']['fields']['name']
    price = item['resource']['fields']['price']
    usd_rates[name]=price
print(usd_rates['USR/EUR'])

