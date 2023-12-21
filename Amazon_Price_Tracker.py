import requests
from bs4 import BeautifulSoup
from lxml import etree as et
import time
import random
import csv

import schedule
import time
from os import system

def job():
    system("python3 Amazon_Price_Tracker.py")

schedule.every(5).seconds.do(job)

while True:
   schedule.run_pending()
   time.sleep(1)


user_agent_list = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1',
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363',
]

headers = {"User-Agent": user_agent_list[random.randint(0, len(user_agent_list) - 1)]}

bucket_list = ['https://www.amazon.co.uk/Hibiki-Japanese-Harmony-Suntory-Whisky/dp/B012DC0OHQ/',
               'https://www.amazon.co.uk/Jura-Whisky-Year-Single-Glasses/dp/B07PJBC9QL/'
               ]

cookie = {'cookie_consent': 'true'}

for item in bucket_list:
    html_text = requests.get(bucket_list[1], cookies=cookie, headers=headers).text
    soup = BeautifulSoup(html_text, 'lxml')
    price = soup.find_all('span', class_='a-price aok-align-center reinventPricePriceToPayMargin priceToPay')
    print('Price ' + price[0].text.strip())
    amazonprice = price[0].text.strip()

with open('profiles1.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(amazonprice)


