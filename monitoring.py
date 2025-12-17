#!/usr/bin/env python
# coding: utf-8

# In[4]:


import sys
import os
import requests
from bs4 import BeautifulSoup
import wikipedia
import csv
import re
import config_settings as config 
import time
import random
import pandas as pd
import smtplib
from email.message import EmailMessage

def main(url):
    HEADERS = config.HEADERS 
    df = pd.read_csv('person_id.csv')  

    response = requests.get(url, headers = HEADERS[random.randint(0,8)])
    response.raise_for_status()
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    #Удаляю ссылки на доп источникки
    for div in soup.find_all('div', class_='reflist columns'):
        div.decompose()
    #Выделяю основной тег
    content = soup.find('div', {'id': 'mw-content-text'})
    
    #Получаю элементы вложенных списков
    for li in content.find_all('li'):
        name = None
        summary = None 
        link = None     
        #Проверяю не является ли элемент вложенным списком
        if li.find(['ul'], recursive=False):
            continue
        #Извлекаю и обрабатываю строки
        else:
            #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#
            deceased_list = []
            text = li.get_text(strip=True)
            if '—' in text:
                #Отделяю имя от краткого описания и очищаю данные
                name_part = text.split('—')[0]
                name_part = name_part[:name_part.find('(')].strip()
                name = name_part.replace(',', '').split('[')[0].strip()
                #Условие для парсинга иностранных ссылок 
                if li.find('span') and 'data-interwiki-lang' in li.find('span').attrs and 'data-interwiki-article' in li.find('span').attrs:
                    #Получаю ссылку из квадратных скобок
                    link = li.find('a', class_='extiw').get('href')
                    #Язык статьи википедии
                    lang = li.find('span').get('data-interwiki-lang')
                    #Оглавление статьи
                    title = li.find('span').get('data-interwiki-article')
                    #Меняю язык
                    wikipedia.set_lang(lang)
                else:
                    link = 'https://ru.wikipedia.org'+li.find('a').get('href')
                    wikipedia.set_lang("ru")
                    title = li.find('a').get('title')
                
                #Есть ли ссылка в csv  
                if link not in df['Url'].values:
                    try:
                        summary = wikipedia.page(title).summary
                    
                    except Exception as e:
                        summary = text.split('—')[1]

                        
                    summary = re.sub(r'\[\d+\]', '', summary).strip()
                    with open('person_id.csv', 'a', newline='', encoding='utf-8-sig') as file:
                        writer = csv.DictWriter(file, fieldnames = ['Name', 'Url'])
                        writer.writerow({
                                'Name': name,
                                 'Url': link
                                                })
                if name and summary and link is not None:
                    send_mail(name, summary, link)
                else:
                    continue
    
def send_mail(name, summary, link):
    msg = EmailMessage()
    msg['Subject'] = name
    msg['From'] = config.EMAIL_ADDRESS
    msg['To'] = config.RECIPIENT
    msg.set_content(f"""{summary}
{link}""")
# Отправка
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(config.EMAIL_ADDRESS, config.EMAIL_PASSWORD)
            smtp.send_message(msg)
        print("Письмо успешно отправлено!")
    except Exception as e:
        print(f"Ошибка при отправке: {e}")
        print(name, summary, link)
    
if __name__ == "__main__":
    while True:
        for url in config.URLS:
            try:
                time.sleep(1)
                main(url)
                print(f'Просмотрена {url}')
            except Exception as e:
                time.sleep(config.BEFORE_PARSE_PAUSE)
                pass
        
        
        time.sleep(config.BEFORE_PARSE_PAUSE)           
       
          


# In[ ]:




