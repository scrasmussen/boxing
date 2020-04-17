from bs4 import BeautifulSoup
import requests

print("start")

def check_columns(rows):
    total = 0
    for row in rows:
        switch =  {
            'Result': True,
            'Res.':    True,
            'Record': True,
            'Opponent': True,
            'Type': True,
            'Method': True,
            'Date': True,
            'Location': True
        }
        if (switch.get(row,False)):
            total += 1
    if (total > 5):
        return True
    return False


url = 'https://en.wikipedia.org/wiki/'
fighter = 'Floyd_Mayweather_Jr.'
# fighter = 'Lawrence_Okolie'
# fighter = 'Murat_Gassiev'
# fighter = 'Alexander_Gustafsson'


url += fighter


# # REMOVE
# req = open("floyd_wiki.html").text
req = requests.get(url).text
soup = BeautifulSoup(req, 'lxml')

result = soup.find_all('table', {'class': 'wikitable'})

for res in result:
    # print(res)
    tr = res.find('tr')
    td = tr.find_all('th')
    rows = [i.text.rstrip() for i in td]
    if (check_columns(rows)):
        print(tr)


print("Fin")

# for fight, row in enumerate(soup.find_all('tr')):
#     fight = 51-fight

#     columns = row.find_all('td')
#     for i, column in enumerate(columns):
#         if (fight == current_fight):
#             current = "           ------- CURRENT"
#         else:
#             current = ""
#         if (i == 3):
#             print(str(fight)+" :: "+column.get_text()[:-1]+current)
