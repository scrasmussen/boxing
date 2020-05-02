import pandas as pd
from bs4 import BeautifulSoup
from tabulate import tabulate
import requests

# -- Boxers --
fighter = 'Floyd_Mayweather_Jr.'
fighter = 'Murat_Gassiev'                    #  eventually; on DAZN
fighter = 'Jarrett_Hurd'                     #  12.01.2018
fighter = 'Oleksandr_Usyk'                   #  11.10.2018
fighter = 'Canelo_Álvarez'                   #  09.15.2018
fighter = 'Rom%C3%A1n_Gonz%C3%A1lez_(boxer)' #  09.15.2018  # chocolatito
fighter = 'José_Ramírez_(boxer)'             #  09.14.2018
fighter = 'Mikey_Garcia'                     #  07.28.2018
fighter = 'Boxing_career_of_Manny_Pacquiao'  #  07.15.2018
fighter = 'Regis_Prograis'                   #  07.14.2018
fighter = 'Daniel_Dubois_(boxer)'            #  06.23.2018
fighter = 'Errol_Spence_Jr.'                 #  06.16.2018
fighter = 'Josh_Warrington'                  #  05.19.2018
fighter = 'Vasyl_Lomachenko'                 #  05.12.2018
fighter = 'Gennady_Golovkin'                 #  05.05.2018
fighter = 'Amir_Khan_(boxer)'                #  04.21.2018 vs
fighter = 'Jermall_Charlo'                   #  04.21.2018 vs Centeno
fighter = 'Adrian_Broner'                    #  04.21.2018 vs Vargas
                                             #       Davis vs Cuellar

 # https://www.forbes.com/sites/brianmazique/2018/04/02/boxing-schedule-april-2018-tv-and-stream-info-results-reported-earnings-and-viewership/#46c7737159f2


# -- MMA --
fighter = 'Alexander_Gustafsson'    # Retired
 # leg tied up but still jumps to knee opponent!
fighter = 'Felicia_Spencer'         #  02.29.2020  UFC Fight Night
fighter = 'Diego_Sanchez'           #  02.15.2020  UFC Fight Night
fighter = 'Arnold_Allen_(fighter)'  #  01.14.2020  UFC Fight Night
fighter = 'Frankie_Edgar'           #  12.21.2019  UFC Fight Night
fighter = 'Colby_Covington'         #  12.14.2019  UFC 245
fighter = 'Marlon_Moraes'           #  12.14.2019  UFC 245
fighter = 'Petr_Yan'                #  12.14.2019  UFC 245
fighter = 'Song_Yadong'             #  12.07.2019  UFC on ESPN
fighter = 'Jorge_Masvidal'          #  11.02.2019  UFC 244
                                    #  UFC Fight Night: Andrade vs. Zhang 13:45

# -- Currently Watching ---
# Boxing April 2018 || MMA August 2019
fighter = 'Lyoto_Machida'           # Bellator, past @ UFC 67 02.03.2007
fighter = 'Andre_Ward'
fighter = 'Buster_Douglas'
fighter = 'Mike_Tyson'
fighter = 'Bernard_Hopkins'
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
