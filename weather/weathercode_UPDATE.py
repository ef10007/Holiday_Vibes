import json 
from pprint import pprint
import pymysql
import os


def get_conn():
    return pymysql.connect(
    host=os.getenv('mysql_host'),
    user=os.getenv('mysql_user'),
    password=os.getenv('mysql_pw'),
    port=3306,
    db='projectdb',
    charset='utf8')


sql_select = "select DISTINCT cityname, citycode from Weather;"

conn = get_conn()
with conn:
                    
    cur = conn.cursor()
    cur.execute(sql_select)
    rows = cur.fetchall()

#pprint(rows)

cityname = [row[0] for row in rows]
citycode = [row[1] for row in rows]


with open('weathercode.json') as jsonfile:
    data = json.loads(jsonfile.read())

# print(lst)

