#!/usr/bin/env python
# coding: utf-8

# In[1]:


#BeautifulSoup
#Beautiful Soup is a library that makes it easy to scrape information from web pages.
#Website Scrapping - Parsing the content from website, pulling the information you want
#Install these modules using pip beautifulsoup4,request,lxml,request.


# In[9]:


from bs4 import BeautifulSoup 
with open('simple.html') as html_file:
    soup= BeautifulSoup(html_file,'lxml') #lxml is parser.


# In[7]:


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


# In[11]:


#Now working with actual website, we will print heading, summary and video links from the website
from bs4 import BeautifulSoup
import requests


# In[12]:


source = requests.get('http://coreyms.com').text #using requests module we will get text data from webpage.
soup = BeautifulSoup(source, 'lxml')
print(soup.prettify())


# In[15]:


article = soup.find('article')
print(article.prettify())


# In[16]:


headline =article.h2.text
print(headline)


# In[17]:


summary=article.find('div',class_='entry-content').p.text
print(summary)


# In[29]:


p_tags = article.find('div',class_='entry-content').find_all('p') #find all the p tags in div_class
print(p_tags)
print()

iframe = article.find('iframe')
print(iframe)
src_iframe = iframe['src']
print(src_iframe)
vid_id=src_iframe.split("/")[4].split("?")[0]
print(vid_id)
youtube_link = f'https://youtube.com/watch?v={vid_id}'
print(youtube_link)


# In[30]:


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
    
    vid_id = article.find('iframe')['src'].split("/")[4].split("?")[0]
    youtube_link = f'https://youtube.com/watch?v={vid_id}'
    print(youtube_link)
    
    print()
    print()


# In[ ]:




