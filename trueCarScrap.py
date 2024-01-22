# source :  https://www.youtube.com/watch?v=FagmjKdOIDs
# author channel name:  WsCube Tech

import requests
from bs4 import BeautifulSoup

# web = requests.get("https://www.truecar.com/used-cars-for-sale/listings/location-austin-tx/")
# web = requests.get("https://www.truecar.com/used-cars-for-sale/listings/location-memphis-tn/")
web = requests.get("https://www.truecar.com/used-cars-for-sale/listings/location-denver-co/")
# web = requests.get("https://www.truecar.com/used-cars-for-sale/listings/location-denver-co/")
# see all html in the url's website 
content = web.content
# see the website url 
content_url = web.url
# see response status code 
content_status_code = web.status_code

# =================================================
# see html formate and it initialize
soup = BeautifulSoup(web.content,'html.parser')
# see html prettier formate
soup.prettify()
title = soup.title
title_name = soup.title.name
first_p_tag = soup.p
first_a_tag = soup.a
first_h1_tag = soup.h1

# check tag type 
tag = soup.h1
type(tag)

# navigable string
first_a_tag_string = soup.a.string
type(tag)
# beautiful soup function
body_beautiful_soup = soup.body
# use prettify
soup_p_with_pretify = soup.body.prettify()

find_single_or_first = soup.find('h1')
find_all= soup.find_all('p')

# Find the element with the specified attribute
element_with_data_test = soup.find(attrs={"data-test": "allVehicleListings"})
element_with_data_test_li = element_with_data_test.li
element_with_data_test_li_by_class = element_with_data_test_li.find_all('div', class_ = 'vehicle-card')
# element_with_data_test_li_by_class = element_with_data_test_li.find_all('div', class_ = 'vehicle-card')
element_with_data_test_li_by_class_img = element_with_data_test_li_by_class.div
# # see json formate
# content_in_json = web.json()
# print(soup_prettify)
print(find_single_or_first)
# preprocessed-image-container 