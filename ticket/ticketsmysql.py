import datetime
import json
import pymysql
import os
import requests
from bs4 import BeautifulSoup
import re
from pprint import pprint


def approx(smonth, emonth):

    url = "https://www.skyscanner.net/g/browseservice/dataservices/browse/v3/bvweb/UK/GBP/en-GB/destinations/SELA/anywhere/{}/{}/?profile=minimalcityrollupwithnamesv2&include=image;trip&apikey=8aa374f4e28e4664bf268f850f767535".format(smonth, emonth)

    headers = {
            'Referer': 'https://www.skyscanner.net/transport/flights-from/sela/?adultsv2=1&childrenv2=&cabinclass=economy&rtn=1&preferdirects=false&outboundaltsenabled=false&inboundaltsenabled=false&oym=1905&iym=1906',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
            }

    html = requests.get(url, headers=headers).text
    jsonData = json.loads(html)
    print(jsonData)


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
select distinct(a.cityname) from Airport a left outer join Country c
on a.countrycode = c.countrycode
'''

sql_insert = ''' 
insert into Ticket(cityname, date, price) values(%s, %s, %s)
'''

with conn:
                    
    cur = conn.cursor()
    cur.execute(sql_select)
    rows = cur.fetchall()

    cityname = [row[0] for row in rows]

today = datetime.datetime.now()

i = 0
datelst = []
while(i < 366):

    today = today + datetime.timedelta(days=1)
    day = today.strftime("%Y-%m-%d")
    datelst.append(day)
    i += 1

pprint(datelst)



