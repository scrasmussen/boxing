from bs4 import BeautifulSoup
current_fight = 38

soup = BeautifulSoup(open("floyd_wiki.html"), 'lxml')
for fight, row in enumerate(soup.find_all('tr')):
    fight = 51-fight
    add_space = 0

    columns = row.find_all('td')
    for i, column in enumerate(columns):
        if (i == 3):
            fight_str = str(fight)+" :: "+column.get_text()[:-1]
            if len(fight_str) < 36:
                add_space = 36 - len(fight_str)
            print(fight_str, end='')


    if fight >= 38 and fight <= 47:
        dazn = ' - on DAZN'
        dazn = dazn.rjust(add_space)
        print(dazn, end='')
        if fight == 39:
              print(', Saturday Fight Live', end='')

    if (fight == current_fight):
        current = '==CURRENT=='
        current = current.rjust(add_space+2)
        print(current, end='')

    print('')
