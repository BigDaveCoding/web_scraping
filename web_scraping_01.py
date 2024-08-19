import requests
from bs4 import BeautifulSoup

webpage = requests.get('https://colonnacoffee.com/collections/beans')
colonna_soup = BeautifulSoup(webpage.content, 'html.parser')

# paragraphs = colonna_soup.find_all('p')
# links = colonna_soup.find_all('a')
# convert_to_text = [p.get_text() for p in paragraphs]
# conv_a = [a.get_text() for a in links]

# print(convert_to_text)
# print(conv_a)

# print(colonna_soup)

product_titles = colonna_soup.select('.product-card-title')
product_subtitles = colonna_soup.select('.product-card-subtitle')
titles_dict = {}
for i in range(0, len(product_titles)):
    titles_dict[product_titles[i].get_text()] = product_subtitles[i].get_text()

print(titles_dict)
