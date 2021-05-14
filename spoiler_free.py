import pandas as pd
import sys
import random
import fighter as ft
import fightEvent as fe

# remove
import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate

event_bool = True
event_bool = False


# derrick lewis vs daniel cormier, look at cormier's entries
# ---------------------------- EVENTS ----------------------------
# event = 'UFC on ESPN: Blaydes vs. Volkov'
event = 'UFC_on_ESPN:_Kattar_vs._Ige'
event = 'UFC 141'
event = 'UFC on ESPN: Chiesa vs. Magny'
event = 'UFC 257' # watch prelims
event = 'UFC Fight Night: Thompson vs. Neal' # should watch prelims
event = 'UFC Fight Night: Blaydes vs. Lewis' # should watch prelims
event = 'UFC 259' # at Nzechukwu I think, and Joe Benavidez
event = 'UFC Fight Night: Brunson vs. Holland' # more of the ill follow you
#                                                home
#                                                and kill you
#                                                 - Montserrat Ruiz
#  invicta 33, 41
# event = 'UFC on ABC: Vettori vs. Holland' # On holtzman vs gamrot in
# prelims?

# to catch up on, Vettori vs Holland, UFC 260, and this
event = 'UFC on ESPN: Whittaker vs. Gastelum'
event = 'UFC on ESPN: Reyes vs. Procházka'
event = 'UFC on ESPN: Rodriguez vs. Waterson'
event = 'UFC 261' # prelims?

# fighter Sean Strickland, super technical, travels up/down Cali training
# ffighter = 'Khaos Williams' # watch 247 prelims with him
# ffighter = 'Gavin Tucker' # vs Jaynes 8/8/20, a banger fun fight, both do
#                           # weird intesting stuff



# check out Asian Boxing Raise?



# Hideo Tokoro vs. Daisuke Nakamura K-1 2008-12-31
#   K-1 Dynamite 2008
#   Saitama, Japan
# Ben Askren

# 4.24.2021 Qileng Aori vs Jeff Molina

# Charles Jourdain vs Marcelo Rojo, Jourdain is skilled fun fighter
#        |- check out more of his fights

# combat sambo, muay thai on ufc
# invicta fc 39 Pearl Gonzalez vs Leonardo
# some bellator on DAZN, cbs sports network, hulu?, moving to showtime


#  -- look at herb dean controversy too earlier UFCs
# 2.  ankalave good striker, can handle counter strikers, other wacky lots of
#                        kicks, great front kick to body
#     A need to keep K on the back foot so he is not kicking
#  Caceres vs Croom maybe fun 02.27.2021 UFC Fight Night: Rozenstruik vs. Gane
#


# event = 'UFC Fight Night: Overeem vs. Volkov' # watch prelims?
# jack slack 6
# james vick , upright tall fighter lost vs short guy, tried finishing uppercuts
# edson bubarso vs benile de el rush, every time hit, edson would run around
#    ring to walk off
# vador vs vagita; stumble after win

# --------------------------------------------------------------
# ----------------------------- MMA ----------------------------
# --------------------------------------------------------------
# ________
# | 1997 | October, start watching Pride
# | 1996 | start watching Sakuraba fights
#
# __current__ : UFC 9, 05.17.1996
# past to watch : UFC The ultimate ultimate
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#

# more Pettis!
# ffighter = 'Henry Cejudo'    # UFC FOX 12.13.2014
# ffighter = 'Jorge Masvidal'  # UFC FOX 04.20.2013, Bellator since 1
# 'Stephen Thompson (fighter)' # UFC 143 02.04.2012
# ffighter = 'T.J. Dillashaw'  # UFC FOX 12.03.2011
# ffighter = 'Anthony Pettis'  # UFC 136 10.08.2011, GFS & WEC from 2007
# ffighter = 'Tony Ferguson'   # UFC 135 09.24.2011
# ffighter = 'Donald Cerrone'  # UFC 126 02.05.2011
#   fights with Jamie Varner and Benson Henderson were,
#   and still are classics of the non-UFC genre.
# ffighter = 'Dustin Poirier'  # UFC 125 01.01.2011
# ffighter = 'Ben Askren' # Bellator 14  04.15.2010
# UFC 104: title fight, ring cutoff      12.24.2009
# ffighter = 'Roy Nelson'      # TUF 10  12.05.2009
# ffighter = 'Shane Carwin'    # UFC 84  05.24.2008
# ffighter = 'Cain Velasquez'  # UFC 83  04.19.2008
# ffighter = 'Conor McGregor'  # Pre-UFC 03.08.2008  UFC 04.06.2013
# ffighter = 'Chan Sung Jung' # Pancrase 12.16.2007, UFC 12.10.2011
# 'Alexander Gustafsson'       # UFC 105 11.14.2009
#                         Shooto Finland 11.17.2007
# ffighter = 'Brock Lesner'    # UFC 81  02.02.2008
#                               Dynamite 06.02.2007
# ffighter = 'Frankie Edgar'   # UFC 67  02.03.2007
# ffighter = 'Lyoto Machida'   # UFC 67  02.03.2007
# ffighter = 'Diego Sanchez'   # UFC 54  08.20.2005
# ffighter = 'Giant Silva'     # Pride   12.31.2003
# ffighter= Fedor Emelianenko' #Pride 21 06.23.2002, in Rings from 2000-02.2002
# ffighter= Georges St-Pierre' # UFC 46  01.31.2004 UCC in 01.25.2002
# ffighter = 'Mirko Cro Cop'   # Pride   11.03.2001 UFC 67 02.03.2007
# ffighter = 'Antônio Rodrigo Nogueira'# 07.29.2001 Pride 15, later UFC 73 2001
# ffighter = 'Alistair Overeem'#         10.24.1999
# ffighter = 'Kevin Randleman' # UFC 19  03.05.1999
# ffighter = 'Chuck Liddell'   # UFC 17  05.15.1998
# ffighter = 'Matt Hughes (fighter)'#    09.24.1999  UFC 22, lots of others
#              Jeet Kune Do Challenge 1  01.01.1998
# ffighter = 'Tito Ortiz'      #         05.30.1997
# ffighter = 'Randy Couture'   # UFC 13  05.30.1997
#             bounce people off of fence to get past guard
# ffighter = 'Alexey Oleynik'  #         11.10.1996
# ffighter = 'Kazushi Sakuraba'#         07.14.1996
# __________current_________   : UFC  9  05.17.1996  -------------------
# ffighter = 'Frank Shamrock' # Pancrase 12.16.1994, UFC 12.21.1997
# ffighter = 'Ken Shamrock'   # Pancrase 09.21.1993
# ffighter = 'Bas Rutten'     # Pancrase 09.21.1993, UFC 01.08.1999

# ----------------------------------------------------------------------
#                         Fedor Emelianenko
# ----------------------------------------------------------------------
# fabor emelianenko vs heath herring, crocop, vs kevin randelman (end great,
#                                                             polite at end)
# vs crocop (fabor had a masterful plan, went to holland had Tyrone Spong &
#            Ernesto Hoost)
# stipe miocic could probably take him , fabricio werdum on a very good day
# perfect record obsession: black
# vs Tsuyoshi Kohsaka, vs Blagoi Ivanov (combat sambo)
# ----------------------------------------------------------------------



# --- Young Bloods ---
# ffighter = 'Loma Lookboonmee' # fixed; last fight on ESPN
# first thai fighter to sign with UFC, had that one match a few before
# ffighter = 'Youssef Zalal'   #         02.08.2020, LFA 22 09.08.2017
# ffighter = 'Jimmy Crute'     #         07.24.2018
# ffighter = 'Antonina Shevchenko' #     06.26.2018
# ffighter = 'Ciryl Gane'      #         08.02.2018
# Serigne Ousmane Dia "Bombardier / B52"
#      vs Konez 05.05.2018;   vs Podmore 02.20.2020
# ffighter = 'Liana Jojua'             # 09.07.2019 UFC 242
# Mariano vs Vannata           UFC 234:  02.09.2019
# ffighter = 'Johnny Walker (fighter)' # 08.11.2018
# ffighter = 'Sean O\'Malley (fighter)'# 03.03.2018 UFC 222
# ffighter = 'Israel Adesanya' #         02.11.2018 UFC 221
# ffighter = 'Ian Heinisch'   #          07.31.2018 LFA 04.21.2017
#                        great anti-wrestling, will just stand right up
# ffighter = 'Zabit Magomedsharipov' #   09.02.2017  ACB before that
# ffighter = 'Trevin Giles'   #          07.08.2017
#                        power, good striker, someone to watch
# ffighter = 'Cody Stamann'  #           07.08.2017 UFC 213
# ffighter = 'Justin Gaethje' #          07.07.2017
# ffighter = 'Marlon Moraes'  #          06.03.2017 UFC 212
# Dominick Cruz vs Cody Garbandt,        12.30.2016 UFC 207
# ffighter = 'Yana Kunitskaya' #         11.18.2016 Invicta 20
#             keyyah like every time
# ffighter = 'Marvin Vettori' #          08.20.2016 Italian middleweight
# Jack Slack starts at UFC 202           08.20.2016
# ffighter = 'Curtis Blaydes'  #         04.10.2016
# ffighter = 'Kamaru Usman'    #         12.19.2015
# ffighter = 'Sage Northcutt'  #         10.03.2015   UFC 192
# ffighter = 'Felicia Spencer' #         09.12.2015 Invicta 14
# ffighter = 'Arnold Allen (fighter)' #  06.20.2015
# ffighter = 'Danny Henry' # anacondas   06.06.2015 EFC 57, UFC 251
# ffighter = 'Cody Garbrandt'  #         01.03.2015 UFC 182
# ffighter = 'Kron Gracie' #             12.23.2014
# ffighter = 'Petr Yan'  #               06.23.2018
#                Siberian league         12.20.2014
# ffighter = 'Seo Hee Ham' # atom weight 12.12.2014 the ultimate fighter 18
#                                        02.16.2007 Deep
# ffighter = 'Colby Covington'  #        08.23.2014
# ffighter = 'Carlos Diego Ferreira' #   06.28.2014
# ffighter = 'Aljamain Sterling'#        02.22.2014
# ffighter = 'Ottman Azaitar'   #        01.15.2014 temp removed from UFC
# -- a bad man, ko power, man with a bag sneaked into room
# ffighter='Bethe Correia'      #        12.07.2013 Jack Slack funny chant
# ffighter = 'Song Yadong'      #        11.25.2017
#                 RUFF 9                 05.18.2013
# ffighter = 'Neil Magny'       #        02.23.2013 UFC 157
# ffighter='Robert Whittaker (fighter)'# 12.15.2012
# ffighter = 'Tim Elliott' #             05.05.2012 no respect, love it
# ffighter = 'Cub Swanson' # fierce look 11.12.2011

# -----------------------  RANDOM NOTES  -----------------------
# 2nd fastest knockdown
# T.J. Dillashaw vs henry cejudo : head butt
# at thompson vs luque
# Whittaker vs Romero 1 and 2
# Yves Edwards, practices thugjitsu
# Brian Ortega vs. Korean Zombie
fighter = 'Islam Makhachev'         #  04.20.2019  UFC Fight Night
# For something?                    #  02.11.2017  UFC 208
# this Smolka vs Paddy Holohan is the best grappling match
fighter = 'Louis Smolka'            #  10.24.2015 UFC Fight Night
# Tito Ortiz and Ken Shamrock       #  11.22.2002  UFC 40
# Felicia Spencer: leg tied up but still jumps to knee opponent!
#     UFC Fight Night: Andrade vs. Zhang 13:45

# Fedor, Couture, Velasquez, and Nog; Monsters: Brock Lesner, Shane Carwin

# best Pride Fights
#https://bleacherreport.com/articles/1767697-the-9-best-pride-fights-of-all-time

# --- Watch --
# Ernesto Hoost (youtube)
# Tyrone Spong (youtube)


# event_bool = False
# --- Muay Thai Fighters ---
# fighter = 'Rafael Fiziev' #  kicks Hard, Muay Thai background so...
# heavyweight Gane, muay thai -> boxing, bad when trying to hit hard






# ----------------------------------------------------------------
# --------------------  CURRENTLY WATCHING  ----------------------
# ---------------------------- BOXING ----------------------------
# ----------------------------------------------------------------
# GSP vs Josh Koscheck
# GGG vs Daniel Jacobs, DAZN USA YOUTUBE
# https://www.youtube.com/watch?v=4VfPtgFEXYc

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
fighter = 'Kell Brook'    # vs. Golovkin and then Spence Jr.
fighter = 'Anthony Joshua'
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ---------------------------- BOXERS ----------------------------
#---- Historical ----
fighter = 'Floyd Mayweather Jr.'
#----- Current ------

show    = 'The Boxing Beat: ESPN'
fighter = 'Canelo Álvarez'
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
# forrest vs mayorga
# Gary Russell Jr. vs. Escandon 2017, vs. Hyland 2016, on Youtube Playlist
#                  vs. Lomachenko
# Big Steal: 'Viktor Postol' vs. Jamshidbek Najmiddinov
# one of the worst hbo fights   vs. Selçuk Aydın?




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


fighter_name = fighter
# allows easy access to fighters near the top
if 'ffighter' in locals():
    fighter_name = ffighter


# run event if in command line
# if (len(sys.argv) > 1):
#     if (sys.argv[1] == 'event'):
#         getEvent()
#     sys.exit()

if event_bool is True:
    event = fe.FightEvent(event)
    event.print_name()
    event.print_events()
else:
    # --- handle fighter ---
    fighter = ft.Fighter(fighter_name)
    fighter.print_name()
    fighter.print_records()


print("Fin")
