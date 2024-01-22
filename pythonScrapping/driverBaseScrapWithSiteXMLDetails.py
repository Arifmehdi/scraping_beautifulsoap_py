import requests
import os
import sys

base_url = "https://driverbase.com/"
addition_url = "sitemap/"
filename ="sitemap-vlp-geo-TX.xml"  
url = base_url+addition_url+filename
filename_without_extension, file_extension = os.path.splitext(filename)
# print(filename_without_extension, file_extension)
# sys.exit()

# Replace this with the actual URL of the XML file
local_filename = f"{filename_without_extension}.xml" # Replace this with the desired local filename

# Make a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Open a local file with write-binary mode and save the content
    with open(local_filename, 'wb') as file:
        file.write(response.content)
    print(f"Downloaded {url} to {local_filename}")
else:
    print(f"Failed to download {url}. Status code: {response.status_code}")