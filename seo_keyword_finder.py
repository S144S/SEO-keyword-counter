# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 10:38:12 2021

@author: Saeed Hosseini <saeed144.73@gmail.com>

https://ariopulse.com
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

urls = []
keywords = []
cnt = []
domains=[]
column = ['URL/KEYS']
url = ''
keyword = ''

# Cleans text (removes any punctuation)
def clean_word(word):
    word = str(word)
    forbidden = [r'\n', r'.', r'?', r'!', r'(', r')']
    for i in forbidden:
        word.replace(i, '')
    return word

# returns count of a word from a page
def count_word(url, word):
    r = requests.get(url, allow_redirects=False)
    print(r.status_code)
    soup = BeautifulSoup(r.content, 'lxml')
    words = ''.join([t for t in soup.body.find_all(text=True)])
    words = clean_word(words.lower())
    words = words.split()
    return words.count(word.lower())


while(url != 'end'):
    url=input()
    if(url != 'end'):
        urls.append(url)

while(keyword != 'end'):
    keyword=input()
    if(keyword != 'end'):
        keywords.append(keyword)

for address in urls:
    domains.append(urlparse(address).netloc)

number_of_keywords = len(keywords)
number_of_urls = len(urls)
column = column + keywords

print(domains)
print(column)
print('----------------------------------------')
print('----------------------------------------')
counter = []
holder = []
data = []
for i in range(number_of_urls):
    holder.append(domains[i])
    for j in range(number_of_keywords):
        holder.append(count_word(urls[i], keywords[j]))
    j = 0
    data.append(tuple(holder))
    print("data = ")
    print(data)
    counter = []
    holder = []
i =  0
print('----------------------------------------')
##for i in range(number_of_urls):
##    data = [domains[i], cnt[0:number_of_keywords]]
##    for j in range(number_of_keywords):
##        data = [domains[i], cnt[0+j], cnt[1+j], cnt[2+j]]
##        print("data = ")
##        print(data)
# students = [('Jack', 34, 'Sydeny', 'Australia'),
#             ('Riti', 30, 'Delhi', 'India'),
#             ('Vikas', 31, 'Mumbai', 'India'),
#             ('Neelu', 32, 'Bangalore', 'India'),
#             ('John', 16, 'New York', 'US'),
#             ('Mike', 17, 'las vegas', 'US')]

table = pd.DataFrame(data, columns=column, index=None)
print(table)

table.to_excel(r'C:\Users\lenovo\Desktop\temp.xlsx', index = False)


