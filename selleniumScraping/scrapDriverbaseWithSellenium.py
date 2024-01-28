
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys


# # # Replace 'your_webdriver_path' with the path to your webdriver executable (e.g., chromedriver.exe)
# webdriver_path = r"C:\Program Files\Google\Chrome\Application\chromedriver.exe"

# url = 'https://driverbase.com/inventory/search/austin-tx/acura'

# # Create a new instance of the Chrome driver
# driver = webdriver.Chrome(executable_path=webdriver_path)

# # # Navigate to the page
# data = driver.get(url)

# ################################# Replace 'your_webdriver_path' with the path to your chromedriver.exe
# webdriver_path = r"C:\Program Files\Google\Chrome\Application\chromedriver.exe"

# # Set up Chrome options with the specified webdriver path
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument(f"webdriver.chrome.driver={webdriver_path}")

# # Create a new instance of the Chrome driver with the specified options
# driver = webdriver.Chrome(options=chrome_options)

# # Rest of your code...

# # Close the browser
# print(driver)
# driver.quit()




# Replace 'your_webdriver_path' with the path to your webdriver executable (e.g., chromedriver.exe)
webdriver_path = r"C:\Program Files\Google\Chrome\Application\chromedriver.exe"

# Set up Chrome options with the specified webdriver path
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"webdriver.chrome.driver={webdriver_path}")

# Create a new instance of the Chrome driver with the specified options
driver = webdriver.Chrome(options=chrome_options)

url = 'https://driverbase.com/inventory/search/austin-tx/acura'

# # Create a new instance of the Chrome driver
# driver = webdriver.Chrome(executable_path=webdriver_path)

# Navigate to the page
driver.get(url)

# Wait for the page to load initially
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, 'listing_count')))

next_button = driver.find_element(By.XPATH, '//button[contains(text(), "Next")]')
next_button.click()
# Wait for the page to load after clicking "Next"
wait.until(EC.presence_of_element_located((By.ID, 'listing_count')))

# Get the updated URL after clicking "Next"
updated_url = driver.current_url
print(f"Updated URL after clicking Next: {updated_url}")
print('done')
sys.exit()

# Your logic to click on a link
# For example, clicking on the first link with a specific class
link_to_click = driver.find_element(By.CLASS_NAME, 'your_link_class')
link_to_click.click()

# Wait for the page to load after clicking the link
wait.until(EC.presence_of_element_located((By.ID, 'listing_count')))

# Get the current URL after clicking the link
current_url_after_click = driver.current_url
print(f"Current URL after clicking link: {current_url_after_click}")

# Your logic to click on the "Next" button
next_button = driver.find_element(By.XPATH, '//button[contains(text(), "Next")]')
next_button.click()

# Wait for the page to load after clicking "Next"
wait.until(EC.presence_of_element_located((By.ID, 'listing_count')))

# Get the updated URL after clicking "Next"
updated_url = driver.current_url
print(f"Updated URL after clicking Next: {updated_url}")

# Close the browser
driver.quit()
