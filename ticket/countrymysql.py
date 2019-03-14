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

with open('../Countrycode.json', 'r') as jsonfile:
    data = json.loads(jsonfile.read())

    for key, value in data.items():
        k = key
        v = value

   



# sql_insert = "insert into Country(countrycd, countryname) values(%s, %s)"
# lst=[]

# conn = get_conn()
# with conn:
        
#     cursor = conn.cursor()
#     sql = sql_insert
#     cursor.execute(sql, lst)
    
# print('success')