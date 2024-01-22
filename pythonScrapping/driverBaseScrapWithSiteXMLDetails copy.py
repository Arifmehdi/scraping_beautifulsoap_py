# import sys
# import time
# import requests
# from bs4 import BeautifulSoup
# from urllib.parse import urlparse
# from urllib.parse import unquote
# import os
# # import pandas as pd

# # # static route for check without hit 
# # url = "https://driverbase.com/inventory/location/dallas-tx"
# # url = "https://driverbase.com/inventory/location/newyork-ny"
# # url = "https://driverbase.com/inventory/location/houston-tx"
# base_url = "https://driverbase.com/"
# addition_url = "inventory/location/"

# # location_url  = "seattle-wa"
# # location_url  = "sandiego-ca"
# # location_url  = "nashville-tn"
# # location_url  = "chichester-nh"
# # location_url  = "kansascity-mo"
# # location_url  = "atlanta-ga"
# # location_url  = "lasvegas-nv"
# location_url  = "charlottesville-va"
# url = base_url+addition_url+location_url

# parsed_url = urlparse(url)
# location = parsed_url.path.split("/")[-1]

# web = requests.get(url)
# soup = BeautifulSoup(web.content, 'html.parser')
# # table = soup.find_all('td', class_ ="valign-middle" , attrs{'data-label":"Gallery"'})
# table =  soup.find_all('td', class_='valign-middle', attrs={'data-label': 'Gallery'})


# table_array = []

# # Check if the table is found before trying to access it
# if table:
#     for row in table:
#         table_array.append(base_url+row.a.get('href'))
#         time.sleep(4)
#     # print(row.get_text(separator='\n'))
#         # table_text = table.get_text(separator='\n')

#     # Write both the HTML content and the extracted text to a text file

#         # file.write(f"HTML Content from {url}:\n")
#         # file.write(str(soup))
#         # file.write("\n\nText Content from the table:\n")
#         # file.write(table_text)
# else:
#     print("Table not found on the webpage.")

# title=''
# dealer_info =''
# dealer_list =''
# dealer_address=''
# for vehicleDetails in table_array:
#     detailWeb = requests.get(vehicleDetails)
#     detaillSoup = BeautifulSoup(detailWeb.content,'html.parser')



#     detailSouptable = detaillSoup.find_all('table')
#     imageSoup = detaillSoup.select('div.col-sm-6 img')

#     # dealer_info = detaillSoup.find('div',class_ = "place-desc-large") 
#     # print(detaillSoup.find('div',class_ = "place-desc-large"))

#     # Find all iframe tags
#     iframe_tags = detaillSoup.find_all('iframe')

#     # Check if there is at least one iframe tag
#     if len(iframe_tags) >= 2:
#         # Select the second iframe tag
#         second_iframe = iframe_tags[1]

#         # Extract the src attribute from the second iframe tag
#         iframe_src = second_iframe.get('src', '')

#         # Decode URL-encoded characters in the src attribute
#         decoded_src = unquote(iframe_src)

#         # Extract dealer name and address from the decoded src attribute
#         query_params = decoded_src.split('?')[1].split('&')
#         for param in query_params:
#             if 'q=' in param:
#                 dealer_info = param.split('=')[1]
#                 dealer_info_parts = dealer_info.split(',')
                 
#                 # Assign the first part to dealer_name and the rest to dealer_address
#                 dealer_name = dealer_info_parts[0].strip()
#                 dealer_address = ', '.join(part.strip() for part in dealer_info_parts[1:])
                
#                 # print(f"Dealer Name: {dealer_name}")
#                 # print(f"Dealer Address: {dealer_address}")
#     else:
#         print("There are less than 2 iframe tags in the HTML.")
    
#     # iframe_src = detaillSoup.iframe
#     # print(second_iframe)
#     # sys.exit()
#     # Extract dealer name and address from the src attribute
#     # query_params = iframe_src.split('?')[1].split('&')
#     # for param in query_params:
#     #     if 'q=' in param:
#     #         dealer_info = param.split('=')[1]
#     #         dealer_name, dealer_address = map(lambda x: x.strip(), dealer_info.split(','))
#     #         print(f"Dealer Name: {dealer_name}")
#     #         print(f"Dealer Address: {dealer_address}")
#     #         sys.exit()
#     # with open("out.txt", "w", encoding="utf-8") as file:
#     #     # Iterate over each <tr> element
#     #     file.write(str(dealer_info))
#     # sys.exit()
#     image_list = []
#     for image in imageSoup:
#         src_value = image['src']
#         cleaned_url = src_value.split('?')[0]
#         if src_value.startswith(('http://', 'https://')):
#             image_list.append(cleaned_url)

#             # Get the image file name from the URL
#             image_name = os.path.basename(cleaned_url)
#             # Extract the filename without the extension
#             filename_without_extension, file_extension = os.path.splitext(image_name)
#             # Create the folder path based on the extracted filename
#             # folder_name = filename_without_extension.split('-')[0]
#             # images_folder = 'upload/'+location_url
#             # title_make = detaillSoup.title.text.strip()
#             # title_without_whitespace = title_make.replace(" ", "_")

#             dealer_make = dealer_info
#             dealer_without_whitespace = dealer_make.replace(" ", "_")

#             images_folder = os.path.join('upload', location_url, dealer_without_whitespace)
            
#             # Create the full path to save the image
#             image_path = os.path.join(images_folder, image_name)
#             # Create the folder if it doesn't exist
#             os.makedirs(images_folder, exist_ok=True)
#             # Download the image
#             response = requests.get(src_value, stream=True)
            
#             # Check if the request was successful (status code 200)
#             if response.status_code == 200:
#                 # Save the image to the specified folder
#                 with open(image_path, 'wb') as file:
#                     for chunk in response.iter_content(chunk_size=128):
#                         file.write(chunk)
#                 print(f"Image '{image_name}' downloaded and saved to '{images_folder}'")
#             else:
#                 print(f"Failed to download image '{image_name}'. Status code: {response.status_code}")


#             # print(src_value)
#         time.sleep(20)

#     # with open("output2.txt", "w", encoding="utf-8") as file:
#     #     # Iterate over each <tr> element
#     #     file.write(str(image_list))
#     #     file.write("\n") 
#     #     print(image_list)
#     #     sys.exit()
#     title = detaillSoup.title.text.strip()


#             # Check if there is at least one table
#     if len(detailSouptable) == 2:
#         second_table = detailSouptable[1]
#         second_table_tbody_tr = second_table.find_all('tr')
#     else:
#         print("There are fewer than two tables in the HTML.")
#     # print(detailSouptable)
#     # sys.exit()
#     # Open the file for writing
#     # #######check for output txt 
#     # with open("output.txt", "a", encoding="utf-8") as file:
        
        
#     # topics_dictionary = {

#     # }
#         # Incrementing dealer ID counter
#     dealer_id_counter =0
#     dealer_id_counter += 1

#     # Creating dealer ID
#     dealer_id = f"202401{dealer_id_counter:04d}"
#     # Create a dictionary
#     dealer_info_dict = {
#         "dealer_id": dealer_id,
#         "dealer_name": dealer_name,
#         "dealer_address": dealer_address
#     }
#     print(dealer_info_dict)
#     sys.exit()
#     with open(f"{location}"+".txt", "a", encoding="utf-8") as file:
#         # Iterate over each <tr> element
#         file.write(f"{image_list}\n")
#         file.write(f"{title}\n")
#         file.write(f"{dealer_info}\n")
#         file.write(f"{dealer_address}\n")
#         file.write("\n") 
#         for i,tr in enumerate(second_table_tbody_tr):
#             # Extract and write the text content of each <tr> to the file
#             # file.write(str(tr.get_text(separator='\n')))
#             file.write(str(tr.get_text()))
#             file.write(",\t")  # Add a newline after each <tr> for better readability

#     # Print the list of <tr> elements
#     for tr in second_table_tbody_tr:
#         print(tr.get_text(separator='\n'))

#     # print(second_table_tbody_tr)
#     # sys.exit()

#     # time.sleep(60)
# print('Done with image')
# sys.exit()
# # print(table_array)
# sys.exit()
# with open(f"{location}.txt", "w", encoding="utf-8") as file:
#     file.write(str(table_array))
# print('ok done')
# sys.exit()


# # # Write both the HTML content and the extracted text to a text file
# # with open("output.txt", "w", encoding="utf-8") as file:

# #     file.write(table)







# # with open('')

# print(table)
# sys.exit()
# print('we are ok')


https://driverbase.com/inventory?search.SortTypeId=3&search.DealershipId=0&search.Zip=78702&search.DistanceFromZip=100&search.InventoryType=all&search.MakeId=333&search.ModelId=-1&search.VehicleBodyTypeId=0&search.YearMin=1980&search.YearMax=2024&search.PriceMinString=%241%2C000&search.PriceMaxString=%24150%2C000%2B&search.MpgMinString=0&search.MpgMaxString=100%2B&search.MileageMinString=0&search.MileageMaxString=200%2C000%2B&search.RequireImages=true&search.PropulsionTypeId=0&search.CabTypeId=0&search.TransmissionTypeId=1&search.SIdx=1&search.EIdx=15&search.Next=true&search.Trims=-1


https://driverbase.com/inventory?search.SortTypeId=3&search.DealershipId=0&search.Zip=78702&search.DistanceFromZip=100&search.InventoryType=all&search.MakeId=333&search.ModelId=-1&search.VehicleBodyTypeId=0&search.YearMin=1980&search.YearMax=2024&search.PriceMinString=%241%2C000&search.PriceMaxString=%24150%2C000%2B&search.MpgMinString=0&search.MpgMaxString=100%2B&search.MileageMinString=0&search.MileageMaxString=200%2C000%2B&search.RequireImages=true&search.PropulsionTypeId=0&search.CabTypeId=0&search.TransmissionTypeId=1&search.SIdx=16&search.EIdx=30&search.Next=true&search.Trims=-1

https://driverbase.com/inventory?search.SortTypeId=3&search.DealershipId=0&search.Zip=78702&search.DistanceFromZip=100&search.InventoryType=all&search.MakeId=333&search.ModelId=-1&search.VehicleBodyTypeId=0&search.YearMin=1980&search.YearMax=2024&search.PriceMinString=%241%2C000&search.PriceMaxString=%24150%2C000%2B&search.MpgMinString=0&search.MpgMaxString=100%2B&search.MileageMinString=0&search.MileageMaxString=200%2C000%2B&search.RequireImages=true&search.PropulsionTypeId=0&search.CabTypeId=0&search.TransmissionTypeId=1&search.SIdx=16&search.EIdx=30&search.Next=true&search.Trims=-1

https://driverbase.com/inventory?search.SortTypeId=3&search.DealershipId=0&search.Zip=78702&search.DistanceFromZip=100&search.InventoryType=all&search.MakeId=333&search.ModelId=-1&search.VehicleBodyTypeId=0&search.YearMin=1980&search.YearMax=2024&search.PriceMinString=%241%2C000&search.PriceMaxString=%24150%2C000%2B&search.MpgMinString=0&search.MpgMaxString=100%2B&search.MileageMinString=0&search.MileageMaxString=200%2C000%2B&search.RequireImages=true&search.PropulsionTypeId=0&search.CabTypeId=0&search.TransmissionTypeId=1&search.SIdx=31&search.EIdx=45&search.Next=true&search.Trims=-1


https://driverbase.com/inventory?search.SortTypeId=3&search.DealershipId=0&search.Zip=78702&search.DistanceFromZip=100&search.InventoryType=all&search.MakeId=333&search.ModelId=-1&search.VehicleBodyTypeId=0&search.YearMin=1980&search.YearMax=2024&search.PriceMinString=%241%2C000&search.PriceMaxString=%24150%2C000%2B&search.MpgMinString=0&search.MpgMaxString=100%2B&search.MileageMinString=0&search.MileageMaxString=200%2C000%2B&search.RequireImages=true&search.PropulsionTypeId=0&search.CabTypeId=0&search.TransmissionTypeId=1&search.SIdx=16&search.EIdx=30&search.Prev=true&search.Trims=-1


https://driverbase.com/inventory?search.SortTypeId=3&search.DealershipId=0&search.Zip=78702&search.DistanceFromZip=100&search.InventoryType=all&search.MakeId=333&search.ModelId=-1&search.VehicleBodyTypeId=0&search.YearMin=1980&search.YearMax=2024&search.PriceMinString=%241%2C000&search.PriceMaxString=%24150%2C000%2B&search.MpgMinString=0&search.MpgMaxString=100%2B&search.MileageMinString=0&search.MileageMaxString=200%2C000%2B&search.RequireImages=true&search.PropulsionTypeId=0&search.CabTypeId=0&search.TransmissionTypeId=1&search.SIdx=1&search.EIdx=15&search.Next=true&search.Trims=-1


https://driverbase.com/inventory?search.SortTypeId=3&search.DealershipId=0&search.Zip=78702&search.DistanceFromZip=100&search.InventoryType=all&search.MakeId=333&search.ModelId=-1&search.VehicleBodyTypeId=0&search.YearMin=1980&search.YearMax=2024&search.PriceMinString=%241%2C000&search.PriceMaxString=%24150%2C000%2B&search.MpgMinString=0&search.MpgMaxString=100%2B&search.MileageMinString=0&search.MileageMaxString=200%2C000%2B&search.RequireImages=true&search.PropulsionTypeId=0&search.CabTypeId=0&search.TransmissionTypeId=1&search.SIdx=16&search.EIdx=30&search.Next=true&search.Trims=-1

https://driverbase.com/inventory?search.SortTypeId=3&search.DealershipId=0&search.Zip=78702&search.DistanceFromZip=100&search.InventoryType=all&search.MakeId=333&search.ModelId=-1&search.VehicleBodyTypeId=0&search.YearMin=1980&search.YearMax=2024&search.PriceMinString=%241%2C000&search.PriceMaxString=%24150%2C000%2B&search.MpgMinString=0&search.MpgMaxString=100%2B&search.MileageMinString=0&search.MileageMaxString=200%2C000%2B&search.RequireImages=true&search.PropulsionTypeId=0&search.CabTypeId=0&search.TransmissionTypeId=1&search.SIdx=31&search.EIdx=45&search.Next=true&search.Trims=-1

# jhfjhfjksf jsdghf sfgjhsdgf hisdgfhi sgfhs hsdgfhsdgfjhksghh jhsdfghsgfh safhgs hfa ahsfgjhasfgfhjgasdjhdf hasfghjasgfjh hg

https://driverbase.com/inventory/search/austin-tx/acura

https://driverbase.com/inventory?search.SortTypeId=3&search.DealershipId=0&search.Zip=78702&search.DistanceFromZip=100&search.InventoryType=all&search.MakeId=333&search.ModelId=-1&search.VehicleBodyTypeId=0&search.YearMin=1980&search.YearMax=2024&search.PriceMinString=%241%2C000&search.PriceMaxString=%24150%2C000%2B&search.MpgMinString=0&search.MpgMaxString=100%2B&search.MileageMinString=0&search.MileageMaxString=200%2C000%2B&search.RequireImages=true&search.PropulsionTypeId=0&search.CabTypeId=0&search.TransmissionTypeId=1&search.SIdx=91&search.EIdx=105&search.Next=true&search.Trims=-1

