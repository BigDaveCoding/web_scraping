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

def headers_for_dictionary(soup_table, dictionary):
    headers = [header.get_text(strip=True) for header in soup_table.find('tr')]
    clean = [header for header in headers if header != '']
    for i in range(0, len(clean)):
        dictionary[clean[i]] = []
    return clean



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

auction_washed_headers = headers_for_dictionary(cr_auction_table_washed, costa_rica_all_auction_data_dict)
extract_data_from_table(cr_auction_table_washed, auction_washed_headers, costa_rica_all_auction_data_dict)

# Removing value in list that is identical to the key. This is because of extracting data from all three tables at once rather than
# individually
for key, values in costa_rica_all_auction_data_dict.items():
    costa_rica_all_auction_data_dict[key] = [val for val in values if val != key]
# Dont need the company name data for the table so using .pop to remove key and values.
costa_rica_all_auction_data_dict.pop('COMPANY NAME')

def remove_invalid_data(_dictionary):
    for key, values in _dictionary.items():
        _dictionary[key] = [val for val in values if val != key]

# Adding a key 'COUNTRY' and value of 'Costa Rica' to auction dictionary

def add_table_dict_data(add_to_dictionary, key_list, data_list):
    for key, value in zip(key_list, data_list):
        if key not in add_to_dictionary:
            add_to_dictionary[key] = [value] * len(next(iter(add_to_dictionary.values())))
        else:
            add_to_dictionary[key].extend([value]) * len(next(iter(add_to_dictionary.values())))

add_table_dict_data(costa_rica_all_auction_data_dict, ['COUNTRY', 'YEAR'], ['Costa Rica', '2024'])
    

for key in costa_rica_washed_dictionary.keys():
    costa_rica_all_data_dict[key] = costa_rica_washed_dictionary[key] + costa_rica_experimental_dictionary[key] + costa_rica_natural_honey_dictionary[key]

add_table_dict_data(costa_rica_all_data_dict, ['CONTINENT', 'COUNTRY', 'YEAR'], ['North America (Central America)', 'Costa Rica', '2024'])

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

def write_csv_file(csv_file_title, _dictionary):
    with open(csv_file_title, 'w', newline = '') as csv_file:
        w = csv.DictWriter(csv_file, fieldnames=_dictionary.keys())
        w.writeheader()
        rows = [dict(zip(_dictionary.keys(), t)) for t in zip(*_dictionary.values())]
        w.writerows(rows)
    return

write_csv_file('costa_rica_auction_table.csv', costa_rica_all_auction_data_dict)

all_auction_df = pd.read_csv('costa_rica_auction_table.csv')
# print(all_auction_df)

all_cr_df = pd.read_csv('all_costa_rica_data_table.csv')
# print(all_cr_df)

df = pd.read_csv('costa_rica_washed_table.csv')
# print(df)

# print(costa_rica_all_auction_data_dict)

#using requests to get the webpage
el_salvador_results_webpage = requests.get('https://allianceforcoffeeexcellence.org/el-salvador-2024/')
# Turning webpage into Soup using html.parser
el_salvador_soup = BeautifulSoup(el_salvador_results_webpage.content, 'html.parser')

# Initializing dictionaires to store the data in
el_salvador_all_results_dict = {}
el_salvador_all_auction_dict = {}

# Finding tables
el_salvador_results_table = el_salvador_soup.find('div', id='coe-results')
el_salvador_auction_table = el_salvador_soup.find('div', id='coe-auction-results')

# Getting headers to store in the Key of dictionaries
es_results_headers = headers_for_dictionary(el_salvador_results_table, el_salvador_all_results_dict)
es_auction_headers = headers_for_dictionary(el_salvador_auction_table, el_salvador_all_auction_dict)

# extracting data from tables to store in values of dictionaries
extract_data_from_table(el_salvador_results_table, es_results_headers, el_salvador_all_results_dict)
extract_data_from_table(el_salvador_auction_table, es_auction_headers, el_salvador_all_auction_dict)

# Removing invalid values
remove_invalid_data(el_salvador_all_results_dict)
remove_invalid_data(el_salvador_all_auction_dict)

# Removing 'COMPANY NAME' Key:value from auction dictionary
el_salvador_all_auction_dict.pop('COMPANY NAME')

# Adding extra data to tables
add_table_dict_data(el_salvador_all_results_dict, ['CONTINENT', 'COUNTRY', 'YEAR'], ['North America (Central America)', 'El Salvador', '2024'])
add_table_dict_data(el_salvador_all_auction_dict, ['COUNTRY', 'YEAR'], ['El Salvador', '2024'])

# Writing data to csv file

write_csv_file('el_salvador_results_table_2024.csv', el_salvador_all_results_dict)
write_csv_file('el_salvador_auction_results_2024.csv', el_salvador_all_auction_dict)

# print(el_salvador_all_results_dict) #Debugging
# print(el_salvador_all_auction_dict) #Debugging