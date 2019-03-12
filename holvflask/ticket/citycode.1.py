import requests
import json


headers = {
"referer": "https://www.skyscanner.net/transport/flights-from/sela?adults=1&children=0&adultsv2=1&childrenv2=&infants=0&cabinclass=economy&rtn=0&preferdirects=false&outboundaltsenabled=false&inboundaltsenabled=false&oym=1905&currency=GBP",
"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}

url = "https://www.skyscanner.net/g/browseservice/dataservices/browse/v3/bvweb/UK/GBP/en-GB/destinations/SELA/KR/2019-05/?profile=minimalcityrollupwithnamesv2&include=image;trip&apikey=8aa374f4e28e4664bf268f850f767535"

html = requests.get(url, headers=headers).text
jsonData = json.loads(html)

for i in jsonData['PlacePrices']:
    print(i)