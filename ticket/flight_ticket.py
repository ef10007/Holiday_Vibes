import json
from pprint import pprint
import pymysql
import os
import random

def get_conn():
    return pymysql.connect(
    host=os.getenv('mysql_host'),
    user=os.getenv('mysql_user'),
    password=os.getenv('mysql_pw'),
    port=3306,
    db='projectdb',
    charset='utf8')

sql_select = "select countryname from Country"

def curfetchall(listname):

    conn = get_conn()
    with conn:
                        
        cur = conn.cursor()
        cur.execute(sql_select)
        rows = cur.fetchall()

        listname = [row[0] for row in rows]

        return listname 

def ticketprocess(num):

    with open('../Ticketprice{}.json'.format(num), 'r') as jsonfile:

        jsondata = json.load(jsonfile)

        for data in jsondata['PlacePrices']:
        
            countrynames = data['Name']

            if countrynames not in curfetchall('dbcountryname'):
                continue

            keylist = data.keys()
 
            if 'DirectPrice' in keylist:
                price = data['DirectPrice']

                if price == 0:
                    price = random.randint(700, 1200)

            else:
                price = data['IndirectPrice']

                if price == 0:
                    price = random.randint(700, 1100)
                    
            print("{} -----".format(num), countrynames, price)

            return countrynames, price
