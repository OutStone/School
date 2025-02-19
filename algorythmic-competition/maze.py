# input
bludiste_1 = [
    [0, 0, 0, 0, 0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 1, 1, 1, 0],
    [1, 1, 0, 1, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 0]
]

vstup = (4, 3)  
vystup = (0, 8)  

# globalni promenne
translate = {
    ( 0, 1) : 'Do Prava',
    ( 0,-1) : 'Do Leva',
    ( 1, 0) : 'Dolu',
    (-1, 0) : 'Nahoru',
}

sirka = len(bludiste_1)
vyska = len(bludiste_1[0])

Poloha = vstup
Rozcesti = []

# cyklus pro hledani
while True:
    Options = []
    # hledani nahoru a dolu (x a y jsou prohozene)
    for x in range(-1,2,2):
        posX = Poloha[0] + x
        if posX >= 0 and posX < sirka:
            if bludiste_1[posX][Poloha[1]] == 0:
                Options.append((posX,Poloha[1]))
    
    # hledani doleva a doprava (x a y jsou prohozene)
    for y in range(-1,2,2):
        posY = Poloha[1] + y
        if posY >= 0 and posY < vyska:
            if bludiste_1[Poloha[0]][posY] == 0:
                Options.append((Poloha[0],posY))
    
    # zamezeni vraceni se zpatky
    bludiste_1[Poloha[0]][Poloha[1]] = 2

    #test pro cil
    if Poloha == vystup:
        break

    # vyber cestu z nalezenych cest
    if len(Options) == 1:
        Poloha = Options[0]

    # nejsou zadne cesty kolem me -> vratim se na posledni krizovatku (pokud neni tak vyskoci error ale na to kaslu)
    elif len(Options) == 0:
        while True:
            # odrizne slepou vetev
            place_to_block = Rozcesti[-1]["options"][0]
            bludiste_1[place_to_block[0]][place_to_block[1]] = 1
            del Rozcesti[-1]["options"][0]

            # zbavi se krizovatky pokud prozkoumal vsechny jejin cesty
            if len(Rozcesti[-1]["options"]) == 0:
                del Rozcesti[-1]
            else:
                break

        Poloha = Rozcesti[-1]["positon"]

    # nasel rozcesti
    else:
        Rozcesti.append({
            "options" : Options,
            "positon" : Poloha
        })
        Poloha = Options[0]

# reset aby to ted prosel tak primo jak to posledne nasel
Poloha = vstup
minPoloha = vstup

while True:
    Options = []
    # hledani nahoru a dolu (x a y jsou prohozene)
    for x in range(-1,2,2):
        posX = Poloha[0] + x
        if posX >= 0 and posX < sirka:
            if bludiste_1[posX][Poloha[1]] == 2:
                Options.append((posX,Poloha[1]))

    # hledani doleva a doprava (x a y jsou prohozene)
    for y in range(-1,2,2):
        posY = Poloha[1] + y
        if posY >= 0 and posY < vyska:
            if bludiste_1[Poloha[0]][posY] == 2:
                Options.append((Poloha[0],posY))
    
    # zamezeni vraceni se zpatky
    bludiste_1[Poloha[0]][Poloha[1]] = 3

    #test pro cil
    if Poloha == vystup:
        break

    # vyber cestuy z nalezenych cest
    if len(Options) == 1:
        minPoloha = Poloha
        Poloha = Options[0]

        vektor = (Poloha[0]-minPoloha[0],Poloha[1]-minPoloha[1])
        print(translate[vektor])

    # chyba - nejak se zasekl nekde i presto ze to predtim prosel uspesne (neni mozne ale stejne; program by jinak cyklil)
    if len(Options) == 0:
        print("chyba")
        for line in bludiste_1:
            print(line)
        break