import requests
import json
from bs4 import BeautifulSoup

products = []

for i in range(5):
    link = "https://www.sulpak.kz/f/smartfoniy"

    page = requests.get(link)
    soup = BeautifulSoup(page.text, 'lxml')

    titles_raw = soup.find_all('div', class_='product__item-name')
    prices_raw = soup.find_all('div', class_='product__item-price')
    
    titles = [title.get_text(strip=True) for title in titles_raw]
    prices = [price.get_text(strip=True) for price in prices_raw]

    for i in range(len(titles)):
        products.append({
            'title': titles[i],
            'price': prices[i]
        })

with open('products.json', 'w', encoding='utf-8') as f:
    json.dump(products, f, ensure_ascii=False, indent=2)
