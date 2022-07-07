from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.myteemaze.com/jumpshot').text
soup = BeautifulSoup(source, 'lxml')

# print(soup.prettify())

product_name = soup.find('h1')
print(product_name.text)
product_price = soup.find('span', class_="color-red")
print(product_price.text)

for product_images in soup.find_all(
        'div', class_="RetailImage p-relative"):
    print(product_images.div.img['src'])

product_color = soup.find_all('span')
print(product_color)


ul = soup.find('ul', class_='custom-bullets')
for li in ul.find_all('li'):
    print(li.span.text)
