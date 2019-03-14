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

continental = ['Africa', 'Asia', 'Europe', 'North America', 'Oceania', 'South America']

for c in continental:
    cd = c.lower().replace(' ', '-')	

    url = "https://www.flightsfrom.com/top-100-airports-in-{}".format(cd)

    html = requests.get(url).text

    soup = BeautifulSoup(html, 'html.parser') 
    lst = soup.select('div.hometoplist a')
    # print(lst)

    iatalst = [] 

    for l in lst:
        namecd = l.select_one('span.hometoplist-first').text.strip()
        s = namecd.split('   ')
        
        if '(' in s[0]:
            continue

        cityname = s[0] 
        airportcd = s[1].strip('()')

        imgtag = l.select_one('div.hometoplist-logo-wrapper img')
        src = imgtag.attrs['src']

        pattern = re.compile('flags/(.*).png')

        code = re.findall(pattern, src)
        countrycd = code[0]

        iatalst.append([countrycd, cityname, airportcd])

    # print(iatalst)

    sql_insert = "insert into Airport(countrycode, cityname, airportcode) values(%s, %s, %s)"

    for i in iatalst:
        conn = get_conn()
        with conn:
                
            cursor = conn.cursor()
            sql = sql_insert
            cursor.execute(sql, i)

print('success')

	
		


	