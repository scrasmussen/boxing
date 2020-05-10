import pandas as pd
import requests
import random
from sys import exit
from bs4 import BeautifulSoup
from tabulate import tabulate

# Saturday Fight Live (SFL)

event = ''
event = 'UFC_Fight_Night:_Hermansson_vs._Cannonier'

def check_boxing_columns(rows):
    total = 0
    for row in rows:
        switch =  {
            'No.': True,
            'Result': True,
            'Record': True,
            'Opponent': True,
            'Round, time': True,
            'Type': True,
            'Method': True,
            'Date': True,
            'Location': True
        }
        if (switch.get(row,False)):
            total += 1
    # print("total: " + str(total) )
    # print(rows)
    if (total > 7):
        print("Boxer")
        return True
    return False

def check_mma_columns(rows):
    total = 0
    for row in rows:
        switch =  {
            'Res.': True,
            'Record': True,
            'Opponent': True,
            'Method':    True,
            'Event': True,
            'Date': True,
            'Round': True,
            'Time': True,
            'Location': True
        }
        if (switch.get(row,False)):
            total += 1

    if (total > 8):
        print("MMA Fighter")
        return True
    return False

def getUrl(event):
    if (event == ''):
        print("No Event Selected")
        exit()
    event.replace(' ', '_')
    url = 'https://en.wikipedia.org/wiki/'
    url += event
    return url

# ----------------------------------------------------------------------------
#                                  START
# ----------------------------------------------------------------------------
req = requests.get(getUrl(event)).text
soup = BeautifulSoup(req, 'lxml')
# result = soup.find_all('table', {'class': 'wikitable'})
result = soup.find('table', {'class': 'toccolours'})
td = result.find_all('tr')
rows = [i.text.rstrip() for i in td]   # dont need this right now
table = pd.read_html(result.prettify())[0]

# Fix column names
column_names = [i[1] for i in table.columns]
column_names[1] = 'Fighter 1'
column_names[2] = 'vs.'
column_names[3] = 'Fighter 2'
table.columns = column_names

# Remove unwanted columns and change to 'vs.'
table = table.drop(['Method','Round','Time','Notes'], axis=1)
table['vs.'] = 'vs.'

# Randomly choose which fighter is where
for index, row in table.iterrows():
    x = row['Fighter 1']
    y = row['Fighter 2']
    if (random.choice([True,False])):
        row['Fighter 1'] = x
        row['Fighter 2'] = y
    else:
        row['Fighter 1'] = y
        row['Fighter 2'] = x


# split tables
has_prelim = table['Weight class'].str.contains("Preliminary")
prelim_row_i = list(has_prelim).index(True)
maincard = table.iloc[:prelim_row_i,:]
prelims  = table.iloc[prelim_row_i+1:,:]

print(tabulate([[event.replace('_',' ')]], tablefmt='psql'))
print(tabulate([["Maincard"]], tablefmt='psql'))
print(tabulate(maincard,headers='keys',tablefmt='psql',showindex=False))
print(tabulate([["Prelims"]], tablefmt='psql'))
print(tabulate(prelims,headers='keys',tablefmt='psql',showindex=False))
print("Fin")
