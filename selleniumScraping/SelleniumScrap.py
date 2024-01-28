from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Replace 'your_webdriver_path' with the path to your webdriver executable (e.g., chromedriver.exe)
webdriver_path = r"C:\Program Files\Google\Chrome\Application\chromedriver.exe"
# Set up Chrome options with the specified webdriver path
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"webdriver.chrome.driver={webdriver_path}")

driver = webdriver.Chrome(options=chrome_options)

base_url = 'https://driverbase.com/'
additional_url = 'inventory/location/'
location = 'atlanta-ga'
url = base_url + additional_url + location

driver.get(url)

wait = WebDriverWait(driver, 30)

# Corrected condition for presence_of_element_located
wait.until(EC.presence_of_element_located((By.ID, 'inventory_vehicles_table')))

# Use a valid class name or another strategy to locate the table
table = driver.find_element(By.ID, 'inventory_vehicles_table')

print(table)
# wait.until(EC.presence_of_element_located((By.ID, 'table responsive dataTable no-footer')))
# table = driver.find_element(By.CLASS_NAME, 'table responsive dataTable no-footer')

# print(table)
# # Get the tag name of the element
# tag_name = link_to_click.tag_name
# link_to_click = driver.find_element(By.CLASS_NAME, 'your_link_class')
# print(wait)