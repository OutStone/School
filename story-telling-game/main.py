from texts import storyObj

print(storyObj)

lives = 10
time = 10
#hunger = 0
inventory = []
gameRunning = True
index = 0

def choice(story,a,b,c):
    a = "A - "
    b = "B - "
    c = "C - "
    basicInfo()
    res = input(story + "\n \n " + a + "\n" + b + "\n" + c + "\n Volim: ")
    return res


def basicInfo():
    print('Mas ' + str(lives) + ' zivotu')
    print('Je ' + str(time) + ' hodin')

    if len(inventory) > 0:
        print('a v inventari mas ', inventory)
    else:
        print('Mas prazdny inventar')
    print('\n')


while gameRunning:
    storyNow = storyObj[index]
    res = choice(storyNow.text , storyNow.a , storyNow.b , storyNow.c )
    index = storyNow.links[res]