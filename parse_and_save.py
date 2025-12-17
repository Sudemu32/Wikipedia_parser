#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
from bs4 import BeautifulSoup
import wikipedia
import csv
import re
import config_settings as config 
import time
import random

def parse_write(URLS):
    print(URLS)
    for url in URLS:
        HEADERS = config.HEADERS 
        response = requests.get(url, headers = HEADERS[random.randint(0,8)])
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        for div in soup.find_all('div', class_='reflist columns'):
            div.decompose()
        content = soup.find('div', {'id': 'mw-content-text'})
        
            
        for li in content.find_all('li'):
            if li.find(['ul'], recursive=False):
                continue
            else:
                deceased_list = []
                text = li.get_text(strip=True)
                if '—' in text:
                    name_part = text.split('—')[0]
                    name_part = name_part[:name_part.find('(')].strip()
                    name = name_part.replace(',', '').split('[')[0].strip()
                    print(name) 
                    if li.find('span') and 'data-interwiki-lang' in li.find('span').attrs and 'data-interwiki-article' in li.find('span').attrs:
                        link = li.find('a', class_='extiw').get('href')       
                    else:
                        link = 'https://ru.wikipedia.org'+li.find('a').get('href')
                    print(link) 
                    deceased_list=[{"Name" : name, "Url" : link}]
            
                    writer.writerow({
                                    'Name': deceased_list[0]['Name'],
                                     'Url': deceased_list[0]['Url']
                                                    })
                    
if __name__ == "__main__":
    with open('person_id.csv', 'w', newline='', encoding='utf-8-sig') as file:
        writer = csv.DictWriter(file, fieldnames = ['Name', 'Url'])
        writer.writeheader()
        parse_write((config.URLS))


# In[ ]:


как постояннно по

