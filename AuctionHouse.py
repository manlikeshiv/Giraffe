import requests
import json
from bs4 import BeautifulSoup


html_text = requests.get('https://auctionhouselondon.co.uk/current-auction/').text

#print(html_text)

soup = BeautifulSoup(html_text,'lxml')

listings = soup.find_all('a',class_ = 'relative flex flex-col h-full w-full')
for listing in listings:
    address = listing.find('h3', class_ = 'text-17 lg:text-19 leading-snug font-bold')
    if address is not None:
        address = listing.find('h3', class_='text-17 lg:text-19 leading-snug font-bold').text.replace('Â', '').replace(',','')
    price = listing.find('p', class_ = 'pl-20 text-19 lg:text-23 text-red font-semibold')
    if price is not None:
        price =  price = listing.find('p', class_ = 'pl-20 text-19 lg:text-23 text-red font-semibold').text.replace('*Â','').replace(',','')
    desc = listing.find('p', class_ = 'text-17 lg:text-19 leading-snug')
    if desc is not None:
        desc = listing.find('p', class_='text-17 lg:text-19 leading-snug').text

    print(f'''
Address: {address}
Description: {desc}
Guide Price: {price}
''')

