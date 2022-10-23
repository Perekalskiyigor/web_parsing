# shop_scraper.py
# версия для понимания процессов
import requests
from bs4 import BeautifulSoup

url = 'https://scrapingclub.com/exercise/list_basic/?page=1'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')

for n, i in enumerate(items, start=1):
    itemName = i.find('h4', class_='card-title').text.strip()
    itemPrice = i.find('h5').text
    print(f'{n}:  {itemPrice} за {itemName}')

pages = soup.find('ul', class_='pagination')
urls = []
links = pages.find_all('a', class_='page-link')

# Записывваем ссылки на страницы в массив urls
for link in links:
    pageNum = int(link.text) if link.text.isdigit() else None
    if pageNum != None:
        # получаем ссылки по ключу из объекта href
        hrefval = link.get('href')
        # Добавляем ссылку в список
        urls.append(hrefval)

# s = 'Java is Nice' 
# # simple string replace example 
# str_new = s.replace('Java', 'Python') 
# print(str_new) 
# # replace character in string s = 'dododo' str_new = s.replace('d', 'c') print(str_new)

for slug in urls:
    newUrl = url.replace('?page=1', slug)
    response = requests.get(newUrl)
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
    for n, i in enumerate(items, start=n):
        itemName = i.find('h4', class_='card-title').text.strip()
        itemPrice = i.find('h5').text
        print(f'{n}:  {itemPrice} за {itemName}')