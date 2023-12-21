import requests
import json
from bs4 import BeautifulSoup


html_text = requests.get('https://auctionhouselondon.co.uk/current-auction/').text

#print(html_text)

soup = BeautifulSoup(html_text,'lxml')

listings = soup.find_all('a',class_ = 'relative flex flex-col h-full w-full')
for listing in listings:
    address = listing.find('h3', class_ = 'text-17 lg:text-19 leading-snug font-bold')
    if address is None:
        address = listing.find('h3', class_ = 'text-17 lg:text-19 leading-snug font-semibold').text.replace('Â', '')
    else:
        address = listing.find('h3', class_='text-17 lg:text-19 leading-snug font-bold').text.replace('Â', '')
    price = listing.find('p', class_='pl-20 text-19 lg:text-23 text-red font-semibold')
    if price is None:
        price = listing.find('p', class_='pl-20 text-18 leading-snug text-red font-semibold').text.replace('*Â','').replace('*', '')
    else:
        price =  listing.find('p', class_ = 'pl-20 text-19 lg:text-23 text-red font-semibold').text.replace('*Â','').replace('+','')

    print(f'''
Address: {address}
Price: {price}
''')