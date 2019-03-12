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

# with open('../Countrycode.json') as jsonfile:
#     data = json.loads(jsonfile.read())

data = {"Mongolia": "MN", "Thailand": "TH", "Singapore": "SG", "Taiwan": "TW", "Vietnam": "VN", "Philippines": "PH", "Turkey": "TR", "Indonesia": "ID", "Macau": "MO", "Malaysia": "MY", "Hong Kong": "HK", "Cambodia": "KH", "Myanmar": "MM", "Laos": "LA", "Brunei": "BN", "Qatar": "QA", "Egypt": "EG", "Ethiopia": "ET", "Israel": "IL", "French Polynesia": "PF", "Guam": "GU", "New Zealand": "NZ", "Brazil": "BR", "Fiji": "FJ", "Palau": "PW", "Canada": "CA", "Mexico": "MX", "Iran": "IR", "United Arab Emirates": "AE", "United States": "US", "Mauritius": "MU", "Northern Mariana Islands": "MP", "Australia": "AU", "Cuba": "CU", "China": "CN", "India": "IN", "Maldives": "MV", "South Korea": "KR", "Uzbekistan": "UZ", "Kazakhstan": "KZ", "Japan": "JP", "Panama": "PA", "Georgia": "GE", "Pakistan": "PK", "Sri Lanka": "LK", "Russia": "RU", "Poland": "PL", "Finland": "FI", "Austria": "AT", "Spain": "ES", "Sweden": "SE", "Denmark": "DK", "South Africa": "ZA", "Italy": "IT", "Hungary": "HU", "Greece": "GR", "Netherlands": "NL", "Belgium": "BE", "Switzerland": "CH", "France": "FR", "United Kingdom": "UK", "Belarus": "BY", "Czech Republic": "CZ", "Germany": "DE", "Benin": "BJ", "Central African Republic": "CF", "Kenya": "KE", "Burundi": "BI", "Burkina Faso": "BF", "Comoros": "KM", "Zambia": "ZM", "Saudi Arabia": "SA", "Bahrain": "BH", "Jordan": "JO", "Botswana": "BW", "DR Congo": "CD", "Cameroon": "CM", "Zimbabwe": "ZW", "Rwanda": "RW", "Mali": "ML", "Somalia": "SO", "Mauritania": "MR", "Sierra Leone": "SL", "Djibouti": "DJ", "Angola": "AO", "Ivory Coast": "CI", "Congo": "CG", "Equatorial Guinea": "GQ", "Gabon": "GA", "Eritrea": "ER", "Gambia": "GM", "Guinea": "GN", "Ghana": "GH", "Algeria": "DZ", "Kuwait": "KW", "Oman": "OM", "Paraguay": "PY", "French Guiana": "GF", "Peru": "PE", "Colombia": "CO", "Cook Islands": "CK", "New Caledonia": "NC", "Argentina": "AR", "Venezuela": "VE", "Iceland": "IS", "Suriname": "SR", "Ecuador": "EC", "Chile": "CL", "Bolivia": "BO", "Uruguay": "UY", "Bermuda": "BM", "Cyprus": "CY", "Lebanon": "LB", "Iraq": "IQ", "Papua New Guinea": "PG", "American Samoa": "AS", "Vanuatu": "VU", "Malawi": "MW", "Mozambique": "MZ", "Antigua and Barbuda": "AG", "Grenada": "GD", "Puerto Rico": "PR", "Honduras": "HN", "Guatemala": "GT", "Haiti": "HT", "Dominican Republic": "DO", "St Maarten": "SX", "US Virgin Islands": "VI", "Nicaragua": "NI", "Saint Lucia": "LC", "Montenegro": "ME", "Republic of Macedonia": "MK", "Saint Kitts and Nevis": "KN", "Belize": "BZ", "Bahamas": "BS", "Caribbean Netherlands": "BQ", "Trinidad and Tobago": "TT", "Aruba": "AW", "Cayman Islands": "KY", "Barbados": "BB", "Turks and Caicos Islands": "TC", "Saint Vincent and the Grenadines": "VC", "Guadeloupe": "GP", "Curacao": "CW", "Kyrgyzstan": "KG", "Tajikistan": "TJ", "Turkmenistan": "TM", "Azerbaijan": "AZ", "Bangladesh": "BD", "Nepal": "NP", "Costa Rica": "CR", "Jamaica": "JM", "El Salvador": "SV", "Gibraltar": "GI", "Martinique": "MQ", "Armenia": "AM", "Afghanistan": "AF", "Madagascar": "MG", "Tunisia": "TN", "Luxembourg": "LU", "Portugal": "PT", "Estonia": "EE", "Romania": "RO", "Tanzania": "TZ", "Albania": "AL", "Namibia": "NA", "Niger": "NE", "Nigeria": "NG", "Sudan": "SD", "Seychelles": "SC", "Reunion": "RE", "Chad": "TD", "Senegal": "SN", "Togo": "TG", "Morocco": "MA", "Uganda": "UG", "Serbia": "RS", "Bosnia and Herzegovina": "BA", "Kosovo": "KO", "Moldova": "MD", "Croatia": "HR", "Malta": "MT", "Ireland": "IE", "Norway": "NO", "Latvia": "LV", "Bulgaria": "BG", "Ukraine": "UA", "Lithuania": "LT", "Slovenia": "SI", "Slovakia": "SK", "South Sudan": "SS", "Crimea": "CE", "North Korea": "KP", "Eswatini": "SZ", "Solomon Islands": "SB", "East Timor": "TL"}

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