import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

website = 'http://webscraper.io/test-sites/tables'
response = requests.get(website)
content = response.text
soup = bs(content, 'lxml')

div_class = soup.find('div', class_ = 'tables-semantically-correct')
tables = div_class.find_all('table')

with open('filename.txt', 'w') as file:
    store = []
    for table in tables:
        body = table.find('tbody')
        vals = body.find_all('tr')
        for val in vals:
            container_val = val.get_text()
            file.write(container_val)

