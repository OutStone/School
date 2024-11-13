def pyramida(x):
    res = 0
    a = x

    for j in range(a):
        res += x
        x -= 1

    print(res) 

    for j in range(a):
        str = "x" * x
        print(str)
        x +=1

pyramida(5)