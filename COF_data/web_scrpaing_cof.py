import requests
from bs4 import BeautifulSoup
import csv
import json

costa_rica_2024_results_webpage = requests.get('https://allianceforcoffeeexcellence.org/costa-rica-2024/#coe-results')
costa_rica_2024_soup = BeautifulSoup(costa_rica_2024_results_webpage.content, 'html.parser')

costa_rica_dictionary = {}
# cr_soup = costa_rica_2024_soup.find_all('div', '.mtr-cell-content')

cr_table_washed = costa_rica_2024_soup.find('table', class_='experimental mtr-table mtr-tr-td')
washed_headers = [header.get_text(strip=True) for header in cr_table_washed.find('tr')]
clean_washed_headers = [header for header in washed_headers if header != '']
print(clean_washed_headers)
# print(cr_table_washed)