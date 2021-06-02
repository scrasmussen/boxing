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
event = 'UFC on ESPN: Reyes vs. Procházka'
event = 'UFC on ESPN: Rodriguez vs. Waterson'
event = 'UFC 261' # prelims?
event = 'UFC on ESPN: Whittaker vs. Gastelum'
event = 'UFC Fight Night: Font vs. Garbrandt'


ffighter = "Shane Burgos" #that bellator guys favorite fighter, Michael Chandler
ffighter = 'Juan Espino' # heavy weight grappler
# fighter Sean Strickland, super technical, travels up/down Cali training
# ffighter = 'Khaos Williams' # watch 247 prelims with him
# ffighter = 'Gavin Tucker' # vs Jaynes 8/8/20, a banger fun fight, both do
#                           # weird intesting stuff
# "Good on Arjan Bhullar. I've liked him since he headbutted Juan Adams"
#                          - Jack Slack
# check out Asian Boxing Raise?



# Hideo Tokoro vs. Daisuke Nakamura K-1 2008-12-31
#   K-1 Dynamite 2008
#   Saitama, Japan
# --- early fights of ---
# --- Ben Askren --------
# --- Deontay Wilder ----
# --- Tyson Fury --------

# 4.24.2021 Qileng Aori vs Jeff Molina
# Charles Jourdain vs Marcelo Rojo, Jourdain is skilled fun fighter
#        |- check out more of his fights

# combat sambo, muay thai on ufc
# invicta fc 39 Pearl Gonzalez vs Leonardo
# some bellator on DAZN, cbs sports network, hulu?, moving to showtime
#
#
#  -- look at herb dean controversy too earlier UFCs
# 2.  ankalave good striker, can handle counter strikers, other wacky lots of
#                        kicks, great front kick to body
#     A need to keep K on the back foot so he is not kicking
#  Caceres vs Croom maybe fun 02.27.2021 UFC Fight Night: Rozenstruik vs. Gane
#
#
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
# -- Mark Hunt vs Antonio "BigFoot" Silva
# 'Stephen Thompson (fighter)' # UFC 143 02.04.2012
# ffighter = 'T.J. Dillashaw'  # UFC FOX 12.03.2011
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
# ffighter = 'Anthony Pettis'  # UFC 136 10.08.2011, GFS & WEC from 2007
# ffighter = 'Diego Sanchez'   # UFC 54  08.20.2005
# ffighter = 'Giant Silva'     # Pride   12.31.2003
# ffighter = 'Lyoto Machida'   # UFC 67  02.03.2007, 2003 before
# ffighter= Georges St-Pierre' # UFC 46  01.31.2004
#                                UCC in  01.25.2002
# ffighter = 'Antônio Rodrigo Nogueira'# 07.29.2001 Pride 15, later UFC 73 2001
# ffighter = 'Hideo Tokoro'    # TFC 1   09.29.2000
# ffighter='Fedor Emelianenko' #Pride 21 06.23.2002
#         , in Rings from 2000-02.2002   05.21.2000
# ffighter = 'Alistair Overeem'#         10.24.1999
# ffighter = 'Kevin Randleman' # UFC 19  03.05.1999
# ffighter = 'Badr Hari'       #         02.17.2002 Kickboxing
# ffighter = 'Chuck Liddell'   # UFC 17  05.15.1998
# ffighter = 'Matt Hughes (fighter)'#    09.24.1999  UFC 22, lots of others
#              Jeet Kune Do Challenge 1  01.01.1998
# ffighter = 'Tito Ortiz'      #         05.30.1997
# ffighter = 'Randy Couture'   # UFC 13  05.30.1997
#             bounce people off of fence to get past guard
# ffighter = 'Alexey Oleynik'  #         11.10.1996
# __________at_________   : UFC  10  07.12.1996  ------------------
# ffighter = 'Kazushi Sakuraba'#         07.14.1996
# ffighter = 'mirko cro cop'   # pride   11.03.2001 ufc 67 02.03.2007
#    k-1 grand prix '99 final round      12.05.1999 kickboxing since 1996
# ffighter = 'frank shamrock' # pancrase 12.16.1994, ufc 12.21.1997
# ffighter = 'ken shamrock'   # pancrase 10.14.1993
#          all Pancrase and UFC until Pride in 2000
# ffighter = 'Bas Rutten'     # pancrase 10.14.1993, ufc 01.08.1999
# -----------------------------------------------------------------
#                   CURRENT: 10.14.1993
# -----------------------------------------------------------------
#        Pride 1 : 10.11.1997
#        UFC 10  : 07.12.1996
#    *   Pancrase: yes, we are hybrid wrestlers 3 11.00.1993
#

# ----------------------------------------------------------------------
#                         fedor emelianenko
# ----------------------------------------------------------------------
# fabor emelianenko vs heath herring, crocop, vs kevin randelman (end great,
#                                                             polite at end)
# vs crocop (fabor had a masterful plan, went to holland had tyrone spong &
#            ernesto hoost)
# stipe miocic could probably take him , fabricio werdum on a very good day
# perfect record obsession: black
# vs tsuyoshi kohsaka, vs blagoi ivanov (combat sambo)
# ----------------------------------------------------------------------



# --- young bloods ---
# ffighter = 'loma lookboonmee' # fixed; last fight on espn
# first thai fighter to sign with ufc, had that one match a few before
# ffighter = 'youssef zalal'   #         02.08.2020, lfa 22 09.08.2017
# ffighter = 'jimmy crute'     #         07.24.2018
# ffighter = 'antonina shevchenko' #     06.26.2018
# ffighter = 'ciryl gane'      #         08.02.2018
# serigne ousmane dia "bombardier / b52"
#      vs konez 05.05.2018;   vs podmore 02.20.2020
# ffighter = 'liana jojua'             # 09.07.2019 ufc 242
# mariano vs vannata           ufc 234:  02.09.2019
# ffighter = 'johnny walker (fighter)' # 08.11.2018
# ffighter = 'sean o\'malley (fighter)'# 03.03.2018 ufc 222
# ffighter = 'israel adesanya' #         02.11.2018 ufc 221
# ffighter = 'ian heinisch'   #          07.31.2018 lfa 04.21.2017
#                        great anti-wrestling, will just stand right up
# ffighter = 'zabit magomedsharipov' #   09.02.2017  acb before that
# ffighter = 'trevin giles'   #          07.08.2017
#                        power, good striker, someone to watch
# ffighter = 'cody stamann'  #           07.08.2017 ufc 213
# ffighter = 'justin gaethje' #          07.07.2017
# ffighter = 'marlon moraes'  #          06.03.2017 ufc 212
# dominick cruz vs cody garbandt,        12.30.2016 ufc 207
# ffighter = 'yana kunitskaya' #         11.18.2016 invicta 20
#             keyyah like every time
# ffighter = 'marvin vettori' #          08.20.2016 italian middleweight
# jack slack starts at ufc 202           08.20.2016
# ffighter = 'curtis blaydes'  #         04.10.2016
# ffighter = 'kamaru usman'    #         12.19.2015
# ffighter = 'felicia spencer' #         09.12.2015 invicta 14
# ffighter = 'arnold allen (fighter)' #  06.20.2015
# ffighter = 'danny henry' # anacondas   06.06.2015 efc 57, ufc 251
# ffighter = 'cody garbrandt'  #         01.03.2015 ufc 182
# ffighter = 'kron gracie' #             12.23.2014
# ffighter = 'petr yan'  #               06.23.2018
#                siberian league         12.20.2014
# ffighter = 'seo hee ham' # atom weight 12.12.2014 the ultimate fighter 18
#                                        02.16.2007 deep
# ffighter = 'colby covington'  #        08.23.2014
# ffighter = 'carlos diego ferreira' #   06.28.2014
# ffighter = 'sage northcutt'  #         04.20.2014 ufc 192: 10.03.2015
# ffighter = 'aljamain sterling'#        02.22.2014
# ffighter = 'ottman azaitar'   #        01.15.2014 temp removed from ufc
# -- a bad man, ko power, man with a bag sneaked into room
# ffighter='bethe correia'      #        12.07.2013 jack slack funny chant
# ffighter = 'song yadong'      #        11.25.2017
#                 ruff 9                 05.18.2013
# ffighter = "uriah hall"       #        04.13.2013
# ffighter = 'neil magny'       #        02.23.2013 ufc 157
# ffighter='robert whittaker (fighter)'# 12.15.2012
# ffighter = 'tim elliott' #             05.05.2012 no respect, love it
# ffighter = 'cub swanson' # fierce look 11.12.2011

# -----------------------  random notes  -----------------------
# 2nd fastest knockdown
# t.j. dillashaw vs henry cejudo : head butt
# at thompson vs luque
# whittaker vs romero 1 and 2
# yves edwards, practices thugjitsu
# brian ortega vs. korean zombie
fighter = 'islam makhachev'         #  04.20.2019  ufc fight night
# for something?                    #  02.11.2017  ufc 208
# this smolka vs paddy holohan is the best grappling match
fighter = 'louis smolka'            #  10.24.2015 ufc fight night
# tito ortiz and ken shamrock       #  11.22.2002  ufc 40
# felicia spencer: leg tied up but still jumps to knee opponent!
#     ufc fight night: andrade vs. zhang 13:45

# fedor, couture, velasquez, and nog; monsters: brock lesner, shane carwin

# best pride fights
#https://bleacherreport.com/articles/1767697-the-9-best-pride-fights-of-all-time

#
# Kick boxing
# --Ernesto Hoost--
# Branko Cikatić
#
# K-1 World Grand Prix
# https://en.wikipedia.org/wiki/K-1_World_Grand_Prix


# --- Watch --
# Ernesto Hoost (youtube)
# Tyrone Spong (youtube)


# event_bool = False
# --- Muay Thai Fighters ---
# Rambaa Somdet  : greatest strawweight in MMA, Muay Thai
# fighter = 'Rafael Fiziev' #  kicks Hard, Muay Thai background so...
# heavyweight Gane, muay thai -> boxing, bad when trying to hit hard


# --------------------------------------------------------------
# -------------------------- GRAPPLING -------------------------
# --------------------------------------------------------------
# Hideo Tokoro, more MMA




# ----------------------------------------------------------------
# --------------------  CURRENTLY WATCHING  ----------------------
# ---------------------------- BOXING ----------------------------
# ----------------------------------------------------------------
#
# https://www.theguardian.com/sport/2021/may/27/time-to-find-out-who-cares-box\
#ing-brain-damage-tris-dixon
#
# GSP vs Josh Koscheck
# GGG vs Daniel Jacobs, DAZN USA YOUTUBE
# https://www.youtube.com/watch?v=4VfPtgFEXYc
# Wilfred Benítez vs. Sugar Ray Leonard

fighter = 'Anthony Joshua' # |     1 | Emanuele Leo        | 10.05.2013 |
fighter = 'Deontay Wilder' # |     4 | Joseph Rabotte      | 04.24.2009 |
                            # couldn't find Wilder's #3 vs Greene
fighter = 'Floyd Mayweather Jr.' # |36| Zab Judah          | 04.08.2006 |
fighter = 'Andre Ward' # |     1 | Chris Molina            | 12.18.2004 |
fighter = 'Bernard Hopkins' # |     1 | Clinton Mitchell   | 10.11.1988 |
fighter = 'Mike Tyson' #|     1 | Hector Mercedes          | 03.06.1985 |

# -- Historical
fighter = 'Archie Moore'   # The (Old) Mongoose, Jack Slack likes
fighter = 'Buster Douglas'
fighter = 'Roy Jones Jr.'
fighter = 'Charley Burley'
fighter = 'Pernell Whitaker' # Elite, defensive talent
fighter = 'Guillermo Rigondeaux' # ducked?
fighter = 'Aaron Pryor' # two battles with Alexis Arguello
# -- Contemporary
fighter = 'Terence Crawford'
fighter = 'Kell Brook'    # vs. Golovkin and then Spence Jr.
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ---------------------------- BOXERS ----------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------

show    = 'The Boxing Beat: ESPN'
# https://www.theguardian.com/sport/2021/may/27/\
# time-to-find-out-who-cares-boxing-brain-damage-tris-dixon

# Watch Vasiliy Lomachenko vs. Teofima Lopez again
# June 26th Show: PPV soooo....
# June 26th ESPN: Vasiliy Lomachenko vs Masayoshi Nakatani
# June 25th ESPN: Rob Brant vs Janibek Alimkhanuly
# June 19th DAZN: Bektemir Melikuziev vs Gabriel Rosado
# June 19th DAZN: Jaime Munguia vs Maciej Sulecki
# June 19th ESPN: *Naoya Inoue* vs Michael Dasmarinas
# June 12th ESPN: Shakur Stevenson vs Jeremiah Nakathila
#                 Jose Pedraza vs Julian Rodriguez
#


fighter = 'Naoya Inoue'
fighter = 'Canelo Álvarez'
fighter = 'Timothy Bradley'
# listed below 'Terence Crawford', Errol Spence Jr., Teofima Lopez
# Usyk, Lomachenko, Josh Taylor, Juan Francisco Estrada
# Michael Hunter: Heavyweight American
# Andy Ruiz Jr. : Heavyweight American
# Joe Joyce     : Heavyweight U.K.
# Dillian Whyte : Heavyweight U.K.
# Alexander Povetkin: Heavyweight Russia
#
# Nonito Donaire vs. Nordine Oubaali
#
# Shakur Stevenson
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
#  QUOTES
# --------------------------------------------------------------
# “Weeping may endure for a night, but joy cometh in the
#  morning.”
#   - Psalm 30:5
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
