import random
seznam = [1,2,3,4,5,6,7,8,9]

for i in range(len(seznam)):
    index = random.randrange(0,len(seznam))
    print(seznam[index])
    seznam.remove(seznam[index])