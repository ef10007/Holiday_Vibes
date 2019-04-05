import json

with open('weathersample.json', 'r') as json_file:  
    weather = json.load(json_file)

cityname = weather['city']['name']
citycode = weather['city']['id']


sql_list = []

date = ''
main = ''
desc = ''
maxtemp = ''
mintemp = ''

for w in weather['list']:

    dt = w['dt_txt']

    if dt[11:19] not in ('15:00:00', '03:00:00'):
        continue
    else:
        desc = w['weather'][0]['description']
        main = w['weather'][0]['main']

        date = dt[0:10]

        tp = w['main']['temp']
        temp = round(tp - 273.15)

        if (dt[11:19] == '03:00:00'):
            maxtemp = temp
    
            continue

        else:
            mintemp = temp

            tupledata = (citycode, cityname, date, main, desc, maxtemp, mintemp)
            
            sql_list.append(tupledata)


print(sql_list)

# with conn:
#     cur = conn.cursor()
#     cur.executemany(sql_insert, date_list)
