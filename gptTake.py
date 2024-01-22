from bs4 import BeautifulSoup

html_content = """
<div><small>VIN: 2C3CDZAG8GH352691</small></div>
<div><small>Stock: R52691</small></div>
"""

soup = BeautifulSoup(html_content, 'html.parser')

# Using lambda function to find the div containing "VIN:"
vin_div = soup.find(lambda tag: tag.name == 'div' and "VIN:" in tag.text)

if vin_div:
    vin = vin_div.small.text.strip()
    print("VIN:", vin)
else:
    print("VIN not found.")