# source :  https://www.youtube.com/watch?v=FagmjKdOIDs
# author channel name:  WsCube Tech

import sys
import requests
from bs4 import BeautifulSoup

# web = requests.get("https://www.truecar.com/used-cars-for-sale/listings/location-austin-tx/")
# web = requests.get("https://www.truecar.com/used-cars-for-sale/listings/location-memphis-tn/")
# web = requests.get("https://www.truecar.com/used-cars-for-sale/listings/location-denver-co/")
# web = requests.get("https://driverbase.com/inventory/location/austin-tx")
web = requests.get("https://driverbase.com/inventory/location/indianapolis-in")

# web = requests.get("https://driverbase.com/inventory/location/oakland-ca")
# see all html in the url's website 
content = web.content
# # see the website url 
content_url = web.url
# see response status code 
content_status_code = web.status_code

# # =================================================
# # see html formate and it initialize
soup = BeautifulSoup(web.content,'html.parser')
# # see html prettier formate
soup.prettify()
# title = soup.title
# title_name = soup.title.name
# first_p_tag = soup.p
# first_a_tag = soup.a
# first_h1_tag = soup.h1

# # check tag type 
# tag = soup.h1
# type(tag)

# # navigable string
# first_a_tag_string = soup.a.string
# type(tag)
# # beautiful soup function
# body_beautiful_soup = soup.body
# # use prettify
# soup_p_with_pretify = soup.body.prettify()

# find_single_or_first = soup.find('h1')
# find_all= soup.find_all('p')

# # Find the element with the specified attribute
# element_with_data_test = soup.find(attrs={"data-test": "allVehicleListings"})
# element_with_data_test_li = element_with_data_test.li
# element_with_data_test_li_by_class = element_with_data_test_li.find_all('div', class_ = 'vehicle-card')
# # element_with_data_test_li_by_class = element_with_data_test_li.find_all('div', class_ = 'vehicle-card')
# element_with_data_test_li_by_class_img = element_with_data_test_li_by_class.div
# # see json formate
# content_in_json = web.json()
# print(soup_prettify)
table =soup.table
table_tbody =table.tbody
table_tr= table_tbody.find_all('tr')
# table_tr_img= table_tr.img

element_with_data_var= table.find(attrs={"data-label": "Vehicle"})
element_with_data_var_first_pretiffy = element_with_data_var.prettify()
element_with_data_var_first_pretiffy_all_a = element_with_data_var.find_all('a')
element_with_data_test_li_by_id = element_with_data_var.find_all('h2')
element_count = len(element_with_data_var)

element_title = soup.table
count_machine = len(element_title)


vehicle_with_data = soup.find('table', id= "inventory_vehicles_table").tbody.find_all('td',class_ ="valign-middle")

# image_list = []

# for vehicles in vehicle_with_data:
#     if vehicles.a:
#         img_tag_html = vehicles.a.img
#         data_original_value = img_tag_html.get('data-original')
        
#         if data_original_value:
#             image_list.append(data_original_value)
#             print(data_original_value)


#         # print(image_info,'khobor')
#         # break
#         # img_tag = vehicles.a.img.find('img', class_ ="lazy")
        
#         # Get the value of the data-original attribute
#         # data_original_value = img_tag.get('data-original')
#         # print("data-original:", data_original_value)
#         else:
#             print("No <a> tag found within the current <td>")
# print("Image List:", image_list)

    # image = vehicles.a.img.get('data-original', 'Not found')

    # image_list.append(image)
# print(image_list,'mair khabi')



vehicle_table_title = soup.find_all(attrs={"data-label": "Vehicle"})
count_a = len(vehicle_table_title)
# print(vehicle_table_title)



title_array = []
image_array = []
price_array = []
vin_array = []

for title_data in vehicle_table_title:
    image_info = title_data.td
    # print(image_info)
    # break
    title_info = title_data.h2.string
    price_info = title_data.h4.text.strip()
    # mileage_info = title_data.find(attrs={"alt":"Vehicle engine icon"})
    # engine_info = title_data.div.small
    vin_div = title_data.find(lambda tag: tag.name == 'div' and "VIN:" in tag.text)

    if vin_div:
        vin_info = vin_div.small.text.strip()
        # print("VIN:", vin_info)
    else:
        print("VIN not found.")
    # Using lambda function to find the div containing "Stock:"
    # stock_div = title_data.find(lambda tag: tag.name == 'div' and "Stock:" in tag.text)

    # if stock_div:
    #     stock = stock_div.small.text.replace("Stock: ", "").strip()
    #     # print("Stock:", stock)
    # else:
    #     print("Stock not found.")

    title_array.append(title_info)
    image_array.append(image_info)
    price_array.append(price_info)
    vin_array.append(vin_info)
    # print(vehicle_table_title[0], 'start here i love you ',vin_info, stock)
    # break
# print(image_info, vin_info)
# print(image_list)
with open("output.txt", "w") as file:
    # Iterate through the lists and write each line to the file
    for title, image, price, vin in zip(title_array, image_array, price_array, vin_array):
        file.write(f"Title: {title}\n")
        file.write(f"Image: {image}\n")
        file.write(f"Price: {price}\n")
        file.write(f"VIN: {vin}\n")
        file.write("\n")
print('hurrah ! Text file cretaed successfully.')
# print(title_array,image_arary,price_array,vin_array)
    # Find the div containing the VIN
    # vin_div = title_data.find('div', string=lambda text: "VIN:" in text)

    # # Extract the VIN value
    # if vin_div:
    #     vin = vin_div.small.text.replace("VIN: ", "")
    #     print("VIN:", vin)
    # else:
    #     print("VIN not found.")
# text_content = vehicle_table.get_text()
    # Save the text content to a file
# with open("new_webpage_content.txt", "w", encoding="utf-8") as file:
#     file.write(vehicle_table)
        
# print(count_a,vehicle_table_title)

# # Loop through each tr in the tbody
# all_img_tags = []

# for tr_tag in soup.table.tbody.find_all('tr'):
#     # Find the img tag within each tr
#     img_tag = tr_tag.find('img')
    
#     # Check if img tag is found and add it to the list
#     if img_tag:
#         all_img_tags.append(img_tag)
# print('all_img_tags')
# # Printing the result
# for img_tag in all_img_tags:
#     print(img_tag)
# print(element_with_data_test_li_by_id)
# preprocessed-image-container data-label="Vehicle" data-label="Gallery"