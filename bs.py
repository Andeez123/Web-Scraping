#beautifulsoup to scrape, requests used to send requests to google

import requests
from bs4 import BeautifulSoup as bs

website = 'https://finance.yahoo.com/quote/ABT/?p=ABT' #website to scrape
result = requests.get(website) #send a request from the website

content = result.text #obtain content of the website

soup = bs(content, 'lxml') #convert to beautifulsoup object using a parser
print(soup.prettify())

# with open('test.html', 'w') as file:
#     file.write(soup.prettify())

# box = soup.find('ul', class_ = "yf-dudngy")
# container = box.find_all('li', class_ = "yf-dudngy")
# for i in container:
#     j = i.find('span', class_ = 'value yf-dudngy')
#     try:
#         print(j.get_text())
#     except:
#         print(j.find('fin-streamer', class_ = 'yf-dudngy').get_text())