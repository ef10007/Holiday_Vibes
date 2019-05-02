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


sql_temp = 'select * from Temp1'
conn = get_conn()
    
cur = conn.cursor()
cur.execute(sql_temp)
rows = cur.fetchall()

# pprint(rows)


data = {}

for row in rows:
    co = row[1]
    ct = row[2]

    if co not in data.keys():
        data[co] = []
        data[co].append(ct)
    else:
        data[co].append(ct)

pprint(data)

with open('getcity_renew.json', 'w') as jsonfile:
    json.dump(data, jsonfile, ensure_ascii=False)

print('success')

exit()

sql_select = 'select ct.cityname, co.countryname from City ct inner join Country co on ct.countrycode = co.countrycode'

conn = get_conn()
    
cur = conn.cursor()
cur.execute(sql_select)
rows = cur.fetchall()

ctn = [row[0] for row in rows]
con = [row[1] for row in rows]

lst = []
with open('weathercode.json') as json_file:  
    codes = json.load(json_file)

for k,v in codes.items():

    if v not in ctn:
        continue

    lst.append(v)

print(lst)

    
    


    



