import pandas as pd
from bs4 import BeautifulSoup
from tabulate import tabulate
import requests

# Saturday Fight Live (SFL)

# -- Boxers --
fighter = 'Floyd Mayweather Jr.'
fighter = 'Timothy Bradley'
fighter = 'Murat Gassiev'                    #  eventually; on DAZN
# Joshua vs Ruiz Jr.                         #  06.01.2019 DAZN, SFL
# Ortiz Jr. vs Herrera                       #  05.04.2019 DAZN, SFL
fighter = 'Amir Khan (boxer)'                #  04.20.2019 vs Crawford, EPSN
fighter = 'Gervonta Davis'                   #  02.09.2019 # fun, powerful
fighter = 'Adrian Broner'                    #  01.19.2019
fighter = 'Jermall Charlo'                   #  12.22.2018
fighter = 'Jarrett Hurd'                     #  12.01.2018 PBC
fighter = 'Oleksandr Usyk'                   #  11.10.2018
fighter = 'Maciej Sulecki'                   #  11.10.2018
fighter = 'Daniel Jacobs (boxer)'            #  10.27.2018
fighter = 'Canelo Álvarez'                   #  09.15.2018 DAZN ?
fighter = 'Rom%C3%A1n_Gonz%C3%A1lez_(boxer)' #  09.15.2018  # chocolatito
fighter = 'José Ramírez (boxer)'             #  09.14.2018
fighter = 'Amir Khan (boxer)'                #  09.08.2018 vs Samual Vargas
fighter = 'Mikey Garcia'                     #  07.28.2018 PBC
fighter = 'Boxing career of Manny Pacquiao'  #  07.15.2018
fighter = 'Regis Prograis'                   #  07.14.2018
fighter = 'Daniel Dubois (boxer)'            #  06.23.2018
fighter = 'Errol Spence Jr.'                 #  06.16.2018 PBC
fighter = 'Daniyar Yeleussinov'    # 06.06.2018, 09.13.2019 on DAZN
# Okolie vs. Watkins                         #  06.06.2018 DAZN
fighter = 'Vergil Ortiz Jr.'                 #  05.23.2019 DAZN ?
fighter = 'Josh Warrington'                  #  05.19.2018
# Stevenson vs Jack, Russell vs Diaz         #  05.19.2018 PBC
fighter = 'Vasyl Lomachenko'                 #  05.12.2018
# Mungula vs. Ali                            #  05.12.2018 DAZN
fighter = 'Gennady Golovkin'                 #  05.05.2018
# Bellow vs Haye 2,  Buatsi vs. Cuevas       #  05.05.2018 DAZN


# -- MMA --
fighter = 'Alexander Gustafsson'    # Retired
 # leg tied up but still jumps to knee opponent!
fighter = 'Felicia Spencer'         #  02.29.2020  UFC Fight Night
fighter = 'Diego Sanchez'           #  02.15.2020  UFC Fight Night
fighter = 'Arnold Allen (fighter)'  #  01.14.2020  UFC Fight Night
fighter = 'Frankie Edgar'           #  12.21.2019  UFC Fight Night
fighter = 'Colby Covington'         #  12.14.2019  UFC 245
fighter = 'Marlon Moraes'           #  12.14.2019  UFC 245
fighter = 'Petr Yan'                #  12.14.2019  UFC 245
fighter = 'Song Yadong'             #  12.07.2019  UFC on ESPN
fighter = 'Jorge Masvidal'          #  11.02.2019  UFC 244
                                    #  UFC Fight Night: Andrade vs. Zhang 13:45

# -- Currently Watching ---
# Boxing April 2018 || MMA August 2019
fighter = 'Lyoto Machida'           # Bellator, past @ UFC 67 02.03.2007
fighter = 'Andre Ward'
fighter = 'Buster Douglas'
fighter = 'Mike Tyson'
fighter = 'Bernard Hopkins'
fighter = ''



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


def getUrl(fighter):

    fighter.replace(" ", "_")
    url = 'https://en.wikipedia.org/wiki/'
    url += fighter
    return url


req = requests.get(getUrl(fighter)).text
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
