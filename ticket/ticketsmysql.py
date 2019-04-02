import datetime
import json
import pymysql
import os
import requests
from bs4 import BeautifulSoup
import re
from pprint import pprint

import flight_ticket as ft


def get_conn():
    return pymysql.connect(
    host=os.getenv('mysql_host'),
    user=os.getenv('mysql_user'),
    password=os.getenv('mysql_pw'),
    port=3306,
    db='projectdb',
    charset='utf8')



def makedate():

    today = datetime.datetime.now()

    i = 0
    datelst = []
    while(i < 366):

        today = today + datetime.timedelta(days=1)
        day = today.strftime("%Y-%m-%d")
        datelst.append(day)
        i += 1

    return datelst


ticket56 = ft.ticketprocess(56) # tuple
ticket1112 = ft.ticketprocess(1112)

sql_insert = "insert into Temp1(countryname, price, countryname, price) values(%s, %s, %s, %s)"

ticket = ticket56 + ticket1112
# print(ticket)

conn = get_conn()
with conn:
                    
    cur = conn.cursor()
    cur.execute(sql_insert, ticket)

print('---- Success!! ----')









