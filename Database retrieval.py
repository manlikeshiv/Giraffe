import pymysql
import requests
import json
from bs4 import BeautifulSoup
import time
from random import randint
from time import sleep
import random




db = pymysql.connect(host='ls-98424ee6136eb87ef64aaea4eba59d2bce5b496c.ckypxf3s6nmb.eu-west-2.rds.amazonaws.com', user='shivroot', password="p~Gt0v-3WLsoSBXQ1", db='dbmaster')

cursor = db.cursor()

query="SELECT Address FROM AuctionHouseData"
cursor.execute(query)

first_row=cursor.fetchone()

records = cursor.fetchall()

for row in records:
    sleep(randint(0,3))
    sqladdress = row[0]
    post_code = (sqladdress.split(",")[-1]).strip()
    first_line_address = (sqladdress.split(",")[0]).strip()
    second_line_address = (sqladdress.split(",")[1]).strip()
    third_line_address = (sqladdress.split(",")[2]).strip()
    x = post_code.split()
    postcode = x[0]+x[1]
    print(first_line_address)
    print(postcode)

    URL = "https://find-energy-certificate.service.gov.uk/find-a-certificate/search-by-postcode"

#print(postcode)

    queryURL = URL + f"?postcode={postcode}"
#print(queryURL)

    session = requests.Session()

    cookie = {'cookie_consent': 'true'}

# Define headers to mimic a Chrome browser
    #headerss = {
    #    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    #    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    #    'Accept-Encoding': 'gzip, deflate, sdch, br',
    #    'Accept-Language': 'en-US,en;q=0.8',
    #    'Connection': 'keep-alive'
    #}

    user_agent_list = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1',
        'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363',
    ]

    headers = {"User-Agent": user_agent_list[random.randint(0, len(user_agent_list) - 1)]}

    #response = session.get(queryURL, cookies=cookie, headers=headers)
    html_text = requests.get(queryURL, cookies=cookie, headers=headers).text
    soup = BeautifulSoup(html_text,'lxml')
    addresses = soup.find_all('a', class_ = 'govuk-link')

    addresslist = []

    for address in addresses:
        addresslist.append((address.text.lower()).strip().replace(",", ""))

        # print(addresslist)
        # print(first_line_address.strip().replace(",", ""))

        occurences = sum((first_line_address.strip().replace(",", "").lower()) in s for s in addresslist)

    if occurences == 1:
        for address in addresses:
            if first_line_address.strip().replace(",", "").lower() in (address.text).strip().replace(",", "").lower():
                propertyURL = ('https://find-energy-certificate.service.gov.uk/' + address['href'])

                html_text2 = requests.get(propertyURL, cookies=cookie, headers=headers).text

                soup2 = BeautifulSoup(html_text2, 'lxml')

                propertytype = soup2.find_all('dd', class_='govuk-summary-list__value govuk-!-width-one-half')
                print('Property Type: ' + propertytype[0].text.strip())
                sqm = soup2.find_all('dd', class_='govuk-summary-list__value govuk-!-width-one-half')
                print('Total floor area: ' + sqm[1].text.strip())
                rating = soup2.find('p', class_='epc-rating-result govuk-body').text
                print('Energy rating: ' + rating.strip())


    elif occurences > 1:
        firstandsecondline = first_line_address + ' ' + second_line_address
        addresslist2 = []

        for address in addresses:
            addresslist2.append((address.text.lower()).strip().replace(",", ""))
            occurences2 = sum((firstandsecondline.strip().replace(",", "").lower()) in s for s in addresslist2)

        if occurences2 == 1:
            propertyURL = ('https://find-energy-certificate.service.gov.uk/' + address['href'])
            html_text2 = requests.get(propertyURL, cookies=cookie, headers=headers).text
            soup2 = BeautifulSoup(html_text2, 'lxml')
            propertytype = soup2.find_all('dd', class_='govuk-summary-list__value govuk-!-width-one-half')
            print('Property Type: ' + propertytype[0].text.strip())
            sqm = soup2.find_all('dd', class_='govuk-summary-list__value govuk-!-width-one-half')
            print('Total floor area: ' + sqm[1].text.strip())
            rating = soup2.find('p', class_='epc-rating-result govuk-body').text
            print('Energy rating: ' + rating.strip())


        else:
            print("Manual Intervention Required")

    elif occurences == 0:
        print("No EPC data")

    URL = "https://api.propertydata.co.uk/prices"
    key = 'RQRJZLTZLM'
    queryURL = URL + f"?key={key}&postcode={postcode}"
    response = requests.get(queryURL)
    housedata = json.loads(response.text)
    price = housedata['data']['average']
    desired_representation = "{:,}".format(price)
    print(f"PropertyData average price: £{desired_representation}\n")



