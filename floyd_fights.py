from bs4 import BeautifulSoup
current_fight = 33

soup = BeautifulSoup(open("floyd_wiki.html"), 'lxml')
for fight, row in enumerate(soup.find_all('tr')):
    fight = 51-fight
    print("On Youtube https://youtu.be/o_PLFpTmIYw") if fight == 43 else False
    print("On DAZN, Saturday Fight Live")            if fight == 39 else False

    columns = row.find_all('td')
    for i, column in enumerate(columns):
        if (fight == current_fight):
            current = "           ------- CURRENT"
        else:
            current = ""
        if (i == 3):
            print(str(fight)+" :: "+column.get_text()[:-1]+current)

# fight 26: Carlos Herandez, end of round 6, only knockdown of Mayweathers
#           careeer. From punching too hard
