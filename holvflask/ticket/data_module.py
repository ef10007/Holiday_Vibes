from bs4 import BeautifulSoup
import requests
import json
import os

def ticket_prices(userdate):

    if len(userdate) == 0:
        print("Please input both year and month (usage. 2019-02)")
        exit()

    city_code = ["SYDA", "LOND", "NYCA", "HEL", 'VLAD', 'ADDA', 'SPNA']
    

    for i, j in enumerate(city_code):
        url = "https://www.skyscanner.net/g/browseservice/dataservices/browse/v3/mvweb/UK/GBP/en-GB/calendar/SELA/{}/{}/?profile=minimalmonthviewgridv2&abvariant=FLUX_GDT2791_SendPriceTraceToMixpanel:b|rts_wta_shadowtraffic:b&apikey=c32d1a225f454c49a44ddec56ddc6910".format(city_code[i], userdate)


        headers = {
            'Referer': 'https://www.skyscanner.net/transport/flights/sela/{}?adults=1&children=0&adultsv2=1&childrenv2=&infants=0&cabinclass=economy&rtn=0&preferdirects=false&outboundaltsenabled=false&inboundaltsenabled=false&oym=1902&selectedoday=01'.format(city_code[i].lower()) ,
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }

        html = requests.get(url, headers=headers).text
        jsonData = json.loads(html)

        for idx, i in enumerate(jsonData["PriceGrids"]["Grid"][0]):
            print(i)

    print("------------- save --------------")

ticket_prices('2019-03')