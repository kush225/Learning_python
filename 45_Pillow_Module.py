#!/usr/bin/env python
# coding: utf-8

# In[10]:


from PIL import Image
#module to show image in my jupyter notebook
from IPython.display import Image as jtImage 


# In[11]:


image1 = Image.open('golden.jpeg')
#this will show image in your system
#image1.show()
#but for jupyter notebook i need to use
jtImage(filename='golden.jpeg')


# In[12]:


#saving the image using pillow, you can convert format of images
image1.save('pup.jpg')


# In[14]:


jtImage(filename='pup.jpg')


# In[24]:


#for converting multiple files at once
import os
for f in os.listdir('.'):
    if f.endswith('.jpg'):
        i = Image.open(f)
        f_name, f_ext = os.path.splitext(f)
        i.save('pngs/{}.png'.format(f_name))

#files in pngs folder
print(os.listdir('pngs'))


# In[30]:


#Resizing
#making 100pixel image using tuple
size_100 = (100,100)
image1 = Image.open('golden.jpeg')
#this will resize it
image1.thumbnail(size_100)
image1.save('puppy_100.jpg')

jtImage(filename='puppy_100.jpg')


# In[31]:


#rotating image
image1 = Image.open('golden.jpeg')
image1.rotate(90).save('golden90.jpg')

jtImage(filename='golden90.jpg')


# In[32]:


#Converting to black-white
image1 = Image.open('golden.jpeg')
image1.convert(mode="L").save('golden90.jpg')

jtImage(filename='golden90.jpg')


# In[33]:


#Blur image
from PIL import ImageFilter #need for blurring

image1 = Image.open('golden.jpeg')
image1.filter(ImageFilter.GaussianBlur()).save('golden90.jpg')

jtImage(filename='golden90.jpg')


# In[36]:


image1 = Image.open('golden.jpeg')
#increasing radius of blur, default is 2
image1.filter(ImageFilter.GaussianBlur(5)).save('golden90.jpg')

jtImage(filename='golden90.jpg')

