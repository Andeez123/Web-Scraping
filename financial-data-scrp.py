from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

#web driver setup
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Navigate to the website
driver.get('https://finance.yahoo.com/news/')

while True:
    pass