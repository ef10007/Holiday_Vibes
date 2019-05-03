import datetime
import json
import pymysql
import os
import requests
from bs4 import BeautifulSoup
import re
from pprint import pprint
import random


def get_conn():
    return pymysql.connect(
    host=os.getenv('mysql_host'),
    user=os.getenv('mysql_user'),
    password=os.getenv('mysql_pw'),
    port=3306,
    db='projectdb',
    charset='utf8')

thprice_sample = ('Thailand', 147)
sgprice_sample =  ('Singapore', 298)
hkprice_sample =  ('Hong Kong', 114)
caprice_sample =  ('Canada', 499)
usprice_sample =  ('United States', 430)
auprice_sample =  ('Australia', 619)
cnprice_sample =  ('China', 82)
jpprice_sample =  ('Japan', 66)
ruprice_sample =  ('Russia', 171)
hgprice_sample =  ('Hungary', 474)
ukprice_sample =  ('United Kingdom', 639)
moprice_sample =  ('Morocco', 552)
sfprice_sample = ('South Africa', 790)

countrynames = [('Russia', 'Moscow'), ('South Africa', 'Johannesburg'), ('Thailand', 'Phuket'), ('China', 'Shanghai'), ('Hong Kong', 'Hong Kong'), ('Japan', 'Tokyo'), ('Japan', 'Osaka'), ('Singapore', 'Singapore'), ('Australia', 'Sydney'), ('United Kingdom', 'London'), ('Belgium', 'Brussels'), ('Ireland', 'Dublin'), ('Hungary', 'Budapest'), ('South Africa', 'Cape Town'), ('Mexico', 'Cancun'), ('United States', 'Chicago'), ('United States', 'New York'), ('United States', 'Los Angeles'), ('Canada', 'Ottawa'), ('Canada', 'Toronto'), ('Morocco', 'Marrakech')]


samplelist = [thprice_sample, sgprice_sample, hkprice_sample, caprice_sample, 
cnprice_sample, jpprice_sample, ruprice_sample, hgprice_sample,
moprice_sample, sfprice_sample, usprice_sample, ukprice_sample, auprice_sample]

def ticket(countryname, cityname, price_sample):
    
    today = datetime.datetime.now()

    i = 0
    datelst = []
    ticketlst = []

    while(i < 366):

        today = today + datetime.timedelta(days=1)
        day = today.strftime("%Y-%m-%d")
        datelst.append(day)
        i += 1

    for i in range(len(datelst)):

        price = random.randint((price_sample[1] - 20), (price_sample[1] + 100))

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
    
    countryname = c[0]
    cityname = c[1]
    
    for s in samplelist:

        if s[0] == countryname:
            price_sample = s
            
            ticket(countryname, cityname, price_sample)



        
    


