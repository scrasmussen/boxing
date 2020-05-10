import pandas as pd
import requests
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
column_names = [i[1] for i in table.columns]
table.columns = column_names

# split tables
has_prelim = table['Weight class'].str.contains("Preliminary")
prelim_row_i = list(has_prelim).index(True)
maincard = table.iloc[:prelim_row_i,:]
prelims  = table.iloc[prelim_row_i+1:,:]
# q = pd.read_html(result.prettify())
exit()

 # this will read too much stuff in || pd.read_html(soup.prettify())

for res in result:
    tr = res.find('tr')
    td = tr.find_all('th')
    rows = [i.text.rstrip() for i in td]
    # print(rows)
    if (check_boxing_columns(rows)):
        table = pd.read_html(res.prettify())[0]
        q = table[['No.', 'Opponent', 'Date']]
    elif (check_mma_columns(rows)):
        table = pd.read_html(res.prettify())[0]
        q = table[['Opponent', 'Event', 'Date']].copy().dropna()
        # q.insert(0, '', list(range(len(q.index),0,-1)))
        # new_date = pd.to_datetime(q['Date']).dt.strftime('%m.%d.%Y')
        # q.loc[:,'Date'] = new_date
        # shorten_lambda = lambda x: x[0:x.find(':')] if (x.find(':')>0) else x
        # q.loc[:,'Event'] = q[['Event']].applymap(shorten_lambda)


# print(tabulate([[event.replace('_',' ')]], tablefmt='psql'))
# print(tabulate(q,headers='keys',tablefmt='psql',showindex=False))
print("Fin")