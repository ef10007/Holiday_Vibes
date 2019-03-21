import os
import requests
from pprint import pprint
import json


apikey = os.getenv('WeatherAPI')

cid = 2147714
locid = (28, 113) 

url = "http://api.openweathermap.org/data/2.5/forecast?id={}&APPID={}".format(cid, apikey)

# url = "http://api.openweathermap.org/data/2.5/forecast/daily?lat={lat}&lon={lon}".format(locid, apikey)


res = requests.get(url).text

weather = json.loads(res)

# print(weather)

for w in weather['city']['coord']:
    print(w)
    # date = w['dt_txt']
    # maxtemp = w['main']['temp_max']
    # mintemp = w['main']['temp_min']
    # temp = w['main']['temp']
    # desc = w['weather']['description']
    



