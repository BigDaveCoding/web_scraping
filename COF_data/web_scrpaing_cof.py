import requests
from bs4 import BeautifulSoup
import csv
import json

costa_rica_2024_results_webpage = requests.get('https://allianceforcoffeeexcellence.org/costa-rica-2024/#coe-results')
costa_rica_2024_soup = BeautifulSoup(costa_rica_2024_results_webpage.content, 'html.parser')

costa_rica_dictionary = {}
# cr_soup = costa_rica_2024_soup.find_all('div', '.mtr-cell-content')

# Find the table
cr_table_washed = costa_rica_2024_soup.find('table', class_='experimental mtr-table mtr-tr-td')

# Extract the headers and clean
washed_headers = [header.get_text(strip=True) for header in cr_table_washed.find('tr')]
clean_washed_headers = [header for header in washed_headers if header != '']
# print(clean_washed_headers)

washed_data = cr_table_washed.find('tbody').find_all('td')[1:]
data = []

for row in washed_data:
    cells = row.find_all('td')
    row_data = [cell.get_text() for cell in cells]
    data.append(row_data)
print(data)

for i in range(0, len(clean_washed_headers)):
    costa_rica_dictionary[clean_washed_headers[i]] = []

# print(costa_rica_dictionary)
