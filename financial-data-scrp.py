from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

options = Options()
options.add_argument("--headless=new")

#web driver setup
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Navigate to the website
driver.get('https://finance.yahoo.com/markets/stocks/gainers/')

body = driver.find_elements(By.TAG_NAME, 'tr')
symbols = []
names = []
prices = []
changes = []
changes_percent = []
PE_ratios = []

for elem in body:
    try:
        symbol = elem.find_element(By.XPATH, "./td[1]").text
        name = elem.find_element(By.XPATH, "./td[2]").text
        price = elem.find_element(By.XPATH, "./td[4]").text
        change = elem.find_element(By.XPATH, "./td[5]").text
        change_percent = elem.find_element(By.XPATH, "./td[6]").text
        PE_ratio = elem.find_element(By.XPATH, "./td[10]").text

        symbols.append(symbol)
        names.append(name)
        prices.append(price)
        changes.append(change)
        changes_percent.append(change_percent)
        PE_ratios.append(PE_ratio)

    except:
        pass
df = pd.DataFrame({
    'Symbol': symbols,
    'Name': names,
    'Price': prices,
    'Change': changes,
    'Change_percent': changes_percent,
    'PE_Ratio': PE_ratios
})
df.to_csv('Top_25_Gainers.csv', index=False)

driver.quit()