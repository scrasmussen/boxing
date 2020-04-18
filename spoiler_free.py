import pandas as pd
from bs4 import BeautifulSoup
from tabulate import tabulate
import requests


print("start")

def check_columns(rows):
    total = 0
    for row in rows:
        switch =  {
            'Result': True,
            'Res.':    True,
            'Record': True,
            'Opponent': True,
            'Type': True,
            'Method': True,
            'Date': True,
            'Location': True
        }
        if (switch.get(row,False)):
            total += 1
    if (total > 5):
        return True
    return False


url = 'https://en.wikipedia.org/wiki/'
fighter = 'Floyd_Mayweather_Jr.'
fighter = 'Lawrence_Okolie'
# fighter = 'Murat_Gassiev'
# fighter = 'Alexander_Gustafsson'

url += fighter

# req = open('full_floyd_wiki.html','r').read()
req = requests.get(url).text

soup = BeautifulSoup(req, 'lxml')
result = soup.find_all('table', {'class': 'wikitable'})

for res in result:
    # print(res)
    tr = res.find('tr')
    td = tr.find_all('th')
    rows = [i.text.rstrip() for i in td]
    if (check_columns(rows)):
        table = pd.read_html(res.prettify())[0]
        q = table[['No.', 'Opponent', 'Date']]

print(tabulate(q,headers='keys',tablefmt='psql',showindex=False))
print("Fin")
