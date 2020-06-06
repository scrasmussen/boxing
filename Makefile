lc=python3
file=spoiler_free.py

all: build

build:
	$(lc) $(file)

e: card
event: card
card:
	$(lc) spoiler_free.py event

f: floyd
floyd:
	$(lc) floyd_fights.py
