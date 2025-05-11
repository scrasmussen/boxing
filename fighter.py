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
    if (fighter == 'Manny_Pacquiao'):
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

        # tables = div.find_next_sibling('table', class_='wikitable', style=lambda s: s and 'text-align:center' in s)
        tables = div.find_next(lambda tag: tag.name == "table" and tag.get("class") == ["wikitable"])

        if not None:
            return tables

    return None

def getRecord(soup, record_type, debug=False):
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
    legal_headers = ['Res.', 'Result', 'Record', 'Opponent', 'Method',
                     'Event', 'Date', 'Round', 'Time', 'Location', 'Notes']
    headers = [header for header in headers if header in legal_headers]

    rows = []
    for row in table.find_all('tr')[1:]:  # Skip the header row
        cols = row.find_all('td')
        cols = [col.get_text(strip=True) for col in cols]
        rows.append(cols)

    record = pd.DataFrame(rows, columns=headers)
    record = record[columns]
    record.loc[:,'Date'] = pd.to_datetime(record['Date'], errors='coerce').dt.strftime('%m.%d.%Y')
    record = record[~((record['Opponent'].isna()) &
                      (record['Event'].isna()) &
                      (record['Date'].isna()))]

    # fix for when dates or names are over several columns
    for i, row in record.iterrows():
        if row['Event'] == '1' and pd.isna(row['Date']):
            row['Event'] = record.loc[i-1, 'Event']
            row['Date'] = record.loc[i-1, 'Date']
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

    def replace_b_with_boxer(self, name):
        if name.endswith("(b)"):
            return name[:-3] + "(boxer)"
        return name

    def __init__(self, name, debug=False):
        name = self.replace_b_with_boxer(name)
        self.name = name.replace('_',' ').title()
        req = requests.get(getUrl(name.replace(' ', '_'), debug)).text
        soup = BeautifulSoup(req, 'lxml')

        self.mma_record = getRecord(soup, 'mma', debug)
        self.boxing_record = getRecord(soup, 'boxing', debug)
        self.kickboxing_record = getRecord(soup, 'kickboxing', debug)
