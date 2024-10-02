# testovaci uoha c.1:
#   vypocti mnozstvi kc po prevodu z eura pri zadanem kurzu prevodu
#
# copyright: David Lausman student na g. Opatov

# input
Kurz_Euro = int(input("jaky je dnes pole google kurz eura? "))
Pocet_Euro = int(input('a kolik eur vlastne mate? '))

# funkce na spocitani pervodu
def calc(eu):
    return eu * Kurz_Euro

# vypis vysledku
kc = calc(Pocet_Euro)
print(kc)