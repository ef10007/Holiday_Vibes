import os
import requests
from pprint import pprint
import json


    # mintemp = ''
    # maxtemp = ''

apikey = os.getenv('WeatherAPI')

for c in city:

    url = "http://api.openweathermap.org/data/2.5/forecast?id={}&APPID={}".format(c, apikey)

    res = requests.get(url).text

    weather = json.loads(res)


    for w in weather['list']:
        
        dt = w['dt_txt']

        if dt[11:19] not in ('15:00:00', '03:00:00'):
            continue

        desc = w['weather'][0]['description']
        main = w['weather'][0]['main']

        date = dt[0:10]

        tp = w['main']['temp']
        temp = round(tp - 273.15)

        if dt[11:19] == '15:00:00':
            mintemp = temp

        else:
            maxtemp = temp

    print(date, mintemp, maxtemp, main, desc)

city = [1835848]
weather(city)



sql_select = 'select mpt_citycode, mpt_cityname from CityMPT'
sql_insert = 'insert into Weather(cityname, date, mintemp, maxtemp, main, desc) values(%s, %s, %s, %s, %s, %s)'

# conn = get_conn()

# with conn:
                    
#     cur = conn.cursor()
#     cur.execute(sql_select)
#     rows = cur.fetchall()

    # citycode = [1835848]
    # cityname = ['seoul']

    # citycode = [row[0] for row in rows]
    # cityname = [row[1] for row in rows] 

    # w = weather(citycode)

    # print(w)

    # cur = conn.cursor()

    # cur.execute(sql_insert, w)

# print("The weather data have been successfully stored")





                



