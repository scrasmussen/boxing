import pandas as pd
from bs4 import BeautifulSoup
from tabulate import tabulate
import requests

# -- Boxers --
fighter = 'Floyd_Mayweather_Jr.'
fighter = 'Daniel_Dubois_(boxer)'
fighter = 'Murat_Gassiev'
fighter = 'Vasyl_Lomachenko'
fighter = 'Errol_Spence_Jr.'
fighter = 'Rom%C3%A1n_Gonz%C3%A1lez_(boxer)' # chocolatito


# -- MMA --
fighter = 'Alexander_Gustafsson'
fighter = 'Marlon_Moraes'
fighter = 'Petr_Yan'
fighter = 'Frankie_Edgar'
fighter = 'Lyoto_Machida'
fighter = 'Arnold_Allen_(fighter)'
fighter = 'Felicia_Spencer' # leg tied up but still jumps to knee opponent!
fighter = 'Diego_Sanchez'

fighter = 'Andre_Ward'
fighter = 'Buster_Douglas'
# fighter = 'Mike_Tyson'
# fighter = 'Josh_Warrington'
# fighter = 'Bernard_Hopkins'
fighter = 'Lyoto_Machida'
fighter = 'Song_Yadong'



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


url = 'https://en.wikipedia.org/wiki/'
url += fighter
# req = open('floyd_wiki.html','r').read()
req = requests.get(url).text

soup = BeautifulSoup(req, 'lxml')
result = soup.find_all('table', {'class': 'wikitable'})

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
        q.insert(0, '', list(range(len(q.index),0,-1)))
        new_date = pd.to_datetime(q['Date']).dt.strftime('%m.%d.%Y')
        q.loc[:,'Date'] = new_date
        shorten_lambda = lambda x: x[0:x.find(':')] if (x.find(':')>0) else x
        q.loc[:,'Event'] = q[['Event']].applymap(shorten_lambda)


print(tabulate([[fighter.replace('_',' ')]], tablefmt='psql'))
print(tabulate(q,headers='keys',tablefmt='psql',showindex=False))
print("Fin")
