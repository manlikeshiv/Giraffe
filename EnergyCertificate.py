import requests
import json
from bs4 import BeautifulSoup


URL = "https://find-energy-certificate.service.gov.uk/find-a-certificate/search-by-postcode"
postcode = 'WD77BB'
theaddress = '18, Shenley Hill, RADLETT, WD7 7BB'



queryURL = URL + f"?postcode={postcode}"

session = requests.Session()

cookie = {'cookie_consent': 'true'}

# Define headers to mimic a Chrome browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch, br',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'
}

response = session.get(queryURL, cookies=cookie, headers=headers)

html_text = requests.get(queryURL, cookies=cookie, headers=headers).text


soup = BeautifulSoup(html_text,'lxml')

addresses = soup.find_all('a', class_ = 'govuk-link')


for address in addresses:
    if (address.text).strip() == theaddress.strip():
        propertyURL = ('https://find-energy-certificate.service.gov.uk/'+address['href'])

        html_text2 = requests.get(propertyURL, cookies=cookie, headers=headers).text

        soup2 = BeautifulSoup(html_text2, 'lxml')

        propertytype = soup2.find_all('dd', class_='govuk-summary-list__value govuk-!-width-one-half')
        print('Property Type: ' + propertytype[0].text.strip())
        sqm = soup2.find_all('dd', class_ = 'govuk-summary-list__value govuk-!-width-one-half')
        print('Total floor area: '+sqm[1].text.strip())
        rating = soup2.find('p', class_ = 'epc-rating-result govuk-body').text
        print('Energy rating: '+rating.strip())




