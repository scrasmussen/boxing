import sys
import fighter as ft
import fightEvent as fe

event_bool = True
event_bool = False


# Gene Fullmer : the Mormon Mauler
# ---------------------------- EVENTS ----------------------------
# Contemporary:
#   - 10.31 : ESPN, DAZN, UFC, Showtime? Figueroa vs. Fulton
#
# 05.15.2021 DAZN to see Dalton Smith
# Invicta Fighting Phoenix
# event = 'UFC on ESPN: Blaydes vs. Volkov'
event = 'UFC_on_ESPN:_Kattar_vs._Ige'
event = 'UFC 141'
event = 'UFC Fight Night: Brunson vs. Holland'
## more of the ill follow you home and kill you - Montserrat Ruiz
#  invicta 33, 41
# event = 'UFC on ABC: Vettori vs. Holland' # On holtzman vs gamrot in

#
# ------- OLYMPIC BOXING: TOKYO EDITION -------
#
# to catch up on, Vettori vs Holland, and this
event = 'UFC 263' # prelims?
event = 'UFC 262' # Prelims: Submissions!
event = 'UFC 260' # prelims?
event = 'UFC 257' # prelims
event = 'UFC Fight Night: Thompson vs. Neal' # should watch prelims
event = 'UFC Fight Night: Blaydes vs. Lewis' # should watch prelims


# --------------------------------------------------------------
# ------------------------- JACK SLACK -------------------------
# --------------------------------------------------------------
fighter = 'Gavin Tucker'   # 08.08.2020 vs Jaynes  a banger fun fight
                           # both do weird intesting stuff
fighter = 'Khaos Williams' # 02.08.2020 watch 247 prelims with him
fighter = 'Rin Nakai'      # 10.01.2006 Pacrase 167,
                           # check UFC
fighter = 'Arjan Bhullar' # 05.04.2019 vs Juan Adams
# "Good on Arjan Bhullar. I've liked him since he headbutted Juan Adams"
#                          - Jack Slack
fighter = 'Daniel Cormier' # UFC 230 | 11.03.2018 |
# derrick lewis vs daniel cormier, look at cormier's entries
ffighter = 'Paulie Malignaggi'
# Paulie Malignaggi: no power in his punches, just lots of skill
#  - Miguel Cotto vs. Paulie Malignaggi #   06.10.2006
# Takanori Gomi's feet would fly all over while punching
# Miguel Baeza UFC Tampa Leg kick
# Edson Barboza: leg kicks
#  - Rafaello Oliveira
#  - Gilbert Melendez
# Sanda, previously Sanshou
# Romanov vs one before Espino
# Frank Lobman
# John L. Sullivan Boxer
# Duke Roufus : Kickboxing coach
# Kamarudeen Boyefio
# Naoya Inoue
# UFC 249: Henry Cejudo vs. Marion Moraes
#
# --- Jack Slack: The Fight Primer ---
# ===Badr Hari==
#  - used cross hand trap/Dutch hand trap
#  - Barney Ross: most dangerous punch in boxing?
#    A: head left, right straight down the middle, response to right hook
#  - kickboxer vs mma Japan New Years Eve card
#    - Masato Kobayashi
#  - Semmy Schilt: perhaps the greatest kickboxing heaveyweight ever
#    - 7 ft. 300+ pounds, awkward style
#  - K-1 fell apart and fighters went to Glory
#  - Cro Cop
#  - Rico Verhoeven
#  - Kickboxing heavyweight Greats:
#    - Hoost, Schilt, Aerts, Le Banner, Hug, Hari
# ===Tommy Loughran===
# Jabbed like a fencer: what he did, how he won, jab-and-clutch
# Great light heavyweights:
#  - undersized light heavyweight masqueradign as a heavyweight
#  - Bob Foster, Joey Maxim, Archie Moore
#  vs. Primo Carnera: a giant
# ===Jose Napoles=== https://t.co/80C7o8944e
# Kid Gavilan: great fighter. skill and power
# Jose Napoles: Demon on the inside: see vs Ernie Lopez
# Gentleman Jim Corbett
# bolo punch
# Augusto Urbina and his rematch with Hedgemon Lewis—Napoles used this in a
#  fashion similar to Roy Jones Jr. in the 1990
#
# -------------------------------------
# Hideo Tokoro vs. Daisuke Nakamura K-1 2008-12-31
#   K-1 Dynamite 2008   Saitama, Japan
# 4.24.2021 Qileng Aori vs Jeff Molina
# Charles Jourdain vs Marcelo Rojo, Jourdain is skilled fun fighter
#        |- check out more of his fights
# Featherweight -> Heavyweight after ten year retirement
#  - more than double the weight
#
# combat sambo, muay thai on ufc
# invicta fc 39 Pearl Gonzalez vs Leonardo
# some bellator on DAZN, cbs sports network, hulu?, moving to showtime
#
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
# --- end Jack Slack ---

# --------------------------------------------------------------
# ----------------------------- MMA ----------------------------
# --------------------------------------------------------------

# Submission Underground 2016, July
# Promotion Polaris 2015, January
fighter = 'Henry Cejudo'    # 12.13.2014  UFC FOX
fighter = 'Sean Strickland' # 03.15.2014  UFC 171
  # super technical, travels up/down Cali training
fighter = 'Jorge Masvidal'  # 04.20.2013, UFC FOX Bellator since 1
# -- Mark Hunt vs Antonio "BigFoot" Silva
# 'Stephen Thompson (fighter)' # UFC 143 02.04.2012
fighter = 'T.J. Dillashaw'  # UFC FOX 12.03.2011
fighter = 'Tony Ferguson'   # UFC 135 09.24.2011
fighter = 'Donald Cerrone'  # UFC 126 02.05.2011
#   fights with Jamie Varner and Benson Henderson were,
#   and still are classics of the non-UFC genre.
fighter = 'Ben Askren' # Bellator 14  04.15.2010
# ---------- 2010s -------------

# UFC 104: title fight, ring cutoff      12.24.2009
fighter = 'Roy Nelson'      # TUF 10  12.05.2009
fighter = 'Dustin Poirier'     # UFC 125 01.01.2011 Jack Slack's Adv-Strike2.0
                               #         05.16.2009
fighter = 'Juan Espino' # heavy grappler 02.21.2009
fighter = 'Shane Carwin'    # UFC 84  05.24.2008
fighter = 'Cain Velasquez'  # UFC 83  04.19.2008
fighter = 'Conor McGregor'  # Pre-UFC 03.08.2008  UFC 04.06.2013
fighter = 'Chan Sung Jung' # Pancrase 12.16.2007, UFC 12.10.2011
# 'Alexander Gustafsson'       # UFC 105 11.14.2009
#                         Shooto Finland 11.17.2007
fighter = "Shane Burgos"       #         11.09.2007
  # that bellator guys favorite fighter, Michael Chandler
fighter = 'Brock Lesner'    # UFC 81  02.02.2008
#                               Dynamite 06.02.2007
fighter = 'Frankie Edgar'   # UFC 67  02.03.2007
fighter = 'Anthony Pettis'  # UFC 136 10.08.2011, GFS & WEC from 2007
fighter = 'Diego Sanchez'   # UFC 54  08.20.2005
fighter = 'Giant Silva'     # Pride   12.31.2003
fighter = 'Karo Parisyan'   # UFC 09.26.2003 Was good, pain meds ruined him
fighter = 'Lyoto Machida'   # UFC 67  02.03.2007, 2003 before
fighter = 'Georges St-Pierre' # UFC 46  01.31.2004
#                               UCC in  01.25.2002
# --- WEC 2 --- on FP 10.04.2001
fighter = 'Antônio Rodrigo Nogueira'# 07.29.2001 Pride 15, later UFC 73 2001
fighter = 'Hideo Tokoro'    # TFC 1   09.29.2000
fighter='Fedor Emelianenko' #Pride 21 06.23.2002
#         , in Rings from 2000-02.2002   05.21.2000
# ---------- 2000s -------------

fighter = 'Alistair Overeem'#         10.24.1999
fighter = 'Kevin Randleman' # UFC 19  03.05.1999
fighter = 'Badr Hari'       #         02.17.2002 Kickboxing
fighter = 'Chuck Liddell'   # UFC 17  05.15.1998
fighter = 'Matt Hughes (fighter)'#    09.24.1999  UFC 22, lots of others
#              Jeet Kune Do Challenge 1  01.01.1998
# Branko Cikatić does MMA in 1998 (Pride?)
fighter = 'Tito Ortiz'      #         05.30.1997
fighter = 'Randy Couture'   # UFC 13  05.30.1997
#             bounce people off of fence to get past guard
fighter = 'Mark_Kerr_(fighter)'        # 01.19.1997 then UFC 14
                     #-- was one of the best fighters in the world,
                     #-- Vale, UFC, Pride, ADCC, HBO The Smashing Machine
fighter = 'Alexey Oleynik'  #         11.10.1996
# __________at_________   : UFC  10  07.12.1996  ------------------
fighter = 'Kazushi Sakuraba'#         07.14.1996
fighter = 'mirko cro cop'   # Pride   11.03.2001 ufc 67 02.03.2007
#    k-1 Opening Battle                  03.10.1996
fighter = 'frank shamrock' # Pancrase 12.16.1994, ufc 12.21.1997
fighter = 'ken shamrock'   # Pancrase and UFC until Pride in 2000
fighter = 'Bas Rutten'     # Pancrase , ufc 01.08.1999
fighter = 'Branko_Cikatić'
fighter = 'Andy Hug'
fighter = 'Ernesto Hoost'
fighter = 'Peter Aerts'
# ---------- 1990s -------------

# ----------------------------------------------------------------------
#                          CURRENT: 12.08.1993
# ----------------------------------------------------------------------
#        Glory       : 05.26.2012
#        Invicta     : 04.28.2012
#        Strikeforce : 10.07.2006
#        WEC         : 06.30.2001 WEC 1: Prince of Pain
#        ADCC        :   .  .1998
#        Pride       : 10.11.1997  Pride 1
#        UFC         : 07.12.1996  UFC 10
#        UFC         : 12.16.1995  The Ultimate Ultimate
#        K-1         : 04.30.1994  K-1: World Grand Prix 1994
#        Pancrase    : 03.12.1994  Pancrash! 2
#        K-1         : 03.04.1994  K-1: Challenge
#        Pancrase    : 01.19.1994  Pancrash! 1
#    *   K-1         : 12.19.1993  K-2: Grand Prix, Hoost, Hug, Satake
#
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




# --------------------
# --- young bloods ---
# --------------------
fighter = 'loma lookboonmee' # fixed; last fight on espn
# first thai fighter to sign with ufc, had that one match a few before
fighter = 'youssef zalal'   #         02.08.2020, lfa 22 09.08.2017
fighter = 'jimmy crute'     #         07.24.2018
fighter = 'antonina shevchenko' #     06.26.2018
fighter = 'ciryl gane'      #         08.02.2018
# serigne ousmane dia "bombardier / b52"
#      vs konez 05.05.2018;   vs podmore 02.20.2020
fighter = 'liana jojua'             # 09.07.2019 ufc 242
# mariano vs vannata           ufc 234:  02.09.2019
fighter = 'johnny walker (fighter)' # 08.11.2018
fighter = 'sean o\'malley (fighter)'# 03.03.2018 ufc 222
fighter = 'israel adesanya' #         02.11.2018 ufc 221
fighter = 'ian heinisch'   #          07.31.2018 lfa 04.21.2017
#                        great anti-wrestling, will just stand right up
fighter = 'zabit magomedsharipov' #   09.02.2017  acb before that
fighter = 'trevin giles'   #          07.08.2017
#                        power, good striker, someone to watch
fighter = 'cody stamann'  #           07.08.2017 ufc 213
fighter = 'justin gaethje' #          07.07.2017
fighter = 'marlon moraes'  #          06.03.2017 ufc 212
# dominick cruz vs cody garbandt,        12.30.2016 ufc 207
fighter = 'yana kunitskaya' #         11.18.2016 invicta 20
#             keyyah like every time
fighter = 'marvin vettori' #          08.20.2016 italian middleweight
# jack slack starts at ufc 202           08.20.2016
fighter = 'curtis blaydes'  #         04.10.2016
fighter = 'kamaru usman'    #         12.19.2015
fighter = 'felicia spencer' #         09.12.2015 invicta 14
fighter = 'arnold allen (fighter)' #  06.20.2015
fighter = 'danny henry' # anacondas   06.06.2015 efc 57, ufc 251
fighter = 'cody garbrandt'  #         01.03.2015 ufc 182
fighter = 'kron gracie' #             12.23.2014
fighter = 'petr yan'  #               06.23.2018
#                siberian league         12.20.2014
fighter = 'seo hee ham' # atom weight 12.12.2014 the ultimate fighter 18
#                                        02.16.2007 deep
fighter = 'colby covington'  #        08.23.2014
fighter = 'carlos diego ferreira' #   06.28.2014
fighter = 'sage northcutt'  #         04.20.2014 ufc 192: 10.03.2015
fighter = 'aljamain sterling'#        02.22.2014
fighter = 'ottman azaitar'   #        01.15.2014 temp removed from ufc
# -- a bad man, ko power, man with a bag sneaked into room
fighter='bethe correia'      #        12.07.2013 jack slack funny chant
fighter = 'song yadong'      #        11.25.2017
#                 ruff 9                 05.18.2013
fighter = "uriah hall"       #        04.13.2013
fighter = 'neil magny'       #        02.23.2013 ufc 157
fighter='robert whittaker (fighter)'# 12.15.2012
fighter = 'tim elliott' #             05.05.2012 no respect, love it
fighter = 'cub swanson' # fierce look 11.12.2011

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



# --------------------------------------------------------------
# -------------------------- GRAPPLING -------------------------
# --------------------------------------------------------------
# Hideo Tokoro, more MMA

# --------------------------------------------------------------
# ------------------------- KICKBOXING -------------------------
# --------------------------------------------------------------
fighter = 'Tyrone Spong' # (youtube) & MMA & boxing  # 2003

# --------------------------------------------------------------
# ------------------------ MUAY THAI ---------------------------
# --------------------------------------------------------------
# Rambaa Somdet  : greatest strawweight in MMA, Muay Thai
fighter = 'Rafael Fiziev' #  kicks Hard, Muay Thai background so...
# heavyweight Gane, muay thai -> boxing, bad when trying to hit hard

# --------------------------------------------------------------
# --------------------  CURRENTLY WATCHING  --------------------
# ---------------------------- BOXING --------------------------
# --------------------------------------------------------------
#
# https://www.theguardian.com/sport/2021/may/27/time-to-find-out-who-cares-box\
#ing-brain-damage-tris-dixon
#
# --- Bert Sugar ---
# GSP vs Josh Koscheck
# GGG vs Daniel Jacobs, DAZN USA YOUTUBE
# https://www.youtube.com/watch?v=4VfPtgFEXYc
# Wilfred Benítez vs. Sugar Ray Leonard
#
# Josh Warrington vs Lara DAZN event, the other fights
# https://boxrec.com/en/event/836382
# Michael Hunter: Heavyweight American
# Andy Ruiz Jr. : Heavyweight American
# Pacman

# --- Career Watch ---
fighter = 'Anthony Joshua' # |     1 | Emanuele Leo        | 10.05.2013 |
fighter = 'Deontay Wilder' # |     4 | Joseph Rabotte      | 04.24.2009 |
fighter = 'Tyson Fury'     # |     1 | Béla Gyöngyösi      | 12.06.2008 |
fighter = 'Floyd Mayweather Jr.' #|36| Zab Judah           | 04.08.2006 |
fighter = 'Andre Ward'     # |     1 | Chris Molina        | 12.18.2004 |
fighter = 'Bernard Hopkins'# |     1 | Clinton Mitchell    | 10.11.1988 |
fighter = 'Mike Tyson'     # |     1 | Hector Mercedes     | 03.06.1985 |

# -- Historical
fighter = 'Archie Moore'   # The (Old) Mongoose, Jack Slack likes
fighter = 'Buster Douglas'
fighter = 'Roy Jones Jr.'
fighter = 'Charley Burley'
ffighter = 'Gene Fullmer'
fighter = 'Pernell Whitaker' # Elite, defensive talent
fighter = 'Guillermo Rigondeaux' # ducked?
fighter = 'Aaron Pryor' # two battles with Alexis Arguello
# -- other historical
fighter = 'Jess Willard'  # tofix
# Jack Johnson
# -----
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
# Nonito Donaire vs. Nordine Oubaali
#
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
# - [ ] Josh Warrington vs Carl Frampton     #  12.22.2018
# - [ ] Dillian Whyte vs Dereck Chisora II   #  12.22.2018
fighter = 'Jermall Charlo'                   #  12.22.2018
fighter = 'Jermell Charlo'                   #  12.22.2018
fighter = 'Josh Warrington'                  #  12.22.2018 ! 2009 start
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
fighter = 'Gennady Golovkin'                #  09.15.2018 DAZN  # 2006 start
fighter = 'Canelo Álvarez'                   #  09.15.2018 DAZN
fighter = 'Rom%C3%A1n_Gonz%C3%A1lez_(boxer)' #  09.15.2018  # chocolatito
fighter = 'Vergil Ortiz Jr.'                 #  09.15.2018 YT no DAZN til 2019
fighter = 'José Ramírez (boxer)'             #  09.14.2018
fighter = 'Amir Khan (boxer)'                #  09.08.2018 vs Samual Vargas
fighter = 'Shawn Porter'                     #  09.08.2018
fighter = 'Lewis Ritson'                     #  09.08.2018
fighter = 'Ryan García'                      #  09.01.2018 YT Morales
fighter = 'Carl Frampton'                    #  08.18.2018 Jackson
fighter = 'Shakur Stevenson'                 #  08.18.2018 YT post 07.2019 ESPN
fighter = 'Sergey Kovalev'                   #  08.05.2018
# devin alexander vs. aundr bird spence      #  08.05.2018
# 08.04.2018
#  Kovalev vs. Eleidar Alvarez
fighter = 'Dmitry Bivol'                   # vs. TBA
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
fighter = 'Mark Coleman'                     #  11.09.2007
fighter = 'Chris Eubank Jr' # vs Groves #  02.17.2018   # 09.28.2018
fighter = 'Keith Thurman'
# 06.24.2016 Shawn Porter    #  03.04.2017 vs Danny Garcia
# ------------------------- 07.14.2018 current -------------------------
# April-June 2018 on DAZN:
#   Buatsi vs. Cuevas, Munguia vs. Ali, Okolie vs. Watkins
#   Vergil Ortiz Jr. vs. Juan Carlos Salgado

# YT  = Young Talent
# SFL = Saturday Fight Live on DAZN
#
# --Classic--
# Andre Berto vs. Victor Ortiz
# GGG vs. Daniel Jacobs 3.18.2017
# Errol Spence Jr. vs Kell Brook 05.27.2017

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
