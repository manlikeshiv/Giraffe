import requests
import json
from bs4 import BeautifulSoup
import pymysql

html_text = requests.get('https://auctionhouselondon.co.uk/current-auction/').text

#print(html_text)

soup = BeautifulSoup(html_text,'lxml')

db = pymysql.connect(host='ls-98424ee6136eb87ef64aaea4eba59d2bce5b496c.ckypxf3s6nmb.eu-west-2.rds.amazonaws.com', user='shivroot', password="p~Gt0v-3WLsoSBXQ1", db='dbmaster')

cursor = db.cursor()

listings = soup.find_all('div',class_ = 'relative flex flex-col md:h-full w-full border-t-6 border-red transition-all duration-300 hover:shadow-post css-2sro01 e1smzzpd0')
for listing in listings:
    lotnumber = listing.find('div', class_ = 'absolute left-0 top-0 bg-red text-white text-17 md:text-19 uppercase px-25 py-6').text.replace('Â', '')
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

    desc = listing.find('p', class_ = 'text-17 lg:text-19 leading-snug')
    if desc is not None:
        desc = listing.find('p', class_='text-17 lg:text-19 leading-snug').text.replace('Â', '')

    a_tag = listing.find('a')
    link = (a_tag['href'])
    full_link = 'https://auctionhouselondon.co.uk'+f"{link}"

    html_text2 = requests.get(f'{full_link}').text
    soup2 = BeautifulSoup(html_text2, 'lxml')


    print(f'''
    Lot Number: {lotnumber}
    Address: {address}
    Description: {desc}
    Guide Price: {price}
    URL: {full_link}
    ''')



    sql = "INSERT INTO AuctionHouseData VALUES (%s, %s, %s, %s, %s)"
    values = ({lotnumber}, {address}, {price}, {desc}, {full_link})
    cursor.execute(sql, values)

    db.commit()