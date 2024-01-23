from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys 

# Replace 'your_webdriver_path' with the path to your chromedriver.exe
webdriver_path = r"C:\Program Files\Google\Chrome\Application\chromedriver.exe"

# Set up Chrome options with the specified webdriver path
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"webdriver.chrome.driver={webdriver_path}")

# Create a new instance of the Chrome driver with the specified options
driver = webdriver.Chrome(options=chrome_options)

# URL of the page you want to scrape
url = 'https://www.carzing.com/find-dealership'  # Replace with your actual URL
# url = 'https://www.carzing.com/find-dealership'  # Replace with your actual URL
driver.get(url)
base_url ='https://www.carzing.com'
# Wait for the page to load initially
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'dealer-result-inventory')))

# Find all div elements with the specified class
div_elements = driver.find_elements(By.CLASS_NAME, 'dealer-result-inventory')


inventory_list = []
# Iterate over each div element
for div_element in div_elements:
        # Click the button in each div element
    anchor_tag = div_element.get_attribute('outerHTML')
    # button = div_element.find_element(By.TAG_NAME, 'a')
    # button.click()

        # Click the button in each div element
    button = div_element.find_element(By.TAG_NAME, 'a')

    # Wait for the button to be clickable before clicking
    wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'a')))
    button.click()

    # Switch to the newly opened tab
    wait.until(driver.switch_to.window(driver.window_handles[-1]))
    wait.until(driver.title)
    sys.exit()
    # Print the title of the current page
    print(f"Title: {driver.title}")

    # Get the URL of the current page
    current_url = driver.current_url
    print(f"Current URL: {current_url}")

    # Close the current tab
    driver.close()
    sys.exit()
    # Switch back to the main tab
    driver.switch_to.window(driver.window_handles[0])

    # anchor_tag = div_element.get_attribute('outerHTML')

    #     # Use BeautifulSoup to parse the HTML
    # soup = BeautifulSoup(anchor_tag, 'html.parser')
    # # Find the anchor tag within the div element
    # anchor_tag_a = soup.find_all('a')
    # for anchor in anchor_tag_a:
    #     full_url = base_url + anchor.get('href')
    #     inventory_list.append(full_url)
    #     # print(anchor_tag_a)

# for inventory_specific_dealer in inventory_list:
    # driver.get(inventory_specific_dealer)
    # sys.exit()
    # # Check if an anchor tag is found
    # if anchor_tag:
    #     # Extract the href attribute
    #     href_value = anchor_tag.get('href')
    #     print(f"href: {href_value}")
    # inventory_list.append(anchor_tag)
        # Print the outerHTML property of each div element
    # print(div_element.get_attribute('outerHTML'))

    # You can now continue with your logic for each div element
# sys.exit()
# Close the browser
print(inventory_list)
print(len(inventory_list))
driver.quit()
    # div_content = BeautifulSoup(div_element.get_attribute('outerHTML'), 'html.parser').prettify()
    
    # print(div_content)
    # print(div_element)
sys.exit()
    