c = [1,2,5,10,20,50]
E = [1,2,5,10,20,50,100,200,500,1000,2000]

while True:
    produkt = input("Vyber si produkt z moznosti: 'trancetto za 75c, grissini za 75c, prosciutto za 3E, colu za 1E a cappy za 1E': ")
    match produkt:
        case "cola":
            To_Pay = 1
        case "trancetto":
            To_Pay = 0.75
        case "grissini":
            To_Pay = 0.75
        case "prosciutto":
            To_Pay = 3
        case "cappy":
            To_Pay = 1
        case _:
            print('spatny produkt vyber si znova')
            continue

    produkt_price = To_Pay
    
    while To_Pay > 0:
        coin = input('vloz penize, jste potreba '+  str(To_Pay) + 'E. : ')

        if coin[-1] == 'c':
            if int(coin[0:-1]) in c:
                To_Pay -= int(coin[0:-1]) / 100
            else:
                print('chyba ve cisle ', print(coin[0:-1]))
                continue
            
        elif coin[-1] == 'E':
            if int(coin[0:-1]) in E:
                To_Pay -= int(coin[0:-1])
            else:
                print('chyba ve cisle')
                continue
        else:
            print('chyba ve mene')
            continue
    
    print('uspesne jsis zakoupil ',produkt, ' vracim ',-1*To_Pay,'E') 