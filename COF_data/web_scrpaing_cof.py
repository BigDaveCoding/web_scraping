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

for i in range(0, len(clean_washed_headers)):
    costa_rica_dictionary[clean_washed_headers[i]] = []

for row in cr_table_washed.find_all('tr')[1:]:
    cells = row.find_all('td')
    for i, cell in enumerate(cells):
        cell_data = cell.find('div', class_='mtr-cell-content').get_text(strip=True)
        costa_rica_dictionary[clean_washed_headers[i]].append(cell_data)


print(costa_rica_dictionary)
