import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driverPath = '/Users/jinny/Desktop/mackintosh/chromedriver'
driver = webdriver.Chrome(driverPath)

driver.get("https://www.skyscanner.net/transport/flights-from/sela?adults=1&children=0&adultsv2=1&childrenv2=&infants=0&cabinclass=economy&rtn=0&preferdirects=false&outboundaltsenabled=false&inboundaltsenabled=false&oym=1903")
time.sleep(3)

driver.find_element_by_id('filter-direct-stops-input').click()
print("The 'Direct flights only' has been clicked")
time.sleep(3)

driver.find_element_by_class_name('browse-data-route').click()
print("The anchor tag has been clicked")
time.sleep(13)

    
# driver.quit()