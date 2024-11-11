Vklad=0
Spravna_volba=1
Volba = input("Vyber produkt (K, D, L, V):")
if Volba == "K":
    Cena = 200
elif Volba == "D":
    Cena = 150
elif Volba == "L":
    Cena = 100
elif Volba == "V":
    Cena = 90
else:
    print("Tento produkt není v nabídce. Prosím začněte znovu.")
    Spravna_volba = 0

if Spravna_volba == 1:
    print("Cena je", Cena, "Kč")
    while(Vklad < Cena):
        print("Je vloženo", Vklad, "Kč. Je potřeba vložit", Cena-Vklad, "Kč.")
        Mince = int(input("Vlož minci "))
        if Mince == 10 or Mince == 20 or Mince == 50 or Mince == 100 or Mince == 200:
            Vklad = Vklad + Mince
            if Vklad > Cena - 1:
                print("Děkuji za nákup, vracím vám", Vklad - Cena, "Kč")
        else:
            print("Špatná mince, zkus to znovu")