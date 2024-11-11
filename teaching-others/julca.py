from tkinter import *

root = Tk()
canvas = Canvas(root, width=500, height=500)
canvas.pack()


def Zed (Pocet_Cihel, Barva): # Pocet_Cihel = pocet cihel na jednom radku
    pocet_Radku = 10
    pocet_Dvojradku = int(pocet_Radku/2)

    Sirka_Cihly = 40 # v pixelech na monitoru - hodnota X
    Vyska_Cihly = 20 # v pixelech na monitoru - hodnota Y

    Spara = 3

    for Cislo_Dvojradku in range(pocet_Dvojradku): # resi VYSKU zdi - hodnota Y

        StartY = Cislo_Dvojradku * (Vyska_Cihly + Spara)*2

        for Cislo_Cihly in range(Pocet_Cihel): # Nizsi_radek
             # resi SIRKU kazdeho licheho radku - ten dole z tech dvou - hodnota X
            StartX = Cislo_Cihly * (Sirka_Cihly + Spara)

            canvas.create_rectangle(
                StartX,                 # Souradnice zacatku X
                StartY,                 # Souradnice zacatku Y
                StartX + Sirka_Cihly,   # Souradnice konce X = zacatek chihly + jeji rozmer
                StartY + Vyska_Cihly,   # Souradnice konce Y = zacatek chihly + jeji rozmer
                fill = Barva                   # Nejaka ta barvicka
                )

        StartY += Vyska_Cihly + Spara # posunu zacatek o vysku prvni radku
        for Cislo_Cihly in range(Pocet_Cihel): # Vyssi_radek
             # resi SIRKU kazdeho sudeho radku - ten nahore z tech dvou - hodnota X
            StartX = Cislo_Cihly * (Sirka_Cihly + Spara)

            canvas.create_rectangle(
                StartX,                 # Souradnice zacatku X
                StartY,                 # Souradnice zacatku Y
                StartX + Sirka_Cihly,   # Souradnice konce X = zacatek chihly + jeji rozmer
                StartY + Vyska_Cihly,   # Souradnice konce Y = zacatek chihly + jeji rozmer
                fill = Barva                   # Nejaka ta barvicka
            )
        
Zed(5,'red')
root.mainloop()
##### pocet dvouradku ku poctu redku
# [OO]  [OO]  [OO]  [OO]
#   [OO]  [OO]  [OO]  [OO] 
#                               5
# [OO]  [OO] [OO]  [OO]
#   [OO]  [OO]  [OO]  [OO] 
#                               4
# [OO]  [OO] [OO]  [OO]
#   [OO]  [OO]  [OO]  [OO] 
#                               3
# [OO]  [OO] [OO]  [OO]
#   [OO]  [OO]  [OO]  [OO]
#                               2
# [OO]  [OO] [OO]  [OO]
#   [OO]  [OO]  [OO]  [OO]
#                               1



#canvas.create_rectangle('StartX', 'StartY', 'EndX', 'EndY', fill='red')