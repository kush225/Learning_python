#!/usr/bin/env python
# coding: utf-8

# In[1]:


#BeautifulSoup
#Beautiful Soup is a library that makes it easy to scrape information from web pages.
#Website Scrapping - Parsing the content from website, pulling the information you want
#Install these modules using pip beautifulsoup4,request,lxml,request.


# In[ ]:


with open('simple.html') as html_file:
    soup= BeautifulSoup(html_file,'lxml') #lxml is parser.


# In[25]:


match = soup.title    #prints the whole title like this "<title>Python Tutorial</title>"
match = soup.title.text #use when only want the text between tags
print(match)


# In[23]:


match = soup.div
print(match)  #will print the first div in page


# In[24]:


match = soup.find('div',class_='footer')  #can used to find particular div
print(match)


# In[28]:


article = soup.find('div',class_='article')
print(article)


# In[35]:


headline=article.h2.a.text
#will grab h2 from our article which was scrapped above. and from it only grap text data of tag a 
print(headline)


# In[36]:


summary= article.p.text
print(summary)


# In[37]:


#To get the information from all the articles
for article in soup.find_all('div',class_='article'):
    headline=article.h2.a.text
    print(headline)
    summary= article.p.text
    print(summary)
    print()


# In[38]:


#Now working with actual website, we will print heading, summary and video links from the website
from bs4 import BeautifulSoup
import requests


# In[124]:


source = requests.get('http://coreyms.com').text #using requests module we will get text data from webpage.
soup = BeautifulSoup(source, 'lxml')
print(soup.prettify())


# In[126]:


article = soup.find('article')
print(article.prettify())


# In[127]:


headline =article.h2.text
print(headline)


# In[128]:


summary=article.find('div',class_='entry-content').p.text
print(summary)


# In[129]:


p_tags = article.find('div',class_='entry-content').find_all('p') #find all the p tags in div_class
print(p_tags)
print()
link=p_tags[1].text.split('/') #split the 2nd p tag with ('/') from list
print(link)
link_data= link[-1] #graps the last link item
print()
video_link=f'https://youtube.com/watch?v={link_data}' #make your know link from link data
print(video_link)


# In[134]:


source = requests.get('http://coreyms.com').text
soup = BeautifulSoup(source, 'lxml')
#print(soup.prettify())
#article = soup.find('article')
#print(article.prettify())

for article in soup.find_all('article'):
    headline =article.h2.text
    print("heading: ",headline)
    print()
    
    summary=article.find('div',class_='entry-content').p.text
    print("summary: ",summary)
    print()
    
    p_tags = article.find('div',class_='entry-content').find_all('p')
    try: 
        link=p_tags[1].text.split('/')
    except Exception as e:
        break
    else: link_data= link[-1]
    video_link=f'https://youtube.com/watch?v={link_data}' 
    print("link: ", video_link)
    print()
    print()


# In[ ]:




