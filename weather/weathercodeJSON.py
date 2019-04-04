import json
import pymysql
import os
import requests
from pprint import pprint

def get_conn():
    return pymysql.connect(
    host=os.getenv('mysql_host'),
    user=os.getenv('mysql_user'),
    password=os.getenv('mysql_pw'),
    port=3306,
    db='projectdb',
    charset='utf8')

def weather():
    sql_select = 'select mpt_citycode, mpt_cityname from CityMPT'

    conn = get_conn()

    weathercity = {}

    with conn:
                        
        cur = conn.cursor()
        cur.execute(sql_select)
        rows = cur.fetchall()

        for row in rows:
            key = row[0]
            val = row[1]

            weathercity[key] = val

        return weathercity

data = weather()

with open('../weathercode.json', 'w') as jsonfile:
    json.dump(data, jsonfile, ensure_ascii=False)

print('-- success --')
