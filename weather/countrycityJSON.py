import json
import pymysql
import os
import requests
from bs4 import BeautifulSoup
import re

def get_conn():
    return pymysql.connect(
    host=os.getenv('mysql_host'),
    user=os.getenv('mysql_user'),
    password=os.getenv('mysql_pw'),
    port=3306,
    db='projectdb',
    charset='utf8')

conn = get_conn()

sql_select = '''
            select mpt_countryname, mpt_cityname, mpt_citycode 
            from CityMPT 
            order by mpt_countryname
            '''
data = {}

with conn:
    
    cur = conn.cursor()
    cur.execute(sql_select)
    rows = cur.fetchall()

for row in rows:
    country = row[0]
    cityname = row[1]
    citycode = row[2]
    
    if country not in data.keys():
        data[country] = []
        data[country].append((cityname, citycode))
    else:
        data[country].append((cityname, citycode))
    
with open('../getcity.json', 'w') as jsonfile:
    json.dump(data, jsonfile, ensure_ascii=False)

print('-- success --')
