#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Web Scraping
#To install this module run "pip install requests-html"
#Using this module you can also scrape dynamic generated data 


# In[4]:


from requests_html import HTML


# In[22]:


with open('simple2.html') as html_file:
    source = html_file.read()
    html = HTML(html=source)
    
print(html.html)


# In[23]:


match =html.find('title') 
#[0] is used to print the first element of the list
print(match[0])
print(match[0].text)
print(match[0].html)


# In[24]:


#or if you only want first, you can do like this
match =html.find('title', first=True) 
#[0] is used to print the first element of the list
print(match)
print(match.text)
print(match.html)


# In[25]:


#To search any div id you can use this method
match =html.find('#footer', first=True)
print(match.text)


# In[29]:


article = html.find('div.article', first=True)
headline = article.find('h2',first=True)
summary = article.find('p',first=True)


# In[32]:


print(headline.text)
print(summary.text)


# In[44]:


#To find all the headline and summary
articles = html.find('div.article')

for article in articles:
    headline = article.find('h2',first=True)
    summary = article.find('p',first=True)
    print(headline.text)
    print(summary.text)
    print()


# In[45]:


#Webscraping
from requests_html import HTML, HTMLSession


# In[53]:


session = HTMLSession()
r = session.get('https://coreyms.com')  #response object using request library
print(r.html)


# In[83]:


article = r.html.find('article',first=True)
headline = article.find('.entry-title-link',first=True)
paragraph =article.find('.entry-content p',first=True)
video_src = article.find('iframe',first=True)
print(headline.text)
print()
print(paragraph.text)
print()
print(video_src)
print()
print(video_src.attrs) #to get attributes


# In[90]:


#splitting the url to get video id
vid_id =video_src.attrs['src']
print(vid_id)
vid_id=video_src.attrs['src'].split('/')
print(vid_id[4])
vid_id= vid_id[4].split('?')[0]
print(vid_id)


# In[91]:


video_link = f'https://youtube.com/watch?v={vid_id}'
print(video_link)


# In[98]:


#To get title, summary, video links from all the article
articles = r.html.find('article')
for article in articles:
    headline = article.find('.entry-title-link',first=True)
    paragraph =article.find('.entry-content p',first=True)
    vid_id = article.find('iframe',first=True).attrs['src'].split('/')[4].split('?')[0]
    video_link = f'https://youtube.com/watch?v={vid_id}'
    print(headline.text)
    print(paragraph.text)
    print(video_link)
    print()
    


# In[99]:


#writing data to csv file
import csv
with open('site.csv','w') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['headline','summary','video'])
    articles = r.html.find('article')
    for article in articles:
        headline = article.find('.entry-title-link',first=True)
        paragraph =article.find('.entry-content p',first=True)
        vid_id = article.find('iframe',first=True).attrs['src'].split('/')[4].split('?')[0]
        video_link = f'https://youtube.com/watch?v={vid_id}'
        csv_writer.writerow([headline.text,paragraph.text,video_link])


# In[101]:


#To get all the links from a website, requests_html has a very simple method
session = HTMLSession()
r = session.get('https://coreyms.com') 
#print(r.html.links)
#if you want absolute path of links
#print(r.html.absolute_links)


# In[105]:


#running javascript
from requests_html import HTML, HTMLSession
with open('simple2.html') as html_file:
    source = html_file.read()
    html = HTML(html=source)
    html.render()
match = html.find('#footer',first=True)
print(match.html)

