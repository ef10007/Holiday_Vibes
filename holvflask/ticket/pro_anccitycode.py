from bs4 import BeautifulSoup
import requests
import json


url = "https://www.skyscanner.net/transport/flights-from/sela?adults=1&children=0&adultsv2=1&childrenv2=&infants=0&cabinclass=economy&rtn=0&preferdirects=false&outboundaltsenabled=false&inboundaltsenabled=false&oym=1903" 


html = requests.get(url).text

soup = BeautifulSoup(html, 'html.parser')

trs = soup.select('#browse-section > div.result-list > ul > li.browse-list-category.open > ul > li:nth-of-type(1) > div > div.browse-data-entry.trip-link > a.flightLink.onlyFlight')


for tr in trs:
    print(tr)


# jsonData = json.loads(html)
