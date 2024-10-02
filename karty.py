# testovaci uoha c.2:
#   vypocti obsah a obvod trojuhelniku z jeho prepony a jedne odvesny
#
# copyright: David Lausman student na g. Opatov

import random
cards = ["Eso", "Seven", "Joker", "Queen", "King", "Nine"]

# funkce na vybrani z listu
def pick(list):
    picked = random.choice(list)
    list.remove(picked)
    return {
        "karty": list,
        "picked" : picked
        }

# cyklus pro vybrai daneho poctu karet
i = int(input('kolik karet ma byt vybrano? '))
if i >= len(cards):
    raise Exception('pocet vybranych kafret je vetsi nezli pocet karet v ruce')

for i in range(i):
    res = pick(cards)
    cards = res['karty']
    print(res['picked'])

print("zbyvajici karty:",cards)