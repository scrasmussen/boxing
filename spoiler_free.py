import pandas as pd
import requests
import sys
import re
import random
from bs4 import BeautifulSoup
from tabulate import tabulate


# ---------------------------- EVENTS ----------------------------
# event = 'UFC on ESPN: Blaydes vs. Volkov'
event = 'UFC_on_ESPN:_Kattar_vs._Ige'
event = 'UFC 141'
event = 'UFC_Fight_Night:_Waterson_vs._Hill' # NEED TO ADD THIS FIGHT!
event = 'UFC_Fight_Night:_Covington_vs._Woodley'
# event = 'UFC 252'
ffighter = 'Danny Henry'
ffighter = 'Jorge Masvidal'
ffighter = 'Stephen Thompson (fighter)'
ffighter = 'Alistair Overeem'
# ffighter='Bethe Correia'  # Jack Slack funny chant
# 8:12  Woodley vs. Burns
#       Sakia vs. Ivanov  1:34

# GSP vs Josh Koscheck
# GGG vs Daniel Jacobs, DAZN USA YOUTUBE
# https://www.youtube.com/watch?v=4VfPtgFEXYc


# Dominick Cruz vs Cody Garbandt, UFC 207
#
# UFC 17 : Chuck Liddell
# UFC 13 : Tito Ortiz's first fight
# at Mariano vs Vannata at 1:30 in fight pass
# ----------------------------------------------------------------
# --------------------  CURRENTLY WATCHING  ----------------------
# ----------------------------- MMA ------------------------------
# -- Historicalish
fighter = 'Lyoto Machida'
fighter = 'Georges St-Pierre'
fighter = 'Matt Hughes (fighter)'             # UFC 22,26
fighter = 'Kevin Randleman'
fighter = 'Sean O\'Malley (fighter)'
# ---------------------------- BOXING ----------------------------
# -- Historical
fighter = 'Archie Moore'   # The (Old) Mongoose, Jack Slack likes
fighter = 'Andre Ward'
fighter = 'Buster Douglas'
fighter = 'Mike Tyson'
fighter = 'Bernard Hopkins'
fighter = 'Roy Jones Jr.'
fighter = 'Charley Burley'
fighter = 'Pernell Whitaker' # Elite, defensive talent
fighter = 'Guillermo Rigondeaux' # ducked?
# -- Contemporary
fighter = 'Terence Crawford'
fighter = "Kell Brook"    # vs. Golovkin and then Spence Jr.
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ---------------------------- BOXERS ----------------------------
#---- Historical ----
fighter = 'Floyd Mayweather Jr.'
#----- Current ------
show    = 'The Boxing Beat: ESPN'
fighter = 'Timothy Bradley'
fighter = 'Murat Gassiev'                    #  eventually; on DAZN
fighter = 'Michael Conlan (boxer)'           #
fighter = 'Daniyar Yeleussinov'              #  09.13.2019 on DAZN vs Hicks
# Joshua vs Ruiz Jr.                         #  06.01.2019 DAZN, SFL
fighter = 'Austin Trout'                     #  05.25.2019
fighter = 'Gary Russell Jr.'                 #  05.18.2019
# Ortiz Jr. vs Herrera                       #  05.04.2019 DAZN, SFL
fighter = 'Amir Khan (boxer)'                #  04.20.2019 vs Crawford, EPSN
fighter = 'Errol Spence Jr.'                 #  03.16.2019
fighter = 'Leo Santa Cruz'                   #  02.16.2019
fighter = 'Gervonta Davis'                   #  02.09.2019 # fun, powerful
fighter = 'Adrian Broner'                    #  01.19.2019
fighter = 'Badou Jack'                       #  01.19.2019
# - [ ] December 22 – Josh Warrington vs Carl Frampton
# - [ ] December 22 – Dillian Whyte vs Dereck Chisora II
fighter = 'Jermall Charlo'                   #  12.22.2018
fighter = 'Jermell Charlo'                   #  12.22.2018
fighter = 'Josh Warrington'                  #  12.22.2018
fighter = 'Billy Joe Saunders'               #  12.22.2018
fighter = 'Sadam Ali'                        #  12.15.2018 beat by Munguia
fighter = 'Vasyl Lomachenko'                 #  12.08.2018 ESPN, Crolla Youtube
fighter = "Kell Brook"                       #  12.08.2018
# - [ ] December 1 – Deontay Wilder vs Tyson Fury [Showtime]
fighter = 'Jarrett Hurd'                     #  12.01.2018 PBC
fighter = 'Oleksandr Usyk'                   #  11.10.2018 Bellew, DAZN Youtube
fighter = 'Maciej Sulecki'                   #  11.10.2018
fighter = 'Josh Kelly (boxer)'               #  11.10.2018
fighter = 'Sullivan Barrera'                 #  11.03.2018
fighter = 'Josh Taylor (boxer)'              #  11.03.2018
fighter = 'Daniel Jacobs (boxer)'            #  10.27.2018 Survived cancer
                                             #           ; Chavez Jr. on SFL
fighter = 'Terence Crawford'                 #  10.13.2018 ESPN
fighter = 'Naoya Inoue'                      #  10.07.2018 DAZN
fighter = 'Daniel Dubois (boxer)'            #  10.06.2018
fighter = 'Jorge Linares'                    #  09.29.2018
fighter = 'Jerwin Ancajas'                   #  09.29.2018
fighter = 'Devin Haney'                      #  09.28.2018 2019 on DAZN, YT
                                             #           ; Haney on SFL
# - [ ] September 24 – Sho Kimura vs Kosei Tanaka
# - [ ] September 15 – Canelo Alvarez vs Gennady Golovkin II [DAZN]
fighter = 'Gennady Golovkin'                 #  09.15.2018 DAZN
fighter = 'Canelo Álvarez'                   #  09.15.2018 DAZN
fighter = 'Rom%C3%A1n_Gonz%C3%A1lez_(boxer)' #  09.15.2018  # chocolatito
fighter = 'Vergil Ortiz Jr.'                 #  09.15.2018 YT no DAZN til 2019
fighter = 'José Ramírez (boxer)'             #  09.14.2018
fighter = 'Amir Khan (boxer)'                #  09.08.2018 vs Samual Vargas
fighter = 'Shawn Porter'                     #  09.08.2018
fighter = 'Lewis Ritson'                     #  09.08.2018
fighter = 'Ryan García'                      #  09.01.2018 YT Morales
fighter = 'Tyson Fury'                       #  08.18.2018
fighter = 'Carl Frampton'                    #  08.18.2018 Jackson
fighter = 'Shakur Stevenson'                 #  08.18.2018 YT post 07.2019 ESPN
fighter = 'Sergey Kovalev'                   #  08.05.2018
# devin alexander vs. aundr bird spence      #  08.05.2018
# 08.04.2018
#  Kovalev vs. Eleidar Alvarez
# fighter = 'Dmitry Bivol'                   # vs. TBA
fighter = 'Zab Judah'

fighter = 'Mikey Garcia'                     #  07.28.2018 PBC Robert Easter Jr.
# - [ ] July 28 – Dereck Chisora vs Carlos Takam   [DAZN]
# Whyte vs Parker 02 Arena
# Kell Brook vs Brandon Cook
fighter = 'Carlos Balderas'                  #  07.28.2018 YT Caro

fighter = 'Jaime Munguía'                    #  07.21.2018 YT Smith
fighter = 'Boxing career of Manny Pacquiao'  #  07.15.2018 Matthysse, ESPN
# Undercard: Moruti Mthalane vs Muhammad Waseem for the IBF flyweight world
#  title; Carlos Canizares vs Bin Lu for the WBA super-straweight world title
fighter = 'Regis Prograis'                   #  07.14.2018 DAZN in future?
# ------------------------- 07.14.2018 current -------------------------



# Vergil Ortiz Jr. vs. Juan Carlos Salgado


# YT  = Young Talent
# SFL = Saturday Fight Live on DAZN

#
# April-June 2018 on DAZN:
#   Buatsi vs. Cuevas, Munguia vs. Ali, Okolie vs. Watkins
#
# --Classic--
# Andre Berto vs. Victor Ortiz
# GGG vs. Daniel Jacobs 3.18.2017
# Errol Spence Jr. vs Kell Brook 05.27.2017

fighter = 'Chris Eubank Jr' # vs Groves #  02.17.2018   # 09.28.2018
fighter = 'Keith Thurman'
# 06.24.2016 Shawn Porter    #  03.04.2017 vs Danny Garcia
# Gary Russell Jr. vs. Escandon 2017, vs. Hyland 2016, on Youtube Playlist
#                  vs. Lomachenko
# Big Steal: 'Viktor Postol' vs. Jamshidbek Najmiddinov
# one of the worst hbo fights   vs. Selçuk Aydın?



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
fighter = 'Justin Gaethje'
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
fighter = 'Sage Northcutt'          #  UFC 192
fighter = 'Aljamain Sterling'
fighter = 'Mounir Lazzez'

# --------------------------------------------------------------
# -----------------------  RANDOM NOTES  -----------------------
# --------------------------------------------------------------
# Jack Slack starts at UFC 202
# 2nd fastest knockdown
# tj dillashaw vs henry cejudo : head butt
# at thompson vs luque
# Whittaker vs Romero 1 and 2
# Giant Silva: PRIDE fighter
# Yves Edwards, practices thugjitsu
# Brian Ortega vs. Korean Zombie
fighter = 'Islam Makhachev'         #  04.20.2019  UFC Fight Night
# For something?                    #  02.11.2017  UFC 208
# this Smolka vs Paddy Holohan is the best grappling match
fighter = 'Louis Smolka'            #  10.24.2015 UFC Fight Night
# Tito Ortiz and Ken Shamrock       #  11.22.2002  UFC 40
# Felicia Spencer: leg tied up but still jumps to knee opponent!
#     UFC Fight Night: Andrade vs. Zhang 13:45
# Marvin Johnson vs Mathew Said Mohammad :: great classic fight
# Archie Moore vs Evon Durell            :: top ten list of fights

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
    p = re.compile('UFC_[0-9]+')
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
    if result is None:
        print("Table not found")
        sys.exit()
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
