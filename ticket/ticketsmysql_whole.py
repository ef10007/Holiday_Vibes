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

for row in rows:
    country = row[1]
    city = row[2]

    countrynames.append((country, city))

# pprint(countrynames)

with open('Ticketprice.json', 'r') as jsonfile:
    data = json.loads(jsonfile.read())

dprice = ''
idprice = ''
countrynames = countrynames

length = len(data['PlacePrices'])

lst = []

pprint(countrynames)

for i in range(1, length):
    
    setdata = data['PlacePrices'][i]
    setname = setdata['Name']


    if setname in countrynames:

        print(setname)


    keylist = setdata.keys()


#     if 'DirectPrice' in keylist:

#         price = data['DirectPrice']

#         if price == 0:
#             dprice = random.randint(500, 1100)

#             continue
        
#         else:
#             dprice = price

#         direct = (countrynames, dprice)


#         lst.append(direct)


#     elif 'IndirectPrice' in keylist:

#         price = data['IndirectPrice']
    
#         if price == 0:
            
#             idprice = random.randint(500, 1400)

#             continue

#         else:
#             idprice = price

#             indirect = (countrynames, idprice)

#         lst.append(indirect)

# pprint(lst)



exit()


def ticket(countryname, cityname, price_sample):
    
    today = datetime.datetime.now()

    i = 0
    datelst = []
    ticketlst = []

    while(i < 300):

        today = today + datetime.timedelta(days=1)
        day = today.strftime("%Y-%m-%d")
        datelst.append(day)
        i += 1

    for i in range(len(datelst)):

        price = random.randint((price_sample[1] - 200), (price_sample[1] + 200))

        tupledata = (countryname, cityname, price, datelst[i])

        print(tupledata)
        
        ticketlst.append(tupledata)

    sql_insert = "insert into Ticket(countryname, cityname, price, dt) values(%s, %s, %s, %s)"

    conn = get_conn()
    with conn:
                        
        cur = conn.cursor()
        cur.executemany(sql_insert, ticketlst)

    print('---- Success to create ticket prices for {}!! ----'.format(cityname))

for c in countrynames:
    print(c)







