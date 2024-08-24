import requests
from bs4 import BeautifulSoup
import csv
import json
import pandas as pd

costa_rica_2024_results_webpage = requests.get('https://allianceforcoffeeexcellence.org/costa-rica-2024/#coe-results')
costa_rica_2024_soup = BeautifulSoup(costa_rica_2024_results_webpage.content, 'html.parser')

costa_rica_all_data_dict = {}
costa_rica_all_auction_data_dict = {}

costa_rica_washed_dictionary = {}
costa_rica_experimental_dictionary = {}
costa_rica_natural_honey_dictionary = {}

# Find the table for results
cr_table_washed = costa_rica_2024_soup.find('table', class_='experimental mtr-table mtr-tr-td')
cr_table_experimental = costa_rica_2024_soup.find('table', class_='redd mtr-table mtr-tr-td')
cr_table_natural_honey = costa_rica_2024_soup.find('table', class_='dry mtr-table mtr-tr-td')

#Find the table for auction results
cr_auction_table_washed = costa_rica_2024_soup.find('div', id='coe-auction-results')

# print(cr_auction_table_washed)



# print(cr_table_washed)


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

auction_washed_headers = headers_for_dictionary(cr_auction_table_washed, costa_rica_all_auction_data_dict)



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

washed_table_headers = headers_for_dictionary(cr_table_washed, costa_rica_washed_dictionary)
extract_data_from_table(cr_table_washed, washed_table_headers, costa_rica_washed_dictionary)

experimental_table_headers = headers_for_dictionary(cr_table_experimental, costa_rica_experimental_dictionary)
extract_data_from_table(cr_table_experimental, experimental_table_headers, costa_rica_experimental_dictionary)

natural_honey_headers = headers_for_dictionary(cr_table_natural_honey, costa_rica_natural_honey_dictionary)
extract_data_from_table(cr_table_natural_honey, natural_honey_headers, costa_rica_natural_honey_dictionary)


extract_data_from_table(cr_auction_table_washed, auction_washed_headers, costa_rica_all_auction_data_dict)

# Removing value in list that is identical to the key. This is because of extracting data from all three tables at once rather than
# individually
for key, values in costa_rica_all_auction_data_dict.items():
    costa_rica_all_auction_data_dict[key] = [val for val in values if val != key]
# Dont need the company name data for the table so using .pop to remove key and values.
costa_rica_all_auction_data_dict.pop('COMPANY NAME')

# Adding a key 'COUNTRY' and value of 'Costa Rica' to auction dictionary

def add_table_dict_data(add_to_dictionary, key_list, data_list):
    for key, value in zip(key_list, data_list):
        if key not in add_to_dictionary:
            add_to_dictionary[key] = [value] * len(next(iter(add_to_dictionary.values())))
        else:
            add_to_dictionary[key].extend([value]) * len(next(iter(add_to_dictionary.values())))

add_table_dict_data(costa_rica_all_auction_data_dict, ['COUNTRY', 'YEAR'], ['Costa Rica', '2024'])
    

# costa_rica_all_auction_data_dict['COUNTRY'] = ['Costa Rica'] * len(next(iter(costa_rica_all_auction_data_dict.values())))
# costa_rica_all_auction_data_dict['YEAR'] = ['2024']


for key in costa_rica_washed_dictionary.keys():
    costa_rica_all_data_dict[key] = costa_rica_washed_dictionary[key] + costa_rica_experimental_dictionary[key] + costa_rica_natural_honey_dictionary[key]

costa_rica_all_data_dict['COUNTRY'] = ['Costa Rica'] * len(next(iter(costa_rica_all_data_dict.values())))
costa_rica_all_data_dict['YEAR'] = ['2024'] * len(next(iter(costa_rica_all_data_dict.values())))

# print(costa_rica_all_data_dict)
# print(costa_rica_washed_dictionary)
# print(costa_rica_experimental_dictionary)
# print(costa_rica_natural_honey_dictionary)

with open('costa_rica_washed_table.csv', 'w', newline = '') as cr_table_washed:
    w = csv.DictWriter(cr_table_washed, fieldnames = costa_rica_washed_dictionary.keys())
    w.writeheader()
    rows = [dict(zip(costa_rica_washed_dictionary.keys(), t)) for t in zip(*costa_rica_washed_dictionary.values())]
    w.writerows(rows)

with open('all_costa_rica_data_table.csv', 'w', newline='') as all_cr_data:
    w = csv.DictWriter(all_cr_data, fieldnames=costa_rica_all_data_dict.keys())
    w.writeheader()
    rows = [dict(zip(costa_rica_all_data_dict.keys(), t)) for t in zip(*costa_rica_all_data_dict.values())]
    w.writerows(rows)

all_cr_df = pd.read_csv('all_costa_rica_data_table.csv')
# print(all_cr_df)

df = pd.read_csv('costa_rica_washed_table.csv')
# print(df)

print(costa_rica_all_auction_data_dict)