import requests
from bs4 import BeautifulSoup

data = requests.get('https://www.weblancer.net/jobs/').text
soup = BeautifulSoup(data, 'html.parser')

divs = soup.find('div', class_='dropdown-menu block-content text_field').find_all('li')

for div in divs: 
    try:    
        li_href = div.find('a').get('href')
        li_text = div.find('a').getText()
        print(li_text)
        print(li_href)
    except:
        pass