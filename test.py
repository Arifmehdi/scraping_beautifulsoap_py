from bs4 import BeautifulSoup
import requests

url = "https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue"
page = requests.get(url)
# soup = BeautifulSoup('page.text','html')


if page.status_code == 200:
    soup = BeautifulSoup(page.text, 'html.parser')

    # Extract the text content
    text_content = soup.get_text()
    soup.find('table')
    #     # Save the text content to a file
    # with open("webpage_content.txt", "w", encoding="utf-8") as file:
    #     file.write(text_content)

    print("Webpage content saved to 'webpage_content.txt'")
else:
    print("Failed to retrieve the webpage. Status code:", page.status_code)
# html_content = """
# <html>
# <head>
#     <title>Sample HTML</title>
# </head>
# <body>
#     <h1>Hello, BeautifulSoup!</h1>
#     <p>This is a sample HTML document.</p>
# </body>
# </html>
# """

# # Create a BeautifulSoup object
# soup = BeautifulSoup(html_content, 'html.parser')

# # Extract data from the HTML
# title = soup.title.text
# heading = soup.h1.text
# paragraph = soup.p.text

# Print the extracted data
# print("Title:", title)
# print("Heading:", heading)
# print("Paragraph:", paragraph)

# print(soup)