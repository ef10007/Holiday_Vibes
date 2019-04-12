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

countrynames = [('United Kingdom', 'London'), ('Australia', 'Sydney'), ('United States', 'New York')]



ukprice_sample = ('United Kingdom', 639)
auprice_sample = ('Australia', 619)
usprice_sample = ('United States', 430)


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

        price = random.randint((price_sample[1] - 200), (price_sample[1] + 200))

        tupledata = (countryname, cityname, price, datelst[i])

        print(tupledata)
        
        ticketlst.append(tupledata)

    sql_insert = "insert into Ticket(countryname, cityname, price,  date) values(%s, %s, %s, %s)"


    conn = get_conn()
    with conn:
                        
        cur = conn.cursor()
        cur.executemany(sql_insert, ticketlst)

    print('---- Success to create ticket prices for {}!! ----'.format(cityname))



ticket('United States', 'New York', usprice_sample)




