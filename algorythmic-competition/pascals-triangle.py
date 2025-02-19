while True:
    vstup = input('pozice: ') # format (n+1,k+1)

    vstup = vstup[1:-1]
    n = int(vstup.split(",")[0]) - 1
    k = int(vstup.split(",")[1]) - 1

    def faktorial(a):
        sum = 1
        for i in range(a):
            sum *= (i+1)
        return sum
    
    # tenhle vzorec popisuje hodnoty kazdeho pole
    value = (faktorial(n))/(faktorial(k)*faktorial(n-k))
    print(value)