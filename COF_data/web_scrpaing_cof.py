import requests
from bs4 import BeautifulSoup
import csv
import json

costa_rica_2024_results_webpage = requests.get('https://allianceforcoffeeexcellence.org/costa-rica-2024/#coe-results')
costa_rica_2024_soup = BeautifulSoup(costa_rica_2024_results_webpage.content, 'html.parser')

costa_rica_dictionary = {}

# Find the table
cr_table_washed = costa_rica_2024_soup.find('table', class_='experimental mtr-table mtr-tr-td')

# # Extract the headers and clean
# washed_headers = [header.get_text(strip=True) for header in cr_table_washed.find('tr')]
# clean_washed_headers = [header for header in washed_headers if header != '']

# # add headers to dictionary
# for i in range(0, len(clean_washed_headers)):
#     costa_rica_dictionary[clean_washed_headers[i]] = []

def headers_for_dictionary(soup_table, dictionary):
    headers = [header.get_text(strip=True) for header in soup_table.find('tr')]
    clean = [header for header in headers if header != '']
    for i in range(0, len(clean)):
        dictionary[clean[i]] = []
    return clean


# Extract data and add to dictionary
# for row in cr_table_washed.find_all('tr')[1:]:
#     cells = row.find_all('td')
#     for i, cell in enumerate(cells):
#         cell_data = cell.find('div', class_='mtr-cell-content').get_text(strip=True)
#         costa_rica_dictionary[clean_washed_headers[i]].append(cell_data)

def extract_data_from_table(soup_table, headers, dictionary):
    for row in soup_table.find_all('tr')[1:]:
        cells = row.find_all('td')
        for i, cell in enumerate(cells):
            cell_data = cell.find('div', class_='mtr-cell-content').get_text(strip=True)
            dictionary[headers[i]].append(cell_data)
    return

washed_table_headers = headers_for_dictionary(cr_table_washed, costa_rica_dictionary)
extract_data_from_table(cr_table_washed, washed_table_headers, costa_rica_dictionary)


print(costa_rica_dictionary)
