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


# with open('../weathercode.json') as json_file:  
#     codes = json.load(json_file)

# citycode = [code for code in codes]
# cityname = [code for code in codes.values()]

citycode = [1835848, 1835848]
cityname = 'seoul'

mintemp = ''
maxtemp = ''

apikey = os.getenv('WeatherAPI')

sql_insert = 'insert into Weather(cityname, date, mintemp, maxtemp, main, desc) values(%s, %s, %s, %s, %s, %s)'

conn = get_conn()

for code in citycode:
    url = "http://api.openweathermap.org/data/2.5/forecast?id={}&APPID={}".format(code, apikey)

    res = requests.get(url).text

    weather = json.loads(res)

    cityname = weather['city']['name']

    
pprint(w)

exit()
for w in weather['list']:
    
    
    
    dt = w['dt_txt']
    if dt[11:19] not in ('15:00:00', '03:00:00'):
        continue

    desc = w['weather'][0]['description']
    main = w['weather'][0]['main']

    date = dt[0:10]


    tp = w['main']['temp']
    print(tp)    

    

    if tp != 0:
        temp = round(tp - 273.15)

    if dt[11:19] == '15:00:00':
        temp = mintemp

    else:
        temp = maxtemp

        print(date, mintemp, maxtemp, main, desc)

        with conn:

            cur = conn.cursor()
            cur.execute(sql_insert, (cityname, date, mintemp, maxtemp, main, desc))

print("The weather data have been successfully stored")






                



