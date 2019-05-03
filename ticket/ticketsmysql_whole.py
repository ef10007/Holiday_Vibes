import datetime
import json
import pymysql
import os
import requests
from bs4 import BeautifulSoup
import re
from pprint import pprint
import random

import flight_ticket as ft


def get_conn():
    return pymysql.connect(
    host=os.getenv('mysql_host'),
    user=os.getenv('mysql_user'),
    password=os.getenv('mysql_pw'),
    port=3306,
    db='projectdb',
    charset='utf8')

sql_select = 'select * from Temp1'

conn = get_conn()
    
cur = conn.cursor()
cur.execute(sql_select)
rows = cur.fetchall()

countrynames = []
countrynames_tocompare = []

for row in rows:
    country = row[1]
    city = row[2]

    countrynames_tocompare.append(country)

    countrynames.append((country, city))

# pprint(countrynames)


with open('Ticketprice.json', 'r') as jsonfile:
    data = json.loads(jsonfile.read())

dprice = ''
idprice = ''

lst = []

for i in data['PlacePrices']:
    
    setdata = i
    setname = i['Name']

    if setname not in countrynames_tocompare:
        continue

    keylist = setdata.keys()

    if 'DirectPrice' in keylist:
        price = setdata['DirectPrice']

        if price == 0:
            dprice = random.randint(500, 1100)
            continue
        
        else:
            dprice = price

        direct = (setname, dprice)

        lst.append(direct)

    elif 'IndirectPrice' in keylist:

        price = setdata['IndirectPrice']
    
        if price == 0:
            idprice = random.randint(500, 1400)
            continue

        else:
            idprice = price

        indirect = (setname, idprice)

        lst.append(indirect)

pprint(lst)








