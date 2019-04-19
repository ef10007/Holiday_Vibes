from datetime import datetime, date, timedelta
import datetime
from pprint import pprint
import json

today = datetime.datetime.now()

i = 1
data = {}
data1 = {}

while(i < 1000):

    datelst = []

    today = today + datetime.timedelta(days=1)

    day = today.strftime("%Y-%m-%d")

    data1[day] = day

    i += 1

data["calendar"] = data1

# pprint(data)

with open('calendar.json', 'w') as jsonfile:
    json.dump(data, jsonfile, ensure_ascii=False)

print("JSON completed")