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

sql_list = []

date = ''
main = ''
desc = ''
maxtemp = ''
mintemp = ''

with open('weathercode.json') as json_file:  
    codes = json.load(json_file)


apikey = os.getenv('WeatherAPI')

for citycode, cityname in codes.items():
    url = "http://api.openweathermap.org/data/2.5/forecast?id={}&APPID={}".format(citycode, apikey)

    res = requests.get(url).text

    weather = json.loads(res)


    for w in weather['list']:
        
        dt = w['dt_txt']

        if dt[11:19] not in ('15:00:00', '03:00:00'):
            continue
        else:
            desc = w['weather'][0]['description']
            main = w['weather'][0]['main']

            date = '2019-04-28'

            tp = w['main']['temp']

            temp = round(tp - 273.15)

            if (dt[11:19] == '03:00:00'):
                maxtemp = temp

                continue

            else:
                if maxtemp == "":
                    maxtemp = 100

                mintemp = temp

    tupledata = (citycode, cityname, date, main, desc, mintemp, maxtemp)
    print(tupledata)
    
    sql_list.append(tupledata)


sql_insert = 'insert into Weather(citycode, cityname, dt, main, description, mintemp, maxtemp) values(%s, %s, %s, %s, %s, %s, %s)'

conn = get_conn()

with conn:
    cur = conn.cursor()
    cur.executemany(sql_insert, sql_list)


print("The blank weather data have been successfully stored")






                



