from requests_html2 import HTMLSession
import csv
import datetime
import random
import requests
from bs4 import BeautifulSoup
import time
import pymysql
import schedule
from os import system
import smtplib
import pywhatkit as w
import pyautogui
import keyboard as k


budgets = {
    "B07PJBC9QL": 30.00,
    "B0CBSTY9N2": 20.00,
    "B01LXOWE6B": 55.00,
    "B07YNSTPN4": 30.00}

#connect to/create database

db = pymysql.connect(host='ls-98424ee6136eb87ef64aaea4eba59d2bce5b496c.ckypxf3s6nmb.eu-west-2.rds.amazonaws.com', user='shivroot', password="p~Gt0v-3WLsoSBXQ1", db='Price_Tracker')
cursor = db.cursor()


#only create the table once, then comment out or delete the line
#c.execute('''CREATE TABLE prices(date DATE, asin TEXT, price FLOAT, title TEXT)''')

#start session and create lists
s = HTMLSession()
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
    URL = f'https://www.amazon.co.uk/dp/{asin}'
    html_text = requests.get(f'https://www.amazon.co.uk/dp/{asin}', cookies=cookie, headers=headers).text
    soup = BeautifulSoup(html_text, 'lxml')

    span1 = soup.find("span", class_="a-price-whole")
    pricepound = span1.text
    span2 = soup.find("span", class_="a-price-fraction")
    pricepence = span2.text
    price = f'£{pricepound}{pricepence}'

    pricenum = f'{pricepound}{pricepence}'

    span = soup.find("span", id ="productTitle")
    title = span.text.strip()

    y = "{:.2f}".format(budgets[asin])

    #titles = soup.find_all('span', class_='a-size-large product-title-word-break')
    #title = titles[0].text.strip()

    asin = asin
    date = datetime.datetime.today()

    sql = "INSERT INTO AmazonPriceTracker VALUES (%s, %s, %s, %s)"
    values = ({date}, {asin}, {price}, {title})
    cursor.execute(sql, values)

    db.commit()
    print(f'Added data for {asin}, {price}')

    '''def notify_mail():
        SMTP_SERVER = "smtp.gmail.com"
        PORT = 587
        EMAIL_ID = "shiv.k.j@gmail.com"
        TO_EMAIL_ID = "shiv.k.j@gmail.com"
        PASSWORD = "byyd qoya epij wrvi"
        server = smtplib.SMTP(SMTP_SERVER, PORT)
        server.starttls()
        server.login(EMAIL_ID, PASSWORD)
        subject = "Price Dropped!! Should Buy Now!"
        body = "Price of the product you want has fallen. You can consider buying it now. " + URL
        msg = f"Subject: {subject}nn{body}"
        server.sendmail(EMAIL_ID, TO_EMAIL_ID, msg)
        server.quit()

    if float(pricenum) <= float(budgets[asin]):
        notify_mail()'''

    if float(pricenum) <= float(budgets[asin]):

    # Specify the phone number (with country code) and the message
        phone_number = "+447805246830"
        message = f"SHIV ALERT: {title} is now {price} vs your budget of £{y}. Buy here: {URL}"

        # Send the message instantly
        w.sendwhatmsg_instantly(phone_number, message, 13, 12, 32)
        #pyautogui.click(1050, 950)
        #time.sleep(2)
        #k.press_and_release('enter')

print('Committed new entries to database')



def job():
    system("python3 ASIN_Price_Tracker.py")

schedule.every(15).minutes.do(job)

while True:
   schedule.run_pending()
   time.sleep(1)
