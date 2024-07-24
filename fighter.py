from bs4 import BeautifulSoup
from io import StringIO
from tabulate import tabulate
import pandas as pd
import requests
import re
import sys

def getUrl(fighter, debug=False):
    if (fighter == ''):
        print("No Fighter Selected")
        exit()
    url = 'https://en.wikipedia.org/wiki/'
    url += fighter.title().replace('(Boxer)','(boxer)')
    if (fighter == 'Manny Pacquiao'):
        url = url.removesuffix(fighter)
        url += 'Boxing career of Manny Pacquiao'
    if (debug):
        print("url =", url)
    return url

def find_table_after_header(soup, header_id):
    divs = soup.find_all('div', class_='mw-heading mw-heading2')

    for div in divs:
        header = div.find('h2', id=header_id)
        if header is None:
            continue

        tables = div.find_next_sibling('table', class_='wikitable', style=lambda s: s and 'text-align:center' in s)

        if not None:
            return tables

    return None

def get_record(soup, record_type, debug=False):
    if (record_type == 'boxing'):
        columns = ['No.', 'Opponent', 'Date']
        record_name = 'Professional_boxing_record'
    if (record_type == 'kickboxing'):
        columns = ['Opponent', 'Event', 'Date']
        record_name = 'Kickboxing_record'
    if (record_type == 'mma'):
        columns = ['Opponent', 'Event', 'Date']
        record_name = 'Mixed_martial_arts_record'

    table = find_table_after_header(soup, record_name)
    if table is None:
        if debug:
            print('table is None for record_name', record_name)
        return None

    headers = [header.get_text(strip=True) for header in table.find_all('th')]

    rows = []
    for row in table.find_all('tr')[1:]:  # Skip the header row
        cols = row.find_all('td')
        cols = [col.get_text(strip=True) for col in cols]
        rows.append(cols)

    record = pd.DataFrame(rows, columns=headers)
    record = record[columns]
    record.loc[:,'Date'] = pd.to_datetime(record['Date']).dt.strftime('%m.%d.%Y')

    return record

class Fighter:
    def print_name(self):
        print(tabulate([[self.name]], tablefmt='psql'))
    def print_records(self):
        records = [self.mma_record, self.boxing_record, self.kickboxing_record]
        for record in records:
            if (record is not None):
                print(tabulate(record,headers='keys',tablefmt='psql',
                               showindex=False))

    def __init__(self, name):
        self.name = name.replace('_',' ').title()
        req = requests.get(getUrl(name.replace(' ', '_'))).text
        soup = BeautifulSoup(req, 'lxml')

        self.mma_record = get_record(soup, 'mma')
        self.boxing_record = get_record(soup, 'boxing')
        self.kickboxing_record = get_record(soup, 'kickboxing')
