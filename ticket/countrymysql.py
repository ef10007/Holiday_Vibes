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


sql_insert = "insert into Country(countryname, countrycd) values(%s, %s)"
conn = get_conn()

with open('../Countrycode.json', 'r') as jsonfile:
    data = json.loads(jsonfile.read())

    for key, value in data.items():
        k = key
        v = value

        with conn:
                    
            cursor = conn.cursor()
            sql = sql_insert
            cursor.execute(sql, (k,v))
        
print('success')