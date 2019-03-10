from bs4 import BeautifulSoup
import requests

url_syd = "https://content.skyscnr.com/aa63694be729955d3709259f1cd989ea/GettyImages-484018307.jpg"

url_lnd = "https://content.skyscnr.com/6a8d297db941ab60a0f132d385fcd96c/stock-photo-panoramic-view-of-big-ben-in-london-at-sunset-113161853.jpg"

url_nyc = "https://content.skyscnr.com/b62fd4346123d1eb9f7525c8f72f2a8a/stock-photo-new-york-city-at-twilight-128894587.jpg"


def country_images(url):
    usercountry = input("Please specify the name of image file (usage. Sydney or London or NewYork)")

    img = requests.get(url).content
    saveFile = "./_image/{}.jpg".format(usercountry)
    with open(saveFile, mode="wb") as file:
        file.write(img)

    print("The image '{}.jpg' has been downloaded.".format(usercountry))

country_images(url_nyc)