import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

companies_list = []

def getCompanyName():
    website = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    response = requests.get(website)
    content = response.text
    soup = bs(content, 'lxml')

    body = soup.find('tbody')
    cols = body.find_all('tr')

    for col in cols:
        try:
            companies_list.append(col.find('a', class_ = 'external text').get_text())
        except:
            pass

def getFinancialData(name):
    financial_info = []
    website = f'https://finance.yahoo.com/quote/{name}?p={name}' #website to scrape
    result = requests.get(website) #send a request from the website

    content = result.text #obtain content of the website

    if name != 'ABT':
        soup = bs(content, 'lxml') #convert to beautifulsoup object using a parser
        box = soup.find('ul', class_ = 'yf-dudngy')
        container = box.find_all('li')
        for i in container:
            j = i.find('span', class_ = 'value yf-dudngy')
            try:
                financial_info.append(j.get_text())
            except:
                print(j.find('fin-streamer', class_ = 'yf-dudngy').get_text())
            df = pd.DataFrame(financial_info)
            df.to_csv(f'{name}.csv')

getCompanyName()

for com in companies_list:
    getFinancialData(com)