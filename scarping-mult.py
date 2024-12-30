from bs4 import BeautifulSoup as bs
import requests
import time
 
# same code
root = 'https://subslikescript.com'
website = f'{root}/movies_letter-A'
result = requests.get(website)
content = result.text
soup = bs(content, 'lxml')

pagination = soup.find('ul', class_='pagination')
pages = pagination.find_all('li', class_='page-item')
last_page = pages[-2].text

links = []
for page in range(1, int(last_page)+1)[:2]:
    website = f'{website}?page={page}'
    result = requests.get(website)
    content = result.text
    soup = bs(content, 'lxml')

    box = soup.find('article', class_='main-article')

    for link in (box.find_all('a', href=True)):
        links.append(link['href'])
    
    # Extracting the movie transcript
    for link in links:
        try:
            time.sleep(1)
            website = f'{root}/{link}'
            result = requests.get(website)
            content = result.text
            soup = bs(content, 'lxml')
            box = soup.find('article', class_='main-article')

            title = box.find('h1').get_text()
            transcript = box.find('div', class_='full-script').get_text(strip=True, separator = ' ')
            with open(f'{title}.txt', 'w', encoding='utf-8') as file:
                file.write(transcript)

        except:
            print("Error!")

        