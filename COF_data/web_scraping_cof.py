import requests
from bs4 import BeautifulSoup
import csv
import json
import pandas as pd

# costa_rica_2024_results_webpage = requests.get('https://allianceforcoffeeexcellence.org/costa-rica-2024/#coe-results')
# costa_rica_2024_soup = BeautifulSoup(costa_rica_2024_results_webpage.content, 'html.parser')

# costa_rica_all_data_dict = {}
# costa_rica_all_auction_data_dict = {}

# costa_rica_washed_dictionary = {}
# costa_rica_experimental_dictionary = {}
# costa_rica_natural_honey_dictionary = {}

# # Find the table for results
# cr_table_washed = costa_rica_2024_soup.find('table', class_='experimental mtr-table mtr-tr-td')
# cr_table_experimental = costa_rica_2024_soup.find('table', class_='redd mtr-table mtr-tr-td')
# cr_table_natural_honey = costa_rica_2024_soup.find('table', class_='dry mtr-table mtr-tr-td')

# #Find the table for auction results
# cr_auction_table_washed = costa_rica_2024_soup.find('div', id='coe-auction-results')

# # print(cr_auction_table_washed)

# def headers_for_dictionary(soup_table, dictionary):
#     headers = [header.get_text(strip=True) for header in soup_table.find('tr')]
#     clean = [header for header in headers if header != '']
#     for i in range(0, len(clean)):
#         dictionary[clean[i]] = []
#     return clean



# def extract_data_from_table(soup_table, headers, dictionary):
#     for row in soup_table.find_all('tr')[1:]:
#         cells = row.find_all('td')
#         for i, cell in enumerate(cells):
#             cell_data = cell.find('div', class_='mtr-cell-content').get_text(strip=True)
#             dictionary[headers[i]].append(cell_data)
#     return

# washed_table_headers = headers_for_dictionary(cr_table_washed, costa_rica_washed_dictionary)
# extract_data_from_table(cr_table_washed, washed_table_headers, costa_rica_washed_dictionary)

# experimental_table_headers = headers_for_dictionary(cr_table_experimental, costa_rica_experimental_dictionary)
# extract_data_from_table(cr_table_experimental, experimental_table_headers, costa_rica_experimental_dictionary)

# natural_honey_headers = headers_for_dictionary(cr_table_natural_honey, costa_rica_natural_honey_dictionary)
# extract_data_from_table(cr_table_natural_honey, natural_honey_headers, costa_rica_natural_honey_dictionary)

# auction_washed_headers = headers_for_dictionary(cr_auction_table_washed, costa_rica_all_auction_data_dict)
# extract_data_from_table(cr_auction_table_washed, auction_washed_headers, costa_rica_all_auction_data_dict)

# # Removing value in list that is identical to the key. This is because of extracting data from all three tables at once rather than
# # individually
# for key, values in costa_rica_all_auction_data_dict.items():
#     costa_rica_all_auction_data_dict[key] = [val for val in values if val != key]
# # Dont need the company name data for the table so using .pop to remove key and values.
# costa_rica_all_auction_data_dict.pop('COMPANY NAME')

# def remove_invalid_data(_dictionary):
#     for key, values in _dictionary.items():
#         _dictionary[key] = [val for val in values if val != key]

# # Adding a key 'COUNTRY' and value of 'Costa Rica' to auction dictionary

# def add_table_dict_data(add_to_dictionary, key_list, data_list):
#     for key, value in zip(key_list, data_list):
#         if key not in add_to_dictionary:
#             add_to_dictionary[key] = [value] * len(next(iter(add_to_dictionary.values())))
#         else:
#             add_to_dictionary[key].extend([value]) * len(next(iter(add_to_dictionary.values())))

# add_table_dict_data(costa_rica_all_auction_data_dict, ['COUNTRY', 'YEAR'], ['Costa Rica', '2024'])
    

# for key in costa_rica_washed_dictionary.keys():
#     costa_rica_all_data_dict[key] = costa_rica_washed_dictionary[key] + costa_rica_experimental_dictionary[key] + costa_rica_natural_honey_dictionary[key]

# add_table_dict_data(costa_rica_all_data_dict, ['CONTINENT', 'COUNTRY', 'YEAR'], ['North America (Central America)', 'Costa Rica', '2024'])

# with open('costa_rica_washed_table.csv', 'w', newline = '') as cr_table_washed:
#     w = csv.DictWriter(cr_table_washed, fieldnames = costa_rica_washed_dictionary.keys())
#     w.writeheader()
#     rows = [dict(zip(costa_rica_washed_dictionary.keys(), t)) for t in zip(*costa_rica_washed_dictionary.values())]
#     w.writerows(rows)

# with open('all_costa_rica_data_table.csv', 'w', newline='') as all_cr_data:
#     w = csv.DictWriter(all_cr_data, fieldnames=costa_rica_all_data_dict.keys())
#     w.writeheader()
#     rows = [dict(zip(costa_rica_all_data_dict.keys(), t)) for t in zip(*costa_rica_all_data_dict.values())]
#     w.writerows(rows)

# def write_csv_file(csv_file_title, _dictionary):
#     with open(csv_file_title, 'w', newline = '') as csv_file:
#         w = csv.DictWriter(csv_file, fieldnames=_dictionary.keys())
#         w.writeheader()
#         rows = [dict(zip(_dictionary.keys(), t)) for t in zip(*_dictionary.values())]
#         w.writerows(rows)
#     return

# write_csv_file('costa_rica_auction_table.csv', costa_rica_all_auction_data_dict)

# all_auction_df = pd.read_csv('costa_rica_auction_table.csv')
# # print(all_auction_df)

# all_cr_df = pd.read_csv('all_costa_rica_data_table.csv')
# # print(all_cr_df)

# df = pd.read_csv('costa_rica_washed_table.csv')
# # print(df)

# # print(costa_rica_all_auction_data_dict)

# #using requests to get the webpage
# el_salvador_results_webpage = requests.get('https://allianceforcoffeeexcellence.org/el-salvador-2024/')
# # Turning webpage into Soup using html.parser
# el_salvador_soup = BeautifulSoup(el_salvador_results_webpage.content, 'html.parser')

# # Initializing dictionaires to store the data in
# el_salvador_all_results_dict = {}
# el_salvador_all_auction_dict = {}

# # Finding tables
# el_salvador_results_table = el_salvador_soup.find('div', id='coe-results')
# el_salvador_auction_table = el_salvador_soup.find('div', id='coe-auction-results')

# # Getting headers to store in the Key of dictionaries
# es_results_headers = headers_for_dictionary(el_salvador_results_table, el_salvador_all_results_dict)
# es_auction_headers = headers_for_dictionary(el_salvador_auction_table, el_salvador_all_auction_dict)

# # extracting data from tables to store in values of dictionaries
# extract_data_from_table(el_salvador_results_table, es_results_headers, el_salvador_all_results_dict)
# extract_data_from_table(el_salvador_auction_table, es_auction_headers, el_salvador_all_auction_dict)

# # Removing invalid values
# remove_invalid_data(el_salvador_all_results_dict)
# remove_invalid_data(el_salvador_all_auction_dict)

# # Removing 'COMPANY NAME' Key:value from auction dictionary
# el_salvador_all_auction_dict.pop('COMPANY NAME')

# # Adding extra data to tables
# add_table_dict_data(el_salvador_all_results_dict, ['CONTINENT', 'COUNTRY', 'YEAR'], ['North America (Central America)', 'El Salvador', '2024'])
# add_table_dict_data(el_salvador_all_auction_dict, ['COUNTRY', 'YEAR'], ['El Salvador', '2024'])

# # Writing data to csv file

# write_csv_file('el_salvador_results_table_2024.csv', el_salvador_all_results_dict)
# write_csv_file('el_salvador_auction_results_2024.csv', el_salvador_all_auction_dict)

# # print(el_salvador_all_results_dict) #Debugging
# # print(el_salvador_all_auction_dict) #Debugging
class Extract_All_Data:
    def __init__(self, webpage_to_scrape_str, id_str, csv_str):
        self.webpage_to_scrape_str = webpage_to_scrape_str
        self.data_dictionary = {}
        self.id_str = id_str
        self.csv_str = csv_str
    
    def __repr__(self):
        return 'Created a class in order to run through the functions to scrape the data from the tables of the different Cup Of Excellence \
            results and auctions found throughout the website.'
    
    def create_soup(self):
        webpage = requests.get(self.webpage_to_scrape_str)
        soup = BeautifulSoup(webpage.content, 'html.parser')
        return soup
    
    def find_table(self, soup):
        table = soup.find('div', id=self.id_str)
        return table
    
    def assign_headers(self, soup_table):
        headers = []
        header_row = soup_table.find('tr')
        if header_row:
            headers = [header.get_text(strip=True) for header in header_row.find_all(['th', 'td'])]
            for header in headers:
                self.data_dictionary[header] = []
        return headers
    
    def extract_data_from_table(self, soup_table, headers):
        rows = soup_table.find_all('tr')[1:]  # Skip header row
        for row in rows:
            cells = row.find_all('td')
            for i, cell in enumerate(cells):
                cell_data = cell.get_text(strip=True)
                if i < len(headers):  # Ensure cell aligns with a header
                    self.data_dictionary[headers[i]].append(cell_data)
    
    def clean_dictionary(self):
        for key, value in self.data_dictionary.items():
            self.data_dictionary[key] = [val for val in value if val != key]
        if self.id_str == 'coe-auction-results':
            self.data_dictionary.pop('COMPANY NAME')
        
    def add_extra_data(self, key_list, value_list):
        if key_list == [] and value_list == []:
            return
        for key, value in zip(key_list, value_list):
            if key not in self.data_dictionary:
                self.data_dictionary[key] = [value] * len(next(iter(self.data_dictionary.values())))
            else:
                self.data_dictionary[key].extend([value]) * len(next(iter(self.data_dictionary.values())))

    def write_to_csv(self):
        with open(self.csv_str, 'w', newline = '') as file:
            w = csv.DictWriter(file, fieldnames=self.data_dictionary.keys())
            w.writeheader()
            rows = [dict(zip(self.data_dictionary.keys(), t)) for t in zip(*self.data_dictionary.values())]
            w.writerows(rows)
    
    def scrape(self, key_list, value_list):
        soup = self.create_soup()
        table = self.find_table(soup)
        if table:
            headers = self.assign_headers(table)
            if headers:
                self.extract_data_from_table(table, headers)
        self.clean_dictionary()
        self.add_extra_data(key_list, value_list)
        self.write_to_csv()
        return self.data_dictionary

    
guatemala_data = Extract_All_Data('https://allianceforcoffeeexcellence.org/guatemala-2024/#coe-results', 'coe-results', 'guatemala_results_table_2024.csv')
guatemala_results = guatemala_data.scrape(['COUNTRY', 'CONTINENT', 'YEAR'], ['Guatemala', 'North America (Central America)', '2024'])
guatemala_auction_data = Extract_All_Data('https://allianceforcoffeeexcellence.org/guatemala-2024/', 'coe-auction-results', 'guatemala_auction_table_2024.csv')
guatemala_auction_results = guatemala_auction_data.scrape(['COUNTRY', 'YEAR'],['Guatemala', '2024'])

el_salvador_data = Extract_All_Data('https://allianceforcoffeeexcellence.org/el-salvador-2024/', 'coe-results', 'el_salvador_results_table_2024.csv')
el_salvador_results = el_salvador_data.scrape(['COUNTRY', 'CONTINENT', 'YEAR'], ['El Salvador', 'North America (Central America)', '2024'])
el_salvador_auction_data = Extract_All_Data('https://allianceforcoffeeexcellence.org/el-salvador-2024/', 'coe-auction-results', 'el_salvador_auction_results_2024.csv')
el_salvador_auction_results = el_salvador_auction_data.scrape(['COUNTRY', 'YEAR'], ['El Salvador', '2024'])

costa_rica_data = Extract_All_Data('https://allianceforcoffeeexcellence.org/costa-rica-2024/', 'coe-results', 'costa_rica_results_table_2024.csv')
costa_rica_results = costa_rica_data.scrape(['COUNTRY', 'CONTINENT', 'YEAR'], ['Costa Rica', 'North America (Central America)', '2024'])
costa_rica_auction_data = Extract_All_Data('https://allianceforcoffeeexcellence.org/costa-rica-2024/', 'coe-auction-results', 'costa_rica_auction_table_2024.csv')
costa_rica_auction_results = costa_rica_auction_data.scrape(['COUNTRY', 'YEAR'], ['Costa Rica', '2024'])

# print(guatemala_auction_results) # Debugging