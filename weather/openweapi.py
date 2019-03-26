import os
import requests
from pprint import pprint
import json
import pymysql

# def get_conn():
#     return pymysql.connect(
#     host=os.getenv('mysql_host'),
#     user=os.getenv('mysql_user'),
#     password=os.getenv('mysql_pw'),
#     port=3306,
#     db='projectdb',
#     charset='utf8')

# sql_select = 'select mpt_citycode, mpt_cityname from CityMPT'

# conn = get_conn()

# with conn:
                    
#     cur = conn.cursor()
#     cur.execute(sql_select)
#     rows = cur.fetchall()

#     city = [row[0] for row in rows]

 
city = [1835848]
apikey = os.getenv('WeatherAPI')

for c in city:

    url = "http://api.openweathermap.org/data/2.5/forecast?id={}&APPID={}".format(c, apikey)


    res = requests.get(url).text

    weather = json.loads(res)

#   print(weather)

    for w in weather['list']:

        dt = w['dt_txt']

        if dt[11:19] not in ('15:00:00', '03:00:00'):
            continue

        date = dt[0:10]

        tp = w['main']['temp']

        temp = round(tp - 273.15)

        
        desc = w['weather'][0]['description']

        print(date, temp, desc)
                



