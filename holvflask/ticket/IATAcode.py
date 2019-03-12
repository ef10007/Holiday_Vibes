import requests
from bs4 import BeautifulSoup
import json
import re

def iatacode():

    saveFile = '../IATAcode.json'
    try:
        file = open(saveFile, mode='x')
        file.close()
        print('-- IATAcode.json created --')
    except:
        print('-- Failed to make IATAcode.json --')
        exit()

    continental = ['Africa', 'Asia', 'Europe', 'North America', 'Oceania', 'South America']

    for c in continental:
        lst = c.lower().replace(' ', '-')

        url = "https://www.flightsfrom.com/top-100-airports-in-{}".format(lst)

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

            # pat = 'flags/(*.).png'
            pattern = re.compile('flags/(.*).png')

            code = re.findall(pattern, src)
            countrycd = code[0]

            if countrycd not in data.keys():    
                data[countrycd] = []
                data[countrycd].append((cityname, airportcd))
            else:
                data[countrycd].append((cityname, airportcd))

        # print(data)

        with open(saveFile, mode='a') as jsonfile:
            json.dump(data, jsonfile, ensure_ascii=False)

    print('--- IATAcode.json saved ---')


iatacode()

