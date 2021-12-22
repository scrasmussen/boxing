from bs4 import BeautifulSoup
from tabulate import tabulate
import pandas as pd
import requests
import re
import sys

def getUrl(fighter):
    if (fighter == ''):
        print("No Fighter Selected")
        exit()
    url = 'https://en.wikipedia.org/wiki/'
    url += fighter.title()
    return url

def get_record(soup, record_type):
    if (record_type == 'boxing'):
        columns = ['No.', 'Opponent', 'Date']
        record_name = 'Professional boxing record'
    if (record_type == 'kickboxing'):
        columns = ['Opponent', 'Event', 'Date']
        record_name = 'Kickboxing record'
    if (record_type == 'mma'):
        columns = ['Opponent', 'Event', 'Date']
        record_name = 'Mixed martial arts record'

    headers = soup.select_one('h2:-soup-contains("'+record_name+'")')

    if (headers is None):
        return None

    if (record_type in ['mma', 'boxing']):
        h_table = headers.find_next_sibling()
        row = h_table.find_next_sibling()
        row_text = row.get_text()
        # breakpoint()

    if (record_type == 'kickboxing'):
        kickboxing_columns = ['Date','Result','Opponent','Event','Location',
                              'Method','Round','Time','Record']
        h_table = headers.find_next_sibling()

        # working for Badr Hari, maybe others?
        row = headers.find_next_sibling()
        row_text = row.get_text()

    # print("ARTLESS")
    # print(row_text)
    if ('Record' in row_text) and ('Opponent' in row_text):
        table = pd.read_html(row.prettify())[0]
        if (record_type == 'kickboxing'):
            table.columns = kickboxing_columns
            table = table[2:]
            print(table)
        record = table[columns].copy().dropna()

        # fix date
        if (record_type != 'kickboxing'):
            new_date = pd.to_datetime(record['Date']).dt.strftime('%m.%d.%Y')
            record.loc[:,'Date'] = new_date
        else:
            drop_index = record[record.Event == record.Date].index
            record.drop(drop_index, inplace=True)
            # --- HACK --- to fix, kickboxing and MMA records in same table
            drop_index = record[record.Date == 'Date'].index
            record.drop(drop_index, inplace=True)

            new_date = pd.to_datetime(record['Date']).dt.strftime('%m.%d.%Y')
            record.loc[:,'Date'] = new_date
            # print(record)


        if (record_type in ['mma', 'kickboxing']):
            record.insert(0, '', list(range(len(record.index),0,-1)))
            # shorten event name
            shorten_lambda = lambda x: x[0:x.find(':')] \
                if (x.find(':')>0) else x
            record.loc[:,'Event'] = record[['Event']].applymap(shorten_lambda)

            max_len = 54
            max_opponent = record.Opponent.str.len().max()
            max_event = record.Event.str.len().max()
            if (max_len < max_opponent + max_event):
                width = max_len - max_opponent
                e = record.Event.replace("(.{"+str(width)+"})", "\\1-\n",
                                         regex=True)
                e = e.replace("\s+-\n|-\n\s+","\n",regex=True)
                record.Event = e.replace("-$","",regex=True)

        return record
    return None

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

        req = requests.get(getUrl(name)).text
        soup = BeautifulSoup(req, 'lxml')

        self.mma_record = get_record(soup, 'mma')
        self.boxing_record = get_record(soup, 'boxing')
        self.kickboxing_record = get_record(soup, 'kickboxing')
