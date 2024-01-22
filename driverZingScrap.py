import sys
import requests
from bs4 import BeautifulSoup

web = requests.get("https://www.carzing.com/find-dealership")

print(web)

# base_url = "https://www.carzing.com/"
# addition_url = "inventory/location/"
# location_url  = "chichester-nh"