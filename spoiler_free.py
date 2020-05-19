import pandas as pd
import requests
import sys
import re
import random
from bs4 import BeautifulSoup
from tabulate import tabulate


# ---------------------------- EVENTS ----------------------------
event = 'UFC 235'
# at Mariano vs Vannata at 1:30 in fight pass
# ----------------------------------------------------------------
# --------------------  CURRENTLY WATCHING  ----------------------
# ----------------------------- MMA ------------------------------
# -- Historicalish
fighter = 'Lyoto Machida'
fighter = 'Georges St-Pierre'
fighter = 'Matt Hughes (fighter)'             # UFC 22,26
# ---------------------------- BOXING ----------------------------
# -- Historical
fighter = 'Archie Moore'   # The (Old) Mongoose, Jack Slack likes
fighter = 'Andre Ward'
fighter = 'Buster Douglas'
fighter = 'Mike Tyson'
fighter = 'Bernard Hopkins'
fighter = 'Roy Jones Jr.'
fighter = 'Charley Burley'
# -- Contemporary
fighter = 'Terence Crawford'
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ---------------------------- BOXERS ----------------------------
#---- Historical ----
fighter = 'Floyd Mayweather Jr.'
#----- Current ------
fighter = 'Timothy Bradley'
fighter = 'Murat Gassiev'                    #  eventually; on DAZN
# Joshua vs Ruiz Jr.                         #  06.01.2019 DAZN, SFL
# Ortiz Jr. vs Herrera                       #  05.04.2019 DAZN, SFL
fighter = 'Amir Khan (boxer)'                #  04.20.2019 vs Crawford, EPSN
fighter = 'Gervonta Davis'                   #  02.09.2019 # fun, powerful
fighter = 'Adrian Broner'                    #  01.19.2019
fighter = 'Jermall Charlo'                   #  12.22.2018
fighter = 'Sadam Ali'                        #  12.15.2018 beat by Munguia
fighter = 'Vasyl Lomachenko'                 #  12.08.2018 ESPN, Crolla Youtube
fighter = 'Jarrett Hurd'                     #  12.01.2018 PBC
fighter = 'Oleksandr Usyk'                   #  11.10.2018 Bellew, DAZN Youtube
fighter = 'Maciej Sulecki'                   #  11.10.2018
fighter = 'Daniel Jacobs (boxer)'            #  10.27.2018 Survived cancer
                                             #           ; Chavez Jr. on SFL
fighter = 'Jorge Linares'                    #  09.29.2018
fighter = 'Devin Haney'                      #  09.28.2018 2019 on DAZN, YT
                                             #           ; Haney on SFL
fighter = 'Gennady Golovkin'                 #  09.15.2018 DAZN
fighter = 'Canelo Álvarez'                   #  09.15.2018 DAZN
fighter = 'Rom%C3%A1n_Gonz%C3%A1lez_(boxer)' #  09.15.2018  # chocolatito
fighter = 'José Ramírez (boxer)'             #  09.14.2018
fighter = 'Amir Khan (boxer)'                #  09.08.2018 vs Samual Vargas
fighter = 'Ryan García'                      #  09.01.2018 YT Morales
# devin alexander vs. aundr bird spence      #  08.05.2018
fighter = 'Mikey Garcia'                     #  07.28.2018 PBC
fighter = 'Jaime Munguía'                    #  07.21.2018 YT
fighter = 'Boxing career of Manny Pacquiao'  #  07.15.2018
fighter = 'Regis Prograis'                   #  07.14.2018
# Alex Saucedo vs Lenny Zappavigna           #  06.30.2018
fighter = 'Daniel Dubois (boxer)'            #  06.23.2018
fighter = 'Josh Taylor (boxer)'              #  06.23.2018
fighter = 'Josh Kelly (boxer)'               #  06.16.2018
fighter = 'Errol Spence Jr.'                 #  06.16.2018 PBC
fighter = 'Daniyar Yeleussinov'    # 06.06.2018, 09.13.2019 on DAZN
fighter = 'Michael Conlan (boxer)'           #  06.12.2018
fighter = 'Terence Crawford'                 #  06.09.2018
fighter = 'Carlos Balderas'                  #  06.09.2018
fighter = 'Shakur Stevenson'                 #  06.09.2018
# Okolie vs. Watkins                         #  06.06.2018 DAZN
# Inoue vs McDonnell, WBC featherweight      #  05.25.2018
fighter = 'Vergil Ortiz Jr.'                 #  05.23.2019 DAZN ?
fighter = 'Josh Warrington'                  #  05.19.2018 vs Lee Selby
# Stevenson vs Jack, Russell vs Diaz         #  05.19.2018 PBC
# April-June 2018 on DAZN:
#   Buatsi vs. Cuevas, Munguia vs. Ali, Okolie vs. Watkins
#
# YT  = Young Talent
# SFL = Saturday Fight Live on DAZN

# ----------------------------- MMA -----------------------------
fighter = 'Alexander Gustafsson'    # Retired
#---- Historical ----
fighter = 'Randy Couture' # bounce people off of fence to get past guard
fighter = 'Kazushi Sakuraba'
fighter = 'Roy Nelson'
#----- Current ------
fighter = 'Petr Yan'
fighter = 'Song Yadong'
fighter = 'Chan Sung Jung '
fighter = 'Arnold Allen (fighter)'
fighter = 'Colby Covington'
fighter = 'Jorge Masvidal'
fighter = 'Curtis Blaydes'          #  Like this heavyweight
fighter = 'Carlos Diego Ferreira'
fighter = 'Donald Cerrone'
fighter = 'Frankie Edgar'
fighter = 'Marlon Moraes'
fighter = 'Tim Elliott'             # no respect, love it
fighter = 'Israel Adesanya'
fighter = 'Felicia Spencer'
fighter = 'Kamaru Usman'
fighter = 'Robert Whittaker (fighter)'
fighter = 'Diego Sanchez'
fighter = 'Tony Ferguson'
fighter = 'Johnny Walker (fighter)' #  finishes people in minutes
fighter = 'Frankie Edgar'
fighter = 'Zabit Magomedsharipov'
fighter = 'Kron Gracie'
fighter = 'Cody Stamann'
fighter = 'Ben Askren'
fighter = 'Cody Garbrandt'
fighter = 'Aleksei Oleinik'
ffighter = 'Sage Northcutt'
# --------------------------------------------------------------
# -----------------------  RANDOM NOTES  -----------------------
# --------------------------------------------------------------
# Jack Slack starts at UFC 202
# 2nd fastest knockdown
# tj dillashaw vs henry cejudo : head butt
# at thompson vs luque
fighter = 'Islam Makhachev'         #  04.20.2019  UFC Fight Night
# For something?                    #  02.11.2017  UFC 208
# this Smolka vs Paddy Holohan is the best grappling match
fighter = 'Louis Smolka'            #  10.24.2015 UFC Fight Night
# Tito Ortiz and Ken Shamrock       #  11.22.2002  UFC 40
# leg tied up but still jumps to knee opponent!
#     UFC Fight Night: Andrade vs. Zhang 13:45
# --------------------------------------------------------------
# --------------------------------------------------------------
# --------------------------------------------------------------
# --------------------------------------------------------------
# --------------------------------------------------------------
# --------------------------------------------------------------
# --------------------------------------------------------------
# --------------------------------------------------------------
# allows easy access to fighters near the top
if 'ffighter' in locals():
    fighter = ffighter
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
    if (fighter == ''):
        print("No Fighter Selected")
        exit()
    fighter.replace(' ', '_')
    url = 'https://en.wikipedia.org/wiki/'
    url += fighter
    return url

def getEventUrl(event):
    if (event == ''):
        print("No Event Selected")
        exit()
    event = event.replace(' ', '_')

    #- check if UFC PPV
    p = re.compile('UFC_[1-9]+')
    match = p.match(event)
    if match is not None:
        event = match.group()

    url = 'https://en.wikipedia.org/wiki/'
    url += event
    return url


def getEvent():
    # --------------------------------------------------------------------------
    #                                  EVENT
    # --------------------------------------------------------------------------
    url = getEventUrl(event)
    req = requests.get(url).text
    soup = BeautifulSoup(req, 'lxml')
    # result = soup.find_all('table', {'class': 'wikitable'})
    result = soup.find('table', {'class': 'toccolours'})
    if result is None:
        result = soup.find('table')
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


        # --- check what prelims there are ---
        has_prelim = table['Weight class'].str.contains("Preliminary")
        has_early_prelim_l = table['Weight class'].str.contains("Early Preliminary")
        has_early_prelim = any(i == True for i in has_early_prelim_l)

        # --- get range of tables
        prelim_row_i = list(has_prelim).index(True)
        if (has_early_prelim):
            early_prelim_row_i = list(has_early_prelim_l).index(True)
            prelim_row_e = early_prelim_row_i
        else:
            prelim_row_e = len(table)

        # --- split and print tables ---
        maincard = table.iloc[:prelim_row_i,:]
        print(tabulate([[event.replace('_',' ')]], tablefmt='psql'))
        print(tabulate([["Maincard"]], tablefmt='psql'))
        print(tabulate(maincard,headers='keys',tablefmt='psql',showindex=False))

        prelims  = table.iloc[prelim_row_i+1:prelim_row_e,:]
        print(tabulate([["Prelims"]], tablefmt='psql'))
        print(tabulate(prelims,headers='keys',tablefmt='psql',showindex=False))

        if (has_early_prelim):
            early_prelims  = table.iloc[early_prelim_row_i+1:,:]
            print(tabulate([["Early Prelims"]], tablefmt='psql'))
            print(tabulate(early_prelims,headers='keys',tablefmt='psql',
                           showindex=False))


        print("Fin")
        sys.exit()

# run event if in command line
if (len(sys.argv) > 1):
    if (sys.argv[1] == 'event'):
        getEvent()
    sys.exit()

# ----------------------------------------------------------------------------
#                                  START
# ----------------------------------------------------------------------------



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
