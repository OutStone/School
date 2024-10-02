# testovaci uoha c.2:
#   vypocti obsah a obvod trojuhelniku z jeho prepony a jedne odvesny
#
# copyright: David Lausman student na g. Opatov

import math

# input udaju
Delka_Prepony = int(input("kolik meri prepona vaseho vysneneho pravouhleho trojuhelniku? "))
Delka_Odvesny = int(input("kolik meri jedna z odvesen vaseho vysneneho pravouhleho trojuhelniku? "))

if Delka_Odvesny >= Delka_Prepony: # kontrola spravnosti udaju
    raise Exception('Tvoje odvesna je moc dlouha')

# funkce na pocitani hodnot
def third_side(a,c):
    b = math.sqrt(c**2 - a**2)
    return b

def area(a,b):
    return (a * b) / 2

def lineLen(a,b,c):
    return a + b + c


# ukladani hodnot z funkci
b = third_side(Delka_Odvesny,Delka_Prepony)

plocha = area(Delka_Odvesny,b)
cara = lineLen(Delka_Odvesny,b,Delka_Prepony)

# vypsani vysledku
print("Obsah pravoúhlého trojúhelníku je: " + str(plocha))
print("Obvod pravoúhlého trojúhelníku je:e " + str(cara))