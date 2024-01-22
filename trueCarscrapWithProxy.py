import requests
from bs4 import BeautifulSoup


with open("proxies_list.txt", "r") as file:
    proxy_lines = file.readlines()

if proxy_lines:
    proxy_info = proxy_lines[0].strip()

else:
    print("No proxy information found in the file.")
    exit()

# proxy_info = '103.74.144.4:80'
print(proxy_info)
proxy = {
    "http": "http://" + proxy_info,
    "https": "http://" + proxy_info,
}

# Make the request using the proxy
web = requests.get("https://www.truecar.com/used-cars-for-sale/listings/location-austin-tx/", proxies=proxy)


# Check if the request was successful (status code 200)
if web.status_code == 200:
    content = web.content

    # Your further processing with BeautifulSoup or other libraries
    soup = BeautifulSoup(content, 'html.parser')
    # Continue with your code...

else:
    print("Failed to retrieve the webpage. Status code:", web.status_code)