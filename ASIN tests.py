from requests_html2 import HTMLSession
import csv
import datetime
import sqlite3
import random
import requests
import json
from bs4 import BeautifulSoup
import time
import pymysql
import schedule
from os import system

asins = []

#read csv to list
with open('asins.csv', 'r') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        asins.append(row[0])

#scrape data

user_agent_list = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1',
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363',
]

headers = {"User-Agent": user_agent_list[random.randint(0, len(user_agent_list) - 1)]}


cookie = {'cookie_consent': 'true'}

for asin in asins:
    html_text = requests.get(f'https://www.amazon.co.uk/dp/{asin}', cookies=cookie, headers=headers).text
    soup = BeautifulSoup(html_text, 'lxml')

    #prices = soup.find_all('span', class_='a-price aok-align-center reinventPricePriceToPayMargin priceToPay')
    #price = prices[0].text.strip()

    #titles = soup.find_all('span', class_='a-size-large product-title-word-break')
    #title = titles[0].text.strip()

    asin = asin
    date = datetime.datetime.today()

    span = soup.find("span", id ="productTitle")
    title = span.text.strip()
    print(title)

    span1 = soup.find("span", class_="a-price-whole")
    pricepound = span1.text


    span2 = soup.find("span", class_="a-price-fraction")
    pricepence = span2.text


    price = f'{pricepound}{pricepence}'
    print(price)






