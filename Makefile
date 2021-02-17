lc=python3
file=spoiler_free.py

all: event

f: fighter
fighter:
	$(lc) $(file)

e: card
event: card
card:
	$(lc) spoiler_free.py event

m: floyd
floyd:
	$(lc) floyd_fights.py
