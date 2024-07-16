import sys
import fighter as ft
import fightEvent as fe

event_bool = True
event_bool = False

#
# Luke grew up on Frank Bruno, Chris Eubank, Nigel Benn, Barry McGuigan, Joe
# Calzaghe, and then Naseem Hamed
#

# --- Careers ---
# | Nayoa Inoue |
# | |

# --------
# | 2024 |
# --------
# - catch-up -
# Shakur Stevenson vs. A. Harutyunyan | 07.06.2024 |
# Zhilei Zhang vs. Joseph Parker      | 06.01.2024 |
# Dmitry Bivol vs. Malik Zinad        | 06.01.2024 |
# Sergey Kovalev vs. R. S. Safar      | 05.18.2024 | Yarde 2019, Pulev2022
# Emanuel Navarrete vs. D. Berinchyk  | 05.18.2024 |
# Moses Itauma vs. Ilja Mezencev      | 05.18.2024 |
# Nina Hughes vs. Cherneka Johnson    | 05.12.2024 |
# Naoya Inoue vs. Luis Nery           | 05.06.2024 |
# Canelo Alvarez vs. Jaime Munguía    | 05.04.2024 |
# Joey Dawejko vs. Walter Burns       | 04.27.2024 |
# Ryan Garcia vs. Devin Haney         | 04.20.2024 |
# Prince Patel vs. Ryad Merhy         | 04.13.2024 |
# Jared Anderson vs. Ryad Merhy       | 04.13.2024 |
# Fabio Wardley vs. Frazer Clarke     | 03.31.2024 |
# Moses Itauma vs. Dan Garber         | 03.22.2024 |
# Anthony Joshua vs. Francis Ngannou  | 03.08.2024 |
# Zhilei Zhang vs. Deontay Wilder     | 03.08.2024 |
# Shields vs. Kelsey DeSantis         | 02.24.2024 | PFL
# Adam Azim vs. Enock Poulsen         | 02.03.2024 |
# Joey Dawejko vs. Malik Titus        | 01.13.2024 |
# Karriss Artingstall v.L.d.S.Furtado | 01.20.2024 |
# Callum Smith vs. Artur Beterbiev    | 01.13.2024 | **

# *Hatton Documentary*
# December  21, 2023 "Homicide Hank" article in Boxing News
# December  21, 2023 "I took a huge chunk out of his neck" article in Boxing News
# December  21, 2023 "Murdered in Manhattan" article in Boxing News
# November   9, 2023 "The Bloodiest of Battles" article in Boxing News
# November   2, 2023 "Don't You Quit" article in Boxing News
# November   2, 2023 "The Fall" article in Boxing News
# September 21, 2023 "Boxing and PEDs in 2023" article in Boxing News

# --------
# | 2023 |
# --------
#
# Nayoa Inoue vs. Marlon Tapales              | 12.26.2023 | [ ] | **
# Dmitry Bivol vs. Lyndon Arthur              | 12.23.2023 | [ ] |
# Anthony Joshua vs. Otto Wallin              | 12.23.2023 | [ ] | **
# Deontay Wilder vs. Joseph Parker            | 12.23.2023 | [ ] | **
# Sunny Edwards vs. Jesse Rodriguez           | 12.16.2023 | [ ] | **
# Devil Haney vs. Regis Prograis              | 12.09.2023 | [ ] | **
# Robeisy Ramirez vs. Rafael Espinoza         | 12.09.2023 | [ ] | **
# Chris Billiam-Smith vs. Mateusx Masternak   | 12.09.2023 | [ ] |
# Matt Windle vs. Craig Derbyshire            | 12.09.2023 | [ ] |
# Joey Dawejko vs. Jesse Bryan                | 12.09.2023 | [ ] |
# Ryan Garcia vs. Oscar Duarte                | 12.02.2023 | [ ] |
# Lani Daniels vs. Desley Robinson            | 12.02.2023 | [ ] | heavy?
# Lauren Parker vs. Giueseppina Di Stefano    | 12.02.2023 | [ ] |
# Moses Itauma vs. Michal Boloz               | 12.01.2023 | [ ] |
# Gary Cully vs. Reece Mould                  | 11.25.2023 | [ ] |
# Jermall Charlo vs. José Benavidez Jr.       | 11.25.2023 | [ ] |
# Katie Taylor vs. Chantelle Cameron          | 11.25.2023 | [ ] |
# Nick Ball vs. Isaac Dogboe                  | 11.18.2023 | [ ] | * Whole Manchester Show
# Emanuel Navarrete vs. Robson Conceição      | 11.16.2023 | [ ] |
# Shakur Stevenson vs. Edwin De Los Santos    | 11.16.2023 | [ ] |
# Harlem Eubank vs. Timo Schwarzkopf          | 11.10.2023 | [ ] |
# Adam Azim vs. Franck Petitjean              | 11.10.2023 | [ ] |
# Joe Cordina vs. Edward Vazquez              | 11.04.2023 | [ ] |
# Tyson Fury vs. Francis Ngannou              | 10.28.2023 | [ ] | **
# Eduardo Hernandez vs. O'Shaquie Foster      | 10.28.2023 | [ ] | **
# Fabio Wardley vs. David Adeleye             | 10.28.2023 | [ ] |
# Moses Itauma vs. István Bernáth             | 10.28.2023 | [ ] |
# Tim Tszyu vs. Brian Mendoza                 | 10.14.2023 | [ ] |
# Leigh Wood vs. Josh Warrington              | 10.07.2023 | [ ] | ** DAZN probs
# Gilberto Ramirez vs. Joe Smith Jnr.         | 10.07.2023 | [ ] | G. moving to cruiser
# Emma Dolan vs. Nicola Hopewell              | 10.07.2023 | [ ] |
# Terri Harper vs. Cecilia Braekhus           | 10.07.2023 | [ ] |
# Canelo Alvarez vs. Jermell Charlo           | 09.30.2023 | [ ] |
# Jordan Thompson vs. Jai Opetaia             | 09.30.2023 | [ ] |
# Sandy Ryan vs. Jessica McCaskill            | 09.23.2023 | [ ] |
# Moses Itauma vs. Amine Boucetta             | 09.23.2023 | [ ] |
# Kenshiro Teraji vs. Hekkie Budler           | 09.18.2023 | [ ] | Japan vs. South Africa
# Jay McFarlane vs. Mohammad Saleem           | 09.08.2023 | [ ] | Scottish heavy
# Lyndon Arthur vs. Braian Nahuel Suarez      | 09.01.2023 | [ ] |
# Ricky Burns vs. Willie Limond               | 09.01.2023 | [ ] | two Scottish legends
# Oleksandr Usyk vs. Daniel Dubois            | 08.26.2023 | [-] | for "the punch"
# Jared Anderson vs. Andriy Rudenko           | 08.26.2023 | [ ] |
# Lani Daniels vs. Razel Mohammed             | 08.26.2023 | [ ] | heavy
# Prince Patel vs. Andriy Rudenko             | 08.26.2023 | [ ] |
# Dennis McCann vs. Ionut Baluta              | 08.18.2023 | [ ] | put show on background, DAZN?
# Terence Crawford vs. Errol Spence           | 07.29.2023 | [ ] |
# Moses Itauma vs. Kevin Nicolas Espindola    | 07.29.2023 | [ ] |
# Alycia Baumgardner vs. Christina Linardatou | 07.15.2023 | [ ] |
# George Kambosos vs. Maxi Hughes             | 07.15.2023 | [ ] | ESPN, main
# Keyshawn Davis vs. Francesco Patera         | 07.15.2023 | [ ] | Cuban vs. Bulgerian, heavy, ESPN
# Nigel Collins vs. Jaron Ennis               | 07.08.2023 | [ ] |
# Savannah Marshall vs. Franchon Crews-Dezurn | 07.01.2023 | [ ] | *
# Dalton Smith vs. Sam Maxwell                | 07.01.2023 | [ ] |
# Jared Anderson vs. Charles Martin           | 07.01.2023 | [ ] |
# Prince Patel vs. Charles Martin             | 07.01.2023 | [ ] |
# Miranda Reyes vs. Joshua Franco             | 06.24.2023 | [ ] |
# Regis Prograis vs. Danielito Zorrilla       | 06.24.2023 | [ ] |
# Tim Tszyu vs. Ocampo                        | 06.17.2023 | [ ] |
# Sunny Edwards vs Andres Camposa [DAZN]      | 06.10.2023 | [ ] | *
# Nina Hughes vs. Katie Healy                 | 06.10.2023 | [ ] |
# Lani Daniels vs. Alrie Meleisea             | 05.27.2023 | [ ] | IBF inagural heavyweight
# Canelo Alvarez vs. John Ryder               | 05.06.2023 | [ ] |
# Moses Itauma vs. Kostiantyn Dovbyshchenko   | 04.15.2023 | [ ] |
# Prince Patel vs. George Arias               | 04.08.2023 | [ ] |
# Jared Anderson vs. George Arias             | 04.08.2023 | [ ] |
# === FUTURE ===
# Deontay Wilder vs. Joseph Parker    | 12.23.2023 |
# Anthony Joshoa vs. Otto Wallin      | 12.23.2023 |

# --- Best Of ---
# | Callum Smith vs. Artur Beterbiev            | 01.13.2024 | [ ] |
# | Nayoa Inoue vs. Marlon Tapales              | 12.26.2023 | [ ] |
# | Anthony Joshua vs. Otto Wallin              | 12.23.2023 | [ ] |
# | Deontay Wilder vs. Joseph Parker            | 12.23.2023 | [ ] |
# | Tyson Fury vs. Francis Ngannou              | 10.28.2023 | [ ] |
# | Zhilei Zhang vs. Joe Joyce                  | 09.23.2023 | [X] |
# | Nayoa Inoue vs. Stephen Fulton              | 07.25.2023 | [-] |
# | Terence Crawford vs. Errol Spence           | 07.29.2023 | [ ] |
# | Claressa Shields vs. Maricela Cornejo       | 06.03.2023 | [-] |
# | Alycia Baumgardner vs. Christina Linardatou | 07.15.2023 | [ ] |

# --------------- top fights plus a few ------------------------
# --------------------------------------------------------------
# | Sunny Edwards vs. Jesse Rodriguez       | 12.16.2023 | [ ] |
# | Devil Haney vs. Regis Prograis          | 12.09.2023 | [ ] |
# | Robeisy Ramirez vs. Rafael Espinoza     | 12.09.2023 | [ ] |
# | Eduardo Hernandez vs. O'Shaquie Foster  | 10.28.2023 | [ ] |
# | Leigh Wood vs. Josh Warrington          | 10.07.2023 | DAZN probs
# | Emanuel Navarrete vs. Óscar Valdez      | 08.12.2023 | [X] |
# | Jamie Munguia vs. Sergiy Derevyanchenko | 06.10.2023 | [X] |
# | Devin Haney vs. Vasiliy Lomachenko      | 05.20.2023 | [-] |
# | Shavkatdzhon Rakhimov vs. Joe Cordina   | 04.22.2023 | [x] |
# | Azat Hovhannisyan vs. Luis Nery         | 02.18.2023 | [-] |
# | Emanuel Navarrete vs. Liam Wilson       | 02.03.2023 | [-] |
# | Artur Beterbiev vs. Anthony Yarde       | 01.28.2023 | [X] |
# --------------------------------------------------------------
# | Anthony Joshua vs. Robert Helenius      | 08.12.2023 | [X] |
# --------------------------------------------------------------
# Robelis Despaigne vs. Katuma Mulumba| 06.03.2022 |
# --- Young Bloodz ---
# Moses Itauma, Abdullah Mason, Ben Whittaker, Curmel Moton, Elijah Garcia
# --------------------
# Book: Tales of Pugilism

# just random fights
# | Emanuel Navarrete vs. Robson Conceição           | 11.16.2023 |
# | Robeisy Ramirez vs. Satoshi Shimizu         | 07.25.2023 |
# | Sunny Edwards vs. Andres Campos          | 06.10.2023 |
# | Robeisy Ramirez vs. Isaac Dogboe            | 04.01.2023 |
# |  Anthony Yard vs. Jorge Silva             | 09.23.2023 |
# fighter = 'Robeisy Ramirez'

# catch-up as it happens
# Sunny Edwards vs Andres Camposa [DAZN] | 06.10.2023 | [ ] |



#
#
# ---------
# | HATCH |
# ---------
# Jack Dempsey and his Championship Fighting
# Salvador Sanchez
# Alexis Arguello
# Andre Ward
# Vasiliy Lomachenko
# Eder Jofre
# Seniesa Estrada
# Rocky Marciano
#  vs Joe Louis
#  vs Ezzard Charles
# Ryan Garcia
# Tony Bellew
# Andre Berto
# Earnie Shavers
# Sugar Ray Robinson
# Marvin Hagler
# Harold Johnson (boxer)
# Tommy Dix
# Robson Conceicao
# Montell Griffin
# Paul Williams (boxer)
# James Toney
# Joe Joyce
# Daniel Dubois
# Shane McGuigan
# Jorge Linares vs Luke Campbell 2019
# Kell Brook
#
# =contemporary=
# Jesse 'Bam' Rodriguez vs Gonzalez
#
# =Trainer=
# Don Turner
# Emanuel Steward: Kronk Gym
# Eddie Futch
# James Ali Bashi: Usyk's former trainer
#
# =MMA/Kickboxing=
# Bas Rutten, liver rupture kick
#
# =Writers=
# A.J. Liebling
# Tris Dixon
# Rachel Charles: promoter, daughter and ex-wife of drummers
# Jerry Izenberg
# Montell "Ice" Griffin: The Ice Life
#
# Fader vs Big Foot Silva
#
#
# ---------
# | INDEX |
# ---------
# | TODO  |
# ---------
# how to watch boxing in 2023: the ring
# --------------------------- TRAINING ---------------------------
# Salvador Sanchez
# Alexis Arguello
# Roberto Duran
# Tommy Hearns
# ---------------------------- EVENTS ----------------------------
# 05.20.2023 Devin Haney vs. Vasiliy Lomachenko
# 04.22.2023 Gervonta "Tank" Davis vs Ryan Garcia

# 04.08.2023 Yigit vs Davis  Anderson vs Arias [ESPN]
# 03.25.2023 Benavidez vs. Plant [SHOW PPV]
# 03.18.2023 5 Ramirez vs 24 Rosado [DAZN PPV]
# 03.11.2023 Daranyi vs Navarrete [DAZN]
# NOW: 11.30.2022
#   - Whyte vs Franklin, [DAZN]
fighter = 'Adam Azim'    # 12.02.2020 | Ed Harrison
fighter = 'Viddal Riley' # 02.11.2023 | Anees Taj
                         # 11.12.2022 | Ross McGuigan
# 12.13.2022 [ESPN] Naoya Inoue vs. Butler
# 08.26.2022 | Murat Gassiev vs. Carlouse Welch
# --- boxing for the weekend ---
# Thursday [D] Diaz Jr. vs Gesta, Indio, CA
# - catchup -
# 04.16.2022 Cunningham vs Couviour [BT Sport]
# 04.16.2022 Spence vs Ugas [SHOW]?
# 04.02.2022 Marshall vs Hermans [SKY]
fighter = 'Hannah Rankin' # 09.25.2022 | Terri Harper
        # one-woman symphony: The Ring article


# - pay attention for: Pacheco
# - Past -
# Fraizer vs Ali II : short vs tall stance
# Serrano vs Cruz [DAZN] Baumgardner vs Mekhaled super feather
# Eubank vs Smith ~ Jan 21 [DAZN] 2 other goood fights
# Lubin vs Fundora [SBOX]
# Fundora vs Ocampo 10.08.2022
# Frazer Clarke
# Karriss Artingstall 05.27.2023, update wiki, Okolie vs. Billam-Smith under
#
# Mike Tyson, Larry Holmes, Evander Holyfield, Lennox Lewis, George Foreman
#   Roy Jones Jr., Bernard Hopkins, Joe Frazier
#
# Defensive Tacticians: Hopkins, Mayweather, Ward
# Boxer-Punchers: De La Hoya, Keith Thurman, Fernando Vargas, Danny Garcia
#
# Mexican Style" I think of fighters like Juan Manuel Marquez, Erik Morales,
#   Marco Antonio Barerra, Finito Lopez
#
# Stances:
#   - bladed: long range, in and out Ward, Mayweather
#   - balanced: pressure in and out: Bernard Hopkins, Coto a bit
#   - pressure: Julio Cesar Chavez, Mike Tyson, Joe Frazier
#               squared up for good side to side
#
# Frazier vs Foreman: one of the best rounds in history
#
# Artur Beterbiev boxing style
# Contemporary:
#   - Garcia vs. Benavidez Showtime
#   - Garcia vs. Fortuna DAZN
#   - Beterbiev vs. Smith Jr. ESPN
#   - Kambosos Fr vs. Haney ESPN
#   - Valdez vs. Stevenson  ESPN
#   - Fury vs. Whyte  ESPN
#   - Magsayo vs. Vargas  Showtime
#
#   - Kubrat Pulev vs Frank Mir
#   - Parter vs. Spence Jr. ESPN
#   - 11.13 Holloway vs. Rodriguez, Prelims too
#   - Zepeda vs Vargas, Caraballo vs Sultan  ESPN
#   - Lomachenko vs Commey ESPN 12.11.2021
fighter = 'Román_González_(boxer)'
fighter = 'Srisaket Sor Rungvisai'
fighter = 'Max Holloway'


#
# Ricardo Cervantez, dad is Rico from Martinez, CA
# 3rd in Junior Mens 138 division
#
# 05.15.2021 DAZN to see Dalton Smith
# watch maincards UFC on ESPN: Holm vs. Aldana
# Invicta Fighting Phoenix
# event = 'UFC on ESPN: Blaydes vs. Volkov'
event = 'UFC_on_ESPN:_Kattar_vs._Ige'
event = 'UFC 141'
event = 'UFC Fight Night: Brunson vs. Holland'
event = 'UFC 269'
event = 'UFC Fight Night: Lewis vs. Daukaus' # watch prelims! Tafa, Leavitt
event = 'UFC 276' # lawler fight good
event = 'UFC 300'
## more of the ill follow you home and kill you - Montserrat Ruiz
#  invicta 33, 41
# event = 'UFC on ABC: Vettori vs. Holland' # On holtzman vs gamrot in prelims
#
# --- To Process ---
# Viacheslav Borshchev new to UFC, Russian dancer

# Austin Hubbard
# Zhang Zhilei: Chinese Boxer
# Liam Williams vs Eubank Jr.
# Joel Diaz
# Question mark kick pantheon level ingorance
# Victor Henry: foundation: catch wrestling, skillz, constant pressure, coach
#
# Khaosai Galaxy: The Thai Tyson
#
# - to process boxing -
# Ronald Winky Wright: master of high guard, very good boxer, career 1990-2012

# - current -
# Victor Henry vs. Raoni Barcelos ; UFC 270 prelims
# Katsunori Kikuno, MMA exhibition vs. Yuichiro Nagashima, vs. Ferguson
# Arlovski vs. Cruz, Berb Dean, UFC 66



#
# ------- OLYMPIC BOXING: TOKYO EDITION -------
#
# to catch up on, Vettori vs Holland, and this
# event = 'UFC 263' # prelims?
# event = 'UFC 262' # Prelims: Submissions!
# event = 'UFC 260' # prelims?
# event = 'UFC 257' # prelims
# event = 'UFC Fight Night: Thompson vs. Neal' # should watch prelims
# event = 'UFC Fight Night: Blaydes vs. Lewis' # should watch prelims
# -- look into --
# Chute Boxe Academy: hard training
# Prince Naseem Hamed





# --------------------------------------------------------------
# ------------------------- JACK SLACK -------------------------
# --------------------------------------------------------------
# 04.10.15 https://www.vice.com/en/contributor/jack-slack?page=32
#
# Bruce Lee: boxing of Edwin Haislet, the philosophies of Jiddu Krishnamurti
#
# overeem vs Hordijk  03.14.1999

# 2005 Pride Middleweight Grand Prix: best MMA of all time - Jack Slack
# 2005 Mauricio 'Shogun' Rua and Antonio Rogerio Nogueira, one of the greatest
#   fights in MMA history

# https://www.vice.com/en/article/nzpaxb/rousimar-palhares-too-dangerous-for-mma
# Saturday night's grappling clinic between Rousimar Palhares and Jake Shields
#   was unfortunately undermined by accusations of foul play. We take a look at
#   both men's history of questionable behavior.

# yoshida vs silva for stomp attempt
fighter = 'Parker Porter' # vs Alan Baudot|UFC Fight Night| 02.19.2022
fighter = 'Gavin Tucker'   # 08.08.2020 vs Jaynes  a banger fun fight
                           # both do weird intesting stuff
fighter = 'Khaos Williams' # 02.08.2020 watch 247 prelims with him,
                           # check KO all hassen
fighter = 'Rin Nakai'      # 10.01.2006 Pacrase 167,
                           # check UFC
fighter = 'Arjan Bhullar' # 05.04.2019 vs Juan Adams
# "Good on Arjan Bhullar. I've liked him since he headbutted Juan Adams"
#                          - Jack Slack
fighter = 'Daniel Cormier' # 11.03.2018 | UFC 230
# derrick lewis vs daniel cormier, look at cormier's entries
fighter = 'Paulie Malignaggi'
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
# UFC 249: Henry Cejudo vs. Marion Moraes
# Marlon Vera : good clincher
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

# --- Denver ---
# Austin Hubbard, Elevation Fight Team
# Vinc Pichel

# -- Process --
# UFC: Barboza vs Chikadze
# Barboza leg kick finish
# Fabricio Werdum
# Julio Cesar La Cruz
# Tishchenko, controversially won gold


# --------------------------------------------------------------
# ----------------------------- MMA ----------------------------
# --------------------------------------------------------------

# Newer
fighter = 'Robelis Despaigne' # vs Katuma Mulumba 06.03.2022

fighter = 'Kazuto Ioka'
# Submission Underground 2016, July
# Promotion Polaris 2015, January
fighter = 'Henry Cejudo'    # 12.13.2014  UFC FOX
fighter = 'Sean Strickland' # 03.15.2014  UFC 171
  # super technical, travels up/down Cali training
fighter = 'Jorge Masvidal'  # 04.20.2013, UFC FOX Bellator since 1
# -- Mark Hunt vs Antonio "BigFoot" Silva
# 'Stephen Thompson (fighter)' # UFC 143 02.04.2012
fighter = 'Jorina Baars'    # 09.08.2012 K-1 Muay Thai
fighter = 'T.J. Dillashaw'  # 12.03.2011 UFC FOX
fighter = 'Tony Ferguson'   # 09.24.2011 UFC 135
fighter = 'Donald Cerrone'  # 02.05.2011 UFC 126
#   fights with Jamie Varner and Benson Henderson were,
#   and still are classics of the non-UFC genre.
fighter = 'Ben Askren'      # 04.15.2010 Bellator 14
# ------------------------------
# ---------- 2010s -------------
# ------------------------------
fighter = 'Michihiro Omigawa'
# 12.24.2009 UFC 104: title fight, ring cutoff
fighter = 'Roy Nelson'      # 12.05.2009 TUF 10
fighter = 'Hideki Sekine'   # 09.27.2009 vs Yasuro Urayama
fighter = 'Dustin Poirier'  # 01.01.2011 UFC 125 Jack Slack's Adv-Strike2.0
                            # 05.16.2009
fighter = 'Juan Espino'     # 02.21.2009 heavyweight grappler
fighter = 'Shane Carwin'    # 05.24.2008 UFC 84
fighter = 'Cain Velasquez'  # 04.19.2008 UFC 83
fighter = 'Conor McGregor'  # 03.08.2008 Pre-UFC UFC 04.06.2013
fighter = 'Chan Sung Jung'  # 12.16.2007 Pancrase, 12.10.2011 UFC
fighter = 'Alexander Gustafsson'
                            # 11.14.2009 UFC 105
                            # 11.17.2007 Shooto Finland
fighter = 'Shane Burgos'    # 11.09.2007
  # that bellator guys favorite fighter, Michael Chandler
fighter = 'Rico Verhoeven'  # 02.17.2008 K-1
fighter = 'Brock Lesner'    # UFC 81  02.02.2008
#                            Dynamite 06.02.2007
fighter = 'Frankie Edgar'   # UFC 67  02.03.2007
fighter = 'Giorgio Petrosyan'#        04.14.2007, K-1
fighter = 'Anthony Pettis'  # UFC 136 10.08.2011, GFS & WEC from 2007
fighter = 'Diego Sanchez'   # UFC 54  08.20.2005
fighter = 'Michihiro Omigawa' # 05.22.2005 PRIDE
fighter = 'Buakaw Banchamek'# 04.07.2004 K-1, Muay Thai before
fighter = 'Giant Silva'     # Pride   12.31.2003
fighter = 'Karo Parisyan'   # UFC 09.26.2003 Was good, pain meds ruined him
fighter = 'Clay Guida'      # 07.26.2003 Adam Copenhaver
fighter = 'Forrest Griffin' # 10.27.2001
fighter = 'Lyoto Machida'   # UFC 67  02.03.2007, 2003 before
fighter = 'Georges St-Pierre' # UFC 46  01.31.2004
#                               UCC in  01.25.2002
# --- WEC 2 --- on FP 10.04.2001
fighter = 'Antônio Rodrigo Nogueira'# 07.29.2001 Pride 15, later UFC 73 2001
fighter = 'Frank Mir'        # 07.14.2001 SF 11
fighter = 'Hideo Tokoro'     # 09.29.2000 TFC 1
fighter= 'Fedor Emelianenko' # 06.23.2002 Pride 21
#         , in Rings from 2000-02.2002   05.21.2000
fighter = 'Mark Hunt'       # 02.27.2000 K-1, 2004 Pride, 2008 Dream, 2010 UFC
# ------------------------------
# ---------- 2000s -------------
# ------------------------------
fighter = 'Alistair Overeem' # 03.14.1999 Kickboxing, 10.24.1999 MMA
fighter = 'Kevin Randleman'  # 03.05.1999 UFC 19
fighter = 'Badr Hari'        # 02.17.2002 Kickboxing
fighter = 'Chuck Liddell'    # 05.15.1998 UFC 17
fight='Matt Hughes (fighter)'# 09.24.1999  UFC 22, lots of others
#    Jeet Kune Do Challenge 1  01.01.1998
# Branko Cikatić does mma in 1998 (Pride?)
fighter = 'Tito Ortiz'       # 05.30.1997
fighter = 'Randy Couture'    # 05.30.1997 UFC 13
#   bounce people off of fence to get past guard
fighter = 'Mark_Kerr_(fighter)' # 01.19.1997 then UFC 14 07.27.1997
                     #-- was one of the best fighters in the world,
                     #-- Vale, UFC, Pride, ADCC, HBO The Smashing Machine
fighter = 'Alexey Oleynik'   # 11.10.1996
fighter = 'Mark Coleman'     # 09.20.1996 UFC 11 #  11.09.2007??
fighter = 'Kazushi Sakuraba' # 07.14.1996
fighter = 'Semmy Schilt'     # 05.16.1996 Pancrase: Truth 5,
                             # UFC & Pride 2001, K-1 2002, Glory 2012
fighter = 'Mirko Cro Cop'    # Pride 11.03.2001 ufc 67 02.03.2007
#                             K-1   03.10.1996 opening battle
fighter = 'Frank Shamrock'   # Pancrase 12.16.1994, ufc 12.21.1997
fighter = 'Ken Shamrock'     # Pancrase and UFC until Pride in 2000
fighter = 'Bas Rutten'       # Pancrase , ufc 01.08.1999
fighter = 'Branko_Cikatić'   # K-1
fighter = 'Andy Hug'         # K-1 career
fighter = 'Ernesto Hoost'    # K-1 career
fighter = 'Peter Aerts'      # 04.30.1994, K-1 until 2012
# 1996: K-1 starts on UFC
# ---------- 1990s -------------

# ----------------------------------------------------------------------
#                          CURRENT: 10.15.1994
# ----------------------------------------------------------------------
#
#        Glory       : 05.26.2012
#        Invicta     : 04.28.2012
#        Strikeforce : 10.07.2006
#        WEC         : 06.30.2001  WEC 1: Prince of Pain
#        ADCC        :   .  .1998
#        Pride       : 10.11.1997  Pride 1
#        UFC         : 09.20.1996  UFC 11
#        K-1         : 1995 Five Events
#        Pancrase    : 1995 Eyes of Beast 1-7 & Neo-Blood Tournament
#        Pancrase    : 12.1[6-7].1994 King of Pancrase
#        K-1         : 12.10.1994  Legend
#    *   Pancrase    : 10.15.1994  Road to the Championship 5
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
fighter = 'Loma Lookboonmee'
# first thai fighter to sign with ufc, had that one match a few before
fighter = 'Paddy Pimblett'
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
fighter = 'uriah hall'       #        04.13.2013
fighter = 'neil magny'       #        02.23.2013 ufc 157
fighter='robert whittaker (fighter)'# 12.15.2012
fighter = 'tim elliott' #             05.05.2012 no respect, love it
fighter = 'Cub Swanson' #   11.12.2011  fierce look

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
# Hideo Tokoro, more mma

# --------------------------------------------------------------
# ------------------------- KICKBOXING -------------------------
# --------------------------------------------------------------
fighter = 'Tyrone Spong' # (youtube) & mma & boxing  # 2003
fighter = 'Filip Verlinden'  # artless: adding kickboxing

# --------------------------------------------------------------
# ------------------------ MUAY THAI ---------------------------
# --------------------------------------------------------------
# Saenchai : a great, great at pull-counter
# Rambaa Somdet  : greatest strawweight in MMA, Muay Thai
fighter = 'Rafael Fiziev' #  kicks Hard, Muay Thai background so...
# heavyweight Gane, muay thai -> boxing, bad when trying to hit hard
# Ramon Dekkers, exciting Dutchman in Thailand, watch highlights

# --------------------------------------------------------------
# -------------------------- BOXING ----------------------------
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
# Pacman
# Young Bloods: Figueroa
fighter = 'Emanuel Navarrete' # long arms, unorthodox, fun
fighter = 'Francis Ngannou'
fighter = 'Galal Yafai'    # British gold metalist
fighter = 'Atif Oberlton'  # fashion designer as well
fighter = 'Richard Torrez' # 2020 silver medalist
fighter = 'Roiman Villa'   # Venezuelan, round 12 2-knockdown comeback
fighter = 'John Hedges'    # U.K. long hingy fighter
fighter = 'Jaron Ennis'    # | Karen Chukhadzhian | 01.07.2023 |
                           # | Custio Clayton     | 05.14.2022 |
fighter = 'Brandun Lee'    # | Diego Luque        | 01.07.2023 |
fighter = 'John Ramirez'   # | Ronal Batista      | 10.12.2023 | DAZN


# ---------------------------
# ------ Career Watch -------
# ---------------------------
#------------------------------------------------------------------------
fighter='Caroline Dubois (boxer)'
# |9| Miranda Reyes             | 02.03.2024 | [ ] |
# |8| Magali Rodriguez          | 09.30.2023 | [ ] |
# |7| Yanina del Carmen Lescano | 07.16.2023 | [ ] |
# |6| Feriche Mashaury          | 02.11.2023 | [ ] |
# |5| Sofia Rodriguez           | 12.17.2022 | [ ] |
# |4| Milena Koleva             | 10.16.2022 | [ ] |
# |3| Happy Daudi               | 07.30.2022 | [ ] |
# |2| Martina Horgasz           | 03.26.2022 | [ ] |
# |1| Vaida Masiokaite          | 02.05.2022 | [X] |

fighter = 'Zhilei Zhang'   # |     1 | Curtis Lee Tate     | 08.08.2014 |
fighter = 'Anthony Joshua' # |     1 | Emanuele Leo        | 10.05.2013 |
fighter = 'Dmitry Bivol'   # |     1 | Jorge Olivera       | 12.23.2016 |
#          Vasyl Lomachenko  |     1 | José Luis Ramírez   | 10.12.2013 |
#          Oleksandr Usyk    |     1 | Felipe Romero       | 09.11.2013 |
#          Artur Beterbiev   |     1 | Christian Cruz      | 06.08.2013 |
#          Errol Spence Jr.  |     1 | Jonathan Garcia     | 11.09.2012 |

#          Naoya Inoue       |     1 | Crison Omayao       | 10.02.2012 |
fighter = 'Guillermo Rigondeaux'#| 1 | Juan Noriega        | 05.22.2009 |
# Cuban big threat who was avoided
fighter = 'Deontay Wilder' # |     4 | Joseph Rabotte      | 04.24.2009 |
fighter = 'Tyson Fury'     # |     1 | Béla Gyöngyösi      | 12.06.2008 |
#          Terence Crawford  |     1 | Brian Cummings      | 03.14.2008 |
fighter = 'Melissa St. Vil'# |     1 | Olivia Fonseca      | 03.30.2007 |
fighter = 'Gennady Golovkin'#|     1 | Gabor Balogh        | 05.06.2006 |
#          Canelo Álvarez    |     1 | Abraham Gonzalez    | 10.29.2005 |
fighter = 'Andre Ward'     # |     3 | Roy Ashworth        | 04.07.2005 |
fighter = 'Timothy Bradley'# |     1 | Francisco Martinez  | 08.20.2004 |
fighter = 'Miguel Cotto'   # |     1 | Jason Doucet        | 02.23.2001 |
fighter = 'Ricky Hatton'   # |     1 | Colin McAuley       | 09.11.1997 |
fighter = 'Juan Manuel Marquez'#| 20 | Cedric Mingosey     | 02.03.1997 |
fighter = 'Vitali Klitschko' # |   1 | Tony Bradham        | 11.16.1996 |
fighter = 'Wladimir Klitschko'#|   1 | Fabian Meza         | 11.16.1996 |
fighter = 'Zab Judah'      # |     1 | Michael Johnson     | 09.20.1996 |
fighter = 'Marco Antonio Barrera'#|35| Daniel C. Jimenez   | 03.31.1995 |
fighter = 'Manny Pacquiao' # |     1 | Edmund E. Ignacio   | 01.22.1995 |
fighter = 'Pongsaklek Wonjongkam'#|1 | Bernardo J. Davalos | 12.21.1994 |
fighter = 'Winky Wright'   # |    26 | Julio Cesar Vasquez | 08.21.1994 |
fighter = 'Shane Mosley'   # |     1 | Greg Puente         | 02.11.1993 |
fighter = 'Oscar De La Hoya'#|     4 | Curtis Strong       | 02.06.1993 |
fighter = 'Naseem Hamed'   # |     1 | Ricky Beard         | 02.14.1992 |
fighter = 'Ricardo López (boxer)'#|27| Hideyuki Ohasi      | 10.25.1990 |
fighter = 'Felix Trinidad' # |     1 | Angel Romero        | 03.10.1990 |
fighter = 'Lennox Lewis'   # |     1 | Al Malcolm          | 06.27.1989 |
fighter = 'Roy Jones Jr.'  # |     1 | Ricky Randall       | 05.06.1989 |
fighter = 'James Toney'    # |     1 | Stephen Lee         | 10.26.1988 |
fighter = 'Bernard Hopkins'# |     1 | Clinton Mitchell    | 10.11.1988 |
fighter = 'Mike Tyson'     # |     1 | Hector Mercedes     | 03.06.1985 |
fighter = 'Evander Holyfield'#|    1 |                     | 11.15.1984 |
fighter = 'Pernell Whitaker'#|     1 | Farrain Comeaux     | 11.15.1984 |
         # Elite, defensive talent
fighter = 'Julio César Chávez'#|  33 | Jerry Lewis         | 10.23.1982 |
fighter = 'Larry Holmes'   # |    28 | Ken Nortan          | 06.11.1982 |
fighter = 'Thomas Hearns'  # |     1 | Jerome Hill         | 11.25.1977 |
fighter = 'Sugar Ray Leonard'#|    1 | Luis Vega           | 02.05.1977 |
fighter = 'Aaron Pryor'    # |     1 | Larry Smith         | 11.12.1976 |
# two battles with Alexis Arguello
fighter = 'Marvin Hagler'  # |     1 | Terry Ryan          | 05.18.1973 |
fighter = 'Roberto Durán'  # |    29 | Ken Buchanan        | 06.26.1972 |
fighter = 'George Foreman' # |     1 | Donald Walheim      | 06.23.1969 |
fighter = 'Joe Frazier'    # |     1 | Woody Goss          | 08.16.1965 |
fighter = 'Muhammad Ali'   # |     1 | Tunney Hunsaker     | 10.29.1960 |
#------------------------------------------------------------------------

# add these Female Boxers
fighter = 'Claressa Shields'
fighter = 'Alycia Baumgardner' # Maricela Cornejo      | 06.03.2023 |
fighter = 'Katie Taylor'
# fighter = 'Caroline Dubois (boxer)'
# | Caroline Dubois (boxer) vs. Magali Rodriguez           | 09.30.2023 |
# | Caroline Dubois (boxer) vs. Yanina del Carmen  Lescano | 06.16.2023 |
#                                     FIX THIS WIKI??
# | Caroline Dubois (boxer) vs. Feriche Mashaury           | 02.11.2023 |
# | Caroline Dubois (boxer) vs. Sofia Rodriguez            | 12.17.2022 |
# | Caroline Dubois (boxer) vs. Milena Koleva              | 10.15.2022 |
# | Caroline Dubois (boxer) vs. Happy Daudi                | 07.30.2022 |
# | Caroline Dubois (boxer) vs. Martina Horgasz            | 03.26.2022 |


# add these Mexican Boxers
fighter = 'Salvador Sánchez'
# Alexis Arguello
# Roberto Duran
# Ricardo Lopez
# Julio Cesar Chavez
# Ruben Oliveira

# add these great boxers
# Emile Griffith
#
# Misc Boxers
# Michael Bentt
# man who would punch behind-the-back
#
# The Sweet Science: A.J. Liebling
# Archie Moore vs Johnson

#-----------------------------
#----- Full Career Watch -----
#------------------------------
# 'Floyd Mayweather Jr.' | 50 |
#------------------------------


# ------------------------------ CLASSIC -------------------------------
fighter = 'Archie Moore'   # The (Old) Mongoose, Jack Slack likes
fighter = 'Buster Douglas'
fighter = 'Charley Burley'
fighter = 'Gene Fullmer'
fighter = 'Jess Willard'
fighter = 'Jack Johnson'

# -- Classic Bouts --
# Andre Berto vs. Victor Ortiz
# GGG vs. Daniel Jacobs 3.18.2017
# Errol Spence Jr. vs Kell Brook 05.27.2017
# Marvin Johnson vs Mathew Said Mohammad :: great classic fight
# Archie Moore vs Evon Durell            :: top ten list of fights

# classic?
# forrest vs mayorga
# Gary Russell Jr. vs. Escandon 2017, vs. Hyland 2016, on Youtube Playlist
#                  vs. Lomachenko
# Big Steal: Viktor Postol vs. Jamshidbek Najmiddinov
# one of the worst hbo fights   vs. Selçuk Aydın?

# ---
show = 'The Boxing Beat: ESPN'
# https://www.theguardian.com/sport/2021/may/27/\
# time-to-find-out-who-cares-boxing-brain-damage-tris-dixon

# -- notes added 2024
# FINISH WATCHING When We Were Kings
# WEC 47: Bowles vs. Cruz
# Ken Norton: great heavy weight boxer in 70s
# mma fighter: Beneil Dariush
# Pereira as kickboxer

# -- from 2021
# Watch Vasiliy Lomachenko vs. Teofima Lopez again
# June 26th Show: PPV soooo....
# June 26th ESPN: Vasiliy Lomachenko vs Masayoshi Nakatani
# June 25th ESPN: Rob Brant vs Janibek Alimkhanuly
# June 19th DAZN: Bektemir Melikuziev vs Gabriel Rosado
# June 19th DAZN: Jaime Munguia vs Maciej Sulecki
# June 19th ESPN: *Naoya Inoue* vs Michael Dasmarinas
# June 12th ESPN: Shakur Stevenson vs Jeremiah Nakathila
#                 Jose Pedraza vs Julian Rodriguez

# Michael Hunter: Heavyweight American
# Nonito Donaire vs. Nordine Oubaali
#
# ------------------
# --- Up-to-date ---
# ------------------
fighter = 'Tony Yoka'
# 'Moses Itauma' #
# 'Andrew Cain'
fighter = 'Leigh Wood (boxer)' # 10.07.2023 Josh Warrington
# ------------
# --- Past ---
# ------------
fighter = 'Teófimo López'                    #  11.27.2021 George Kambosos Jr.
fighter = 'Michael Conlan (boxer)'           #
fighter = 'Daniyar Yeleussinov'              #  09.13.2019 on DAZN vs Hicks
fighter = 'Richard Riakporhe'                #  07.20.2019 Billam-Smith
fighter = 'Demetrius Andrade'                #  06.29.2019 Maciej Sulecki
# Joshua vs Ruiz Jr.                         #  06.01.2019 DAZN, SFL
fighter = 'Austin Trout'                     #  05.25.2019
fighter = 'Gary Russell Jr.'                 #  05.18.2019
# Ortiz Jr. vs Herrera                       #  05.04.2019 DAZN, SFL
fighter = 'Amir Khan (boxer)'                #  04.20.2019 vs Crawford, EPSN
fighter = 'Errol Spence Jr.'                 #  03.16.2019
fighter = 'David Benavidez'                  #  03.16.2019 J'Leon Love
fighter = 'Leo Santa Cruz'                   #  02.16.2019
fighter = 'Gervonta Davis'                   #  02.09.2019 # fun, powerful
fighter = 'Adrian Broner'                    #  01.19.2019
fighter = 'Badou Jack'                       #  01.19.2019
# - [ ] Josh Warrington vs Carl Frampton     #  12.22.2018
fighter = 'Jermall Charlo'                   #  12.22.2018
fighter = 'Jermell Charlo'                   #  12.22.2018
fighter = 'Josh Warrington'                  #  12.22.2018 Carl Frampton
# vs. Lee Selby | 05.19.2018
fighter = 'Billy Joe Saunders'               #  12.22.2018
# vs. Chris Eubank Jr. | 11.29.2014
fighter = 'Diego Pacheco (boxer)'            #  12.22.2018 Luis Gonzalez
# Exciting tall fighter, learn his style!
fighter = 'Sadam Ali'                        #  12.15.2018 beat by Munguia
fighter = 'Canelo Álvarez'                   #  12.15.2018 Rocky Fielding
fighter = 'Vasyl Lomachenko'                 #  12.08.2018 ESPN, Crolla Youtube


# - [ ] December 1 – Deontay Wilder vs Tyson Fury [Showtime]
fighter = 'Jarrett Hurd'                     #  12.01.2018 PBC
fighter = 'Oleksandr Usyk'                   #  11.10.2018 Bellew, DAZN Youtube
fighter = 'Maciej Sulecki'                   #  11.10.2018
fighter = 'Josh Kelly (boxer)'               #  11.10.2018 Walter Castillo
fighter = 'Sullivan Barrera'                 #  11.03.2018
fighter = 'Josh Taylor (boxer)'              #  11.03.2018 Ryan Martin
# vs. Viktor Postol | 06.23.2018 |
fighter = 'Daniel Jacobs (boxer)'            #  10.27.2018 Survived cancer
                                             #           ; Chavez Jr. on SFL
fighter = 'Terence Crawford'                 #  10.13.2018 ESPN
fighter = 'Naoya Inoue'                      #  10.07.2018 DAZN
fighter = 'Daniel Dubois (boxer)'            #  10.06.2018
fighter = 'Artur Beterbiev'                  #  10.06.2018, start 06.08.2013

fighter = 'Jorge Linares'                    #  09.29.2018
fighter = 'Jerwin Ancajas'                   #  09.29.2018
fighter = 'Devin Haney'                      #  09.28.2018 2019 on DAZN, YT
                                             #           ; Haney on SFL
# - [ ] September 24 – Sho Kimura vs Kosei Tanaka
fighter = 'Alexander Povetkin'               #  09.22.2018 Anthony Joshua
# vs. Wladimir Klitschko  | 10.05.2013
# Gennady Golovkin                           #  09.15.2018 DAZN  # 2006 start
fighter = 'Canelo Álvarez'                   #  09.15.2018 DAZN
fighter = 'Rom%C3%A1n_Gonz%C3%A1lez_(boxer)' #  09.15.2018  # chocolatito
fighter = 'Vergil Ortiz Jr.'                 #  09.15.2018 YT no DAZN til 2019
fighter = 'Jaime Munguía'                    #  09.15.2018 Brandon Cook
fighter = 'José Ramírez (boxer)'             #  09.14.2018 Antonio Orozco
fighter = 'Amir Khan (boxer)'                #  09.08.2018 Samual Vargas
fighter = 'Juan Francisco Estrada'           #  09.08.2018 Felipe Orucuta
# 06.24.2016 Shawn Porter                    #  03.04.2017 Danny Garcia
fighter = 'Shawn Porter'                     #  09.08.2018
fighter = 'Lewis Ritson'                     #  09.08.2018
fighter = 'Ryan Garcia'                      #  09.01.2018 YT Carlos Morales
fighter = 'Carl Frampton'                    #  08.18.2018 Jackson
fighter = 'Shakur Stevenson'                 #  08.18.2018 YT post 7.2019 ESPN
fighter = 'Joseph Diaz'                      #  08.11.2018 Jesús Rojas
fighter = 'Sergey Kovalev'                   #  08.05.2018
# devin alexander vs. aundr bird spence      #  08.05.2018
fighter = 'Dmitry Bivol'                     #  08.04.2018, start 11.28.2014
# Kovalev vs. Eleidar Alvarez
# April-June 2018 on DAZN:
#   Buatsi vs. Cuevas, Munguia vs. Ali, Okolie vs. Watkins
#   Vergil Ortiz Jr. vs. Juan Carlos Salgado
fighter = 'Sebastian Fundora'                #  08.24.2018 Antonio Urista
fighter = 'Mikey Garcia'                     #  07.28.2018 Robert Easter Jr.



fighter = 'Dereck Chisora'                   #  07.28.2018 Carlos Takam [DAZN]
# - [ ] Dillian Whyte vs Dereck Chisora II   #  07.28.2018
# vs. Dillian Whyte     | 12.10.2016
# vs. Tyson Fury        | 11.29.2014
# vs. Vitali Klitschko  | 02.18.2012
# vs. Tyson Fury        | 07.23.2011
fighter = 'Dillian Whyte'                    #  07.28.2018 Parker
# vs. Anthony Joshua    | 12.12.2015
fighter = 'Liam Smith (boxer)'               #  07.21.2018 Jaime Munguia
# Liam Williams         | 11.11.2017 |
# Liam Williams         | 04.08.2017 |
# Marian Cazacu         | 03.18.2017 |
# Canelo Álvarez        | 09.17.2016 |
# Predrag Radošević     | 06.04.2016 |
# Jimmy Kelly           | 12.19.2015 |
fighter = 'Kell Brook'                       #  12.08.2018
                                             #  05.27.2017  Spence Jr.
                                             #  09.10.2016 Golovkin
fighter = 'Carlos Balderas'                  #  07.28.2018 YT Caro
fighter = 'Jaime Munguía'                    #  07.21.2018 YT Smith
fighter = 'Boxing career of Manny Pacquiao'  #  07.15.2018 Matthysse, ESPN
# Undercard: Moruti Mthalane vs Muhammad Waseem for the IBF flyweight world
#  title; Carlos Canizares vs Bin Lu for the WBA super-straweight world title
fighter = 'Regis Prograis'                   #  07.14.2018 DAZN in future?
fighter = 'Daniel Roman (boxer)'             #  06.16.2018 Moises Flores
fighter = 'Chris Eubank Jr' # vs Groves      #  02.17.2018   # 09.28.2018
fighter = 'Joe Joyce (boxer)'                #  10.20.2017 Ian Lewison
# Gervonta Davis vs Francisco Fonseca         | 08.26.2017
fighter = 'Savannah Marshall'                #  08.26.2017 Sydney LeBlanc
fighter = 'Franchón Crews-Dezurn'
# Mikey Garcia vs. Adrien Broner              | 07.29.2017
fighter = 'Lawrence Okolie'                  #  03.25.2017 | Geoffrey Cave
   # was 20 before watching the Olympics and deciding he wanted to do that
fighter = 'Keith Thurman'                    #  03.04.2017 # Danny Garcia
# Artur Beterbiev vs. Isidro Ranoni Prieto    | 12.23.2016
fighter = 'Joseph Parker'                    #  12.10.2016 Ruiz Jr.
fighter ='Andy Ruiz Jr.'                     #  12.10.2016 Joseph Parker
# vs. Ortiz 09.04.2022
fighter = 'Brandon Figueroa'                 #  10.08.2016 Raymond Chacon
# vs. Fulton 2021, Castro 2022 to catchup
fighter = 'Yordenis Ugás'                    #  09.27.2016 Bryant Perrella
fighter = 'Sunny Edwards'                    #  09.24.2016 Tasimov
fighter = 'Viktor Postol'                    #  07.23.2016 Terence Crawford
fighter = 'Carlos Takam'                     #  05.21.2016 Joseph Parker
# vs. Povetkin 10.24.2014
fighter = 'Murat Gassiev'                    #  09.21.2011 Roman Mirzoev

# ----------------------------------
# ------- 07.14.2018 current -------
# ----------------------------------



# --------------------------------------------------------------
#  INDEX
# --------------------------------------------------------------
# YT  = Young Talent
# SFL = Saturday Fight Live on DAZN

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

# event = "https://www.tapology.com/fightcenter/events/6919-k-1-legend-94"

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


print('Fin')
