from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time 

#Run in headless mode, the window does not open in the background
options = Options()
options.add_argument("--headless=new")

# Setup WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options) 

# Navigate to the website
driver.get('https://www.adamchoi.co.uk/overs/detailed')

# Click on "All matches" button
all_matches_button = driver.find_element(By.XPATH, '//label[@analytics-event="All matches"]')
all_matches_button.click()

country_dropdown = Select(driver.find_element(By.ID, 'country'))
country_dropdown.select_by_visible_text('Spain')

time.sleep(3)

# Wait for table rows to load
# WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, "tr")))
matches = driver.find_elements(By.TAG_NAME, 'tr')

# Extract data
date = [] 
home_team = []
score = []
away_team = []

for match in matches:
    try:
        date_val = match.find_element(By.XPATH, "./td[1]").text
        home_val = match.find_element(By.XPATH, "./td[2]").text
        score_val = match.find_element(By.XPATH, "./td[3]").text
        away_val = match.find_element(By.XPATH, "./td[4]").text

        date.append(date_val)
        home_team.append(home_val)
        score.append(score_val)
        away_team.append(away_val)
    except Exception as e:
        print(f"Error processing match: {e}")

# Create and save the DataFrame
df = pd.DataFrame({
    'date': date,
    'home_team': home_team,
    'score': score,
    'away_team': away_team
})
df.to_csv('football_data.csv', index=False)
print(df)

# Close the driver
driver.quit()
