from bs4 import BeautifulSoup
import requests
import os
import sys
import re
import csv

# local_filename = "sitemap-vlp-geo-TX.xml"

# url_list = []

# # Open the file for reading
# with open(local_filename, 'r') as file:
#     local_file_content = file.read()

#     # Parse the XML content using BeautifulSoup
#     soup = BeautifulSoup(local_file_content, 'xml')

#     # Find all 'loc' tags and extract their text
#     loc_tags = soup.find_all('loc')
#     for loc_tag in loc_tags:
#         url_list.append(loc_tag.text)

#     filename_without_extension, file_extension = os.path.splitext(local_filename)

#     with open(f"{filename_without_extension}"+"_sitemap_url"+".txt", "a", encoding="utf-8") as file:
#             file.write(str(url_list))
#             file.write(",\t")  # Add a newline after each <tr> for better readability


# target_link = "https://driverbase.com/inventory/search/austin-tx/acura"
# if target_link in url_list:
#         print('found')
# else:
#         print('not find')
# # Print the list of URLs
# print("List of URLs:")
# # print(url_list)

############### read sitemap and check target email exist or not and result is true so go for next
base_url = "https://driverbase.com"
addition_url = "/inventory/search/"
location_url  = "austin-tx/acura"

directory_location = location_url.replace('/','_').replace('-', '_')

targated_url  = base_url+addition_url+location_url

web = requests.get(targated_url)
soup = BeautifulSoup(web.content, 'html.parser')

listing_count = soup.find('strong', id= "listing_count").text
with open(f"test03.txt", "w", encoding="utf-8") as file:
        file.write(str(soup))
print(listing_count)
sys.exit()
table = soup.find_all('tr', class_ ="inventory_row")

result_list = []

for tr in table:
    single_url = base_url+tr.a['href']
    single_img = tr.find('img')['data-original']
    single_title = tr.h2.text
    single_type = tr.find('span', class_="label label-default square").text
    single_price = tr.find('img', class_="price_field").parent.text
    # Convert the Tag object to a string before using re.search
    tr_str = str(tr)
    # Extract the script content containing the mileage information
    mileage_script = re.search(r'<script>.*?document\.write\(\'(.*?)\'\);.*?</script>', tr_str, re.DOTALL)
    # Check if a match is found
    if mileage_script:
        # Extract the mileage value using a regex
        mileage_match = re.search(r'(\d{1,3}(,\d{3})*(\.\d+)?)\s*<small>Miles</small>', mileage_script.group(1))
        single_mileage = mileage_match.group(1) if mileage_match else None

    tr_soup = BeautifulSoup(tr_str, 'html.parser')
    # Extracting engine details, transmission, and mileage
    engine_details_element = tr_soup.find('img', {'alt': 'Vehicle engine icon'})
    engine_details = engine_details_element.parent.text

    transmission_details_element = tr_soup.find('img', {'alt': 'Vehicle transmission icon'})
    transmission_details = transmission_details_element.parent.text

    mileage_details_element = tr_soup.find('img', {'alt': 'Vehicle mileage icon'})
    mileage_details = mileage_details_element.parent.text

    dealer_details_element = tr_soup.find('span', {'class': 'glyphicon glyphicon-map-marker meta'})
    dealer_details = dealer_details_element.parent.text.strip()

    star_details_element = tr_soup.find_all('span', {'class': 'glyphicon glyphicon-star'})
    star_count = len(star_details_element)

    # Incrementing dealer ID counter
    dealer_id_counter=0
    dealer_id_counter += 1
    # Creating dealer ID
    dealer_id = f"202401{dealer_id_counter:04d}"
    # Create a dictionary
    item_dict = {
        "dealer_id": dealer_id,
        "dealer_details": dealer_details,
        "details_url": single_url,
        "img_url": single_img,
        "title": single_title,
        "type": single_type,
        "price": single_price,
        "miles": single_mileage,
        "engine_details": engine_details,
        "transmission": transmission_details,
        "mileage": mileage_details,
        "star": star_count,
    }
    result_list.append(item_dict)

    # Specify the CSV file path
    csv_file_path = directory_location+".csv"

    # Specify the CSV header
    csv_header = [
        "dealer_id",
        "dealer_details",
        "details_url",
        "img_url",
        "title",
        "type",
        "price",
        "miles",
        "engine_details",
        "transmission",
        "mileage",
        "star",
    ]

    # Write the data to the CSV file
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=csv_header)
        
        # Write the header
        writer.writeheader()
        
        # Write the data
        writer.writerows(result_list)

    print(f"CSV file '{csv_file_path}' has been created.")
    # # Print or use the result_list as needed
    # for item in result_list:
    #     print(item)
    #     sys.exit()

    # # Extracting VIN details with error handling
    # vin_element = tr_soup.find('small', text=lambda text: 'VIN' in text)
    # print("Stock Details:", vin_element)
    # sys.exit()
    # vin_details = vin_element.text.strip() if vin_element else None

    # # Extracting Stock details with error handling
    # stock_element = tr_soup.find('small', text=lambda text: 'Stock' in text)
    # stock_details = stock_element.text.strip() if stock_element else None

    # print("VIN Details:", vin_details)
    # print("Stock Details:", stock_details)
    # sys.exit()

    # transmission = soup.find('div', {'alt': 'Vehicle transmission icon'}).text.strip()
    # mileage_info = soup.find('div', {'alt': 'Vehicle mileage icon'}).text.strip()

    # # Extracting VIN and stock information
    # vin_info = soup.find('div', text=lambda text: 'VIN' in text).text.strip()
    # stock_info = soup.find('div', text=lambda text: 'Stock' in text).text.strip()

    print("Star Details:", star_count)
    # print("Transmission:", transmission)
    # print("Mileage Information:", mileage_info)
    # print("VIN:", vin_info)
    # print("Stock:", stock_info)

    # print(single_mileage)
    # sys.exit()
# with open("outpit.txt", "a", encoding="utf-8") as file:
#         file.write(str(table))
#         file.write(",\t")  # Add a newline after each <tr> for better readability
# print('done')
