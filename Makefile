lc=python3
file=spoiler_free.py

all: build

build:
	$(lc) $(file)

card:
	$(lc) fight_card.py

floyd:
	$(lc) floyd_fights.py

when:
	@echo "beyond 17th of March, 2018"

where: when
