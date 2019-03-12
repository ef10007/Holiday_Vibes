import json

json = {"Mongolia": "MN"}


json2 = {1: {'Id': 'CJUA', 'Name': 'Jeju', 'DirectPrice': 15, 'ImageUrl': 'https://content.skyscnr.com/48a389f8137372a0eb0394896b8cd140/cjua_488471333.jpg', 'TripUrl': None}, 2: {'Id': 'CJUA', 'Name': 'Jeju', 'DirectPrice': 15, 'ImageUrl': 'https://content.skyscnr.com/48a389f8137372a0eb0394896b8cd140/cjua_488471333.jpg', 'TripUrl': None}}


dic = {}
data = {}
fd = {}

for key, value in json.items():
    
    for k, v in json2.items():
        # print(v['Id']) # 1,2
        
        countryid = v['Id']
        countryname = v['Name']

        data[countryname] = countryid

        dic[key] =  data

        print(dic)