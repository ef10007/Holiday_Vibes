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

    with open('Ticketprice{}.json'.format(num), 'r') as jsonfile:

        jsondata = json.load(jsonfile)
        # print(len(jsondata['PlacePrices'])) # 197

        dprice = ''
        idprice = ''

        length = len(jsondata['PlacePrices'])

        lst = []

        for i in range(1, length):

            data = jsondata['PlacePrices'][i]
            countrynames = data['Name']

            countrynames_inuse = curfetchall('dbcountryname')

            if countrynames not in countrynames_inuse:
                # print(countrynames) North Macedonia, Liberia, Tuvalu, Guyana
                continue

            keylist = data.keys()
 
            if 'DirectPrice' in keylist:

                price = data['DirectPrice']

                if price == 0:
                    dprice = random.randint(500, 1100)

                    continue
                
                else:
                    dprice = price

                direct = (countrynames, dprice)

        
                lst.append(direct)


            elif 'IndirectPrice' in keylist:
    
                price = data['IndirectPrice']
            
                if price == 0:
                    
                    idprice = random.randint(500, 1400)

                    continue

                else:
                    idprice = price

                    indirect = (countrynames, idprice)

                lst.append(indirect)
                

        return lst

