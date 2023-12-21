import requests
import json
from bs4 import BeautifulSoup
import pymysql


html_text = requests.get('https://auctionhouselondon.co.uk/current-auction/').text

print(html_text)

soup = BeautifulSoup(html_text,'lxml')

listings = soup.find_all('div',class_ = 'pt-23 px-10 flex justify-between pb-10')
for listing in listings:
    address = listing.find('h3', class_ = 'text-17 lg:text-19 leading-snug font-semibold')
    price = listing.find('p', class_ = 'pl-20 text-19 lg:text-23 text-red font-semibold')
    desc = listing.find('p', class_ = 'text-17 lg:text-19 leading-snug')

print(f'''
Address: {address}
Description: {desc}
Guide Price: {price}
''')