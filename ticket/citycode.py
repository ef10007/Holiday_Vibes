import requests
import json


saveFile = './Citycode.json'
try:
    file = open(saveFile, mode='x')
    file.close()
    print('-- citycode.json saved --')
except:
    print('-- Failed to make citycode.json --')
    exit()

with open('../Countrycode.json') as jsonfile:
    data = json.loads(jsonfile.read())

for key, value in data.items():
    # print(value)
    headers = {
    "referer": "https://www.skyscanner.net/transport/flights-from/sela?adults=1&children=0&adultsv2=1&childrenv2=&infants=0&cabinclass=economy&rtn=0&preferdirects=false&outboundaltsenabled=false&inboundaltsenabled=false&oym=1905&currency=GBP",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    }

    url = "https://www.skyscanner.net/g/browseservice/dataservices/browse/v3/bvweb/UK/GBP/en-GB/destinations/SELA/{}/2019-05/?profile=minimalcityrollupwithnamesv2&include=image;trip&apikey=8aa374f4e28e4664bf268f850f767535".format(value)

    html = requests.get(url, headers=headers).text
    jsonData = json.loads(html)
    
    dic = {}
    data = {}

    for i in jsonData["PlacePrices"]:

        cityid = i['Id']
        cityname = i['Name']

        data[cityname] = cityid

        dic[key] = data

    # print(dic)

    with open(saveFile, mode='a') as jsonfile:
        json.dump(dic, jsonfile, ensure_ascii=False)

print('--- The citycode.json saved ---')