from bs4 import BeautifulSoup

# fight 26: Carlos Herandez, end of round 6, only knockdown of Mayweathers
#           careeer. From punching too hard




current_fight = 27

soup = BeautifulSoup(open("floyd_wiki.html"), 'lxml')
for fight, row in enumerate(soup.find_all('tr')):
    fight = 51-fight

    columns = row.find_all('td')
    for i, column in enumerate(columns):
        if (fight == current_fight):
            current = "           ------- CURRENT"
        else:
            current = ""
        if (i == 3):
            print(str(fight)+" :: "+column.get_text()[:-1]+current)
