import os
import requests
from pprint import pprint
import pymysql
import json

def get_conn():
    return pymysql.connect(
    host=os.getenv('mysql_host'),
    user=os.getenv('mysql_user'),
    password=os.getenv('mysql_pw'),
    port=3306,
    db='projectdb',
    charset='utf8')

sql_select = '''
select DISTINCT cityname, citycode from Weather where  cityname in ('Moscow', 'Johannesburg', 'Phuket',
 'Shanghai', 'Hong Kong', 'Seoul', 'Tokyo', 'Osaka', 'Singapore', 
 'Sydney', 'London', 'Brussels', 'Dublin', 'Budapest', 'Cape Town', 
 'Mexico City', 'Cancun', 'Chicago', 'Los Angeles', 'Ottawa', 'Toronto',
 'Marrakech', 'New York')
'''

conn = get_conn()
    
cur = conn.cursor()
cur.execute(sql_select)
rows = cur.fetchall()


d = {}

for row in rows:

    cityname = row[0]
    citycode = row[1]

    d[citycode] = cityname

pprint(d)


with open('weathercode.json', 'w') as jsonfile:
    json.dump(d, jsonfile, ensure_ascii=False)

print('--- json saved ---')