lc=python3
file=spoiler_free.py

all: build

build:
	$(lc) $(file)

e: card
event: card
card:
	$(lc) spoiler_free.py event

floyd:
	$(lc) floyd_fights.py

when:
	@echo "beyond 17th of March, 2018"

where: when
