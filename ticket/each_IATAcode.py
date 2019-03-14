import requests
from bs4 import BeautifulSoup
import json
import re


def iatacode(cd):

    url = "https://www.flightsfrom.com/top-100-airports-in-{}".format(cd)

    html = requests.get(url).text

    soup = BeautifulSoup(html, 'html.parser') 
    lst = soup.select('div.hometoplist a')
    # print(lst)

    data = {}

    for l in lst:
        namecd = l.select_one('span.hometoplist-first').text.strip()
        s = namecd.split('   ')
        
        if '(' in s[0]:
            continue

        cityname = s[0] 
        airportcd = s[1].strip('()')

        imgtag = l.select_one('div.hometoplist-logo-wrapper img')
        src = imgtag.attrs['src']
        # print(type(src)) #str 

        pattern = re.compile('flags/(.*).png')

        code = re.findall(pattern, src)
        countrycd = code[0]

        if countrycd not in data.keys():    
            data[countrycd] = []
            data[countrycd].append((cityname, airportcd))
        else:
            data[countrycd].append((cityname, airportcd))

    # print(data)

    with open('../{}_IATAcode.json'.format(cd), 'w') as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False)

    print('--- {}_IATAcode.json saved ---'.format(cd))



continental = ['Africa', 'Asia', 'Europe', 'North America', 'Oceania', 'South America']

for c in continental:
    cd = c.lower().replace(' ', '-')

    iatacode(cd)
