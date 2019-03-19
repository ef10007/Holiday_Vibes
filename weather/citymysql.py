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

sql_select = "select distinct(cityname) from Airport"
sql_insert = "insert into City(citycode, cityname, countrycode) values(%s, %s, %s)"

with conn:
    
    cur = conn.cursor()
    cur.execute(sql_select)
    rows = cur.fetchall()

for row in rows:
    acityname = row[0]

    with open('../Weathercitycode.json', 'r') as jsonfile:
        data = json.loads(jsonfile.read())

        for datum in data:

            weathercid = datum['id']
            countrycode = datum['country']
            wcityname = datum['name']

            if acityname == wcityname:

                with conn:
                    cursor = conn.cursor()
                    sql = sql_insert
                    cursor.execute(sql, (weathercid, wcityname, countrycode))
        
print('-- success --')