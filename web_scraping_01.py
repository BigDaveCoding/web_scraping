import requests
from bs4 import BeautifulSoup
import json

#using requests to get the html from the webpage
webpage = requests.get('https://colonnacoffee.com/collections/beans')
#creating soup of the webpage using the .content and html parser
colonna_soup = BeautifulSoup(webpage.content, 'html.parser')

#getting the titles and subtitles using select to identify id's in the html
product_titles = colonna_soup.select('.product-card-title')
product_subtitles = colonna_soup.select('.product-card-subtitle')

#creating individual lists to store the information and a dictionary as an alternative

titles_list = []
titles_origin_list = []
#product_subtitles contains the origin and bean catergory for some of the beans and I need to split
#this information into different lists
bean_catergory = []

# for loop from 0 to length of product titles adding titles as the key and subtitles as the value in titles dictionary
titles_dict = {}
for i in range(0, len(product_titles)):
    titles_dict[product_titles[i].get_text()] = product_subtitles[i].get_text()


#trying more efficient way of extracting data found in the script tag within the html
#this data is already organised into catergories and can be easily accessed

#finding the script tag for a specific bean using the id
script_tag_LRR_019 = colonna_soup.find('script', id='pxl-product-card-7033499353173')
#if to check if the id is correct and if so creates 
if script_tag_LRR_019 is not None:
    #extracts content inside of the script tag as a string
    json_content_LRR_019 = script_tag_LRR_019.string
    #Converts data in a python dictionary
    data_LRR_019 = json.loads(json_content_LRR_019)
else:
    print("Script tag not found.")


product_title = data_LRR_019['product']['title']
print(product_title)
print(data_LRR_019)
print('hello')
