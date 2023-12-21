import requests
import json
from bs4 import BeautifulSoup

html_text = requests.get('https://auctionhouselondon.co.uk/current-auction/').text

#print(html_text)

soup = BeautifulSoup(html_text,'lxml')


listings = soup.find_all('div',class_ = 'relative flex flex-col md:h-full w-full border-t-6 border-red transition-all duration-300 hover:shadow-post css-2sro01 e1smzzpd0')
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

    desc = listing.find('p', class_ = 'text-17 lg:text-19 leading-snug')
    if desc is not None:
        desc = listing.find('p', class_='text-17 lg:text-19 leading-snug').text.replace('Â', '')

    a_tag = listing.find('a')
    link = (a_tag['href'])
    full_link = 'https://auctionhouselondon.co.uk'+f"{link}"

    html_text2 = requests.get(f'{full_link}').text
    soup2 = BeautifulSoup(html_text2, 'lxml')

    headings = soup2.find_all('h4')
    for heading in headings:
        print(heading.text)
# >> <strong>some value</strong>
''' extrainfo = soup2.find('div',class_ = 'text-17 xl:text-19 mb-15' ).text

    exterior_section = soup2.find('h4', text='Exterior').find_next_sibling('div')
    exterior_text = exterior_section.get_text(strip=True) if exterior_section else 'Exterior information not found'
'''

'''
    extrainfo = soup2.find('div',class_ = 'text-17 xl:text-19 mb-15' ).text

    exterior_section = soup2.find('h4', text='Exterior').find_next_sibling('div')
    if exterior_section is not None:
        exterior_text = exterior_section.get_text(strip=True)
    else:
        exterior_text = 'Exterior information not found

        '''