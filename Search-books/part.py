import requests
from bs4 import BeautifulSoup

def has_page_dowld(url):
    page = requests.get(url)
    if page.status_code == 200:
        return BeautifulSoup(page.text, "lxml")

def has_data_search(resul):
    return resul.find('ul', attrs = {'class': 'horizontal-list main-sections hide-on-dropdown'})

def has_text_title(dict):
    title =dict.find('li', attrs={'class' : 'p12-separator--right--primary' })
    # print(title)
    return title.get_text(dict)
    
def has_text_link(dict):
    return dict.a.get('href')
    
    
    
# page = requests.get("https://www.falabella.com.pe/falabella-pe/category/cat760702/Telefonia")
# soup = BeautifulSoup(page.content, "lxml")

# resul = soup.div
# resul['id']

# soup.status_code
# print(soup.prettify())