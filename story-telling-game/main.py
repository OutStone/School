from texts import storyObj
import os


alphabeth = 'abcdefghijklmnopqrstuvwxyz'
health = 10
money = {
    'měďáky' : 0,
    'zlaťáky' : 0,
}
# time = 10
#hunger = 0
inGameVars = {}
inventory = []
gameRunning = True
PosInGame = 0

def choice(story):
    if len(story['action']) > 0:
        actionParser(story['action'])

    Options = []

    print(story['text'] + '\n')

    basicInfo()

    # zpracovani moznosti bez podminek
    mainOpt = list(story['options'].keys())
    for key in mainOpt:
        text = story['options'][key]

        letter = alphabeth[len(Options)]
        text = letter.upper() + ' - ' + text

        Options.append(text)

    # zpracovani moznosti s podminky
    if len(story['conditionalOpt']) > 0:
        for item in story['conditionalOpt']:
            if condition(item['condition']):

                letter = alphabeth[len(Options)]
                text = letter.upper() + ' - ' + item['text']

                Options.append(text)
                story['links'][letter] = item['link']
                

    
    # vytiskne vsechny moznosti, ze kterych je na vyber
    for option in Options:
        print(option)

    res = input("Volim: ")
    return res


def basicInfo():

    print('Mas ' + str(health) + ' zivotu')
    # print('Je ' + str(time) + ' hodin')

    if money['měďáky'] > 0 and money['zlaťáky'] > 0:
        print('Mas ' + str(money['měďáky']) + ' měďáků a '  + str(money['zlaťáky']) + 'zlaťáků')
    elif money['měďáky'] > 0:
        print('Mas ' + str(money['měďáky']) + ' měďáků')
    elif money['zlaťáky'] > 0:
        print('Mas '  + str(money['zlaťáky']) + ' zlaťáků')
    else:
        print("Jsi bez peněz")

    if len(inventory) > 0:
        items = ''
        for itm in inventory:
            items += itm + ', '
        items = items[:-2] # deletes last comma and white space

        # pos = items.rfind(',')

        # if pos != -1:


        print('V inventari mas ' + items  + '\n')
    else:
        print('Mas prazdny inventar'  + '\n')
    


def actionParser(action):
    run = True
    while run:
        pos = action.index(':')
        command = action[:pos]
        command = removeSpace(command)


        dividerPos = action.find('&&')

        if dividerPos != -1:
            param = action[pos + 1: dividerPos]

            action = action[dividerPos + 2:] # smaze prave se zpracovavajici prikaz
        else:
            run = False
            param = action[pos+1:]

        param = removeSpace(param)
        
        match command:
            # inventory management
            case 'money-bronz':
                sign = param[0]
                value = removeSpace(param[1:])
                value = int(value)

                match sign:
                    case '+':
                        money['měďáky'] += value
                    case '-':
                        money['měďáky'] -= value
                        if money['měďáky']<0:
                            print('money error, you have a deficit')

                while money['měďáky']>24:
                        money['zlaťáky'] += 1
                        money['měďáky'] -= 24

            case 'money-gold':
                sign = param[0]
                value = removeSpace(param[1:])
                value = int(value)

                match sign:
                    case '+':
                        money['zlaťáky'] += value
                    case '-':
                        money['zlaťáky'] -= value
                        if money['zlaťáky']<0:
                            print('money error, you have a deficit')
                            
            case 'Add-item':
                inventory.append(param)
            case 'Delete-item':
                inventory.remove(param)
            # text in game variables
            case 'Create-var' | 'Change-var':
                pos = param.find(';') # variable and its value are separated by ';'

                varName = removeSpace(param[:pos])
                value = removeSpace(param[pos + 1:])

                inGameVars[varName] = value

            case 'Delete-var':
                del inGameVars[removeSpace(param)]
            # math in game variables
            case 'Create-math-var':
                pos = param.find(';') # variable and its value are separated by ;

                varName = removeSpace(param[:pos])
                value = removeSpace(param[pos + 1:])
                value = int(value)

                inGameVars[varName] = value
            case 'Change-math-var':
                pos = param.find(';') # variable and its value are separated by ;

                varName = removeSpace(param[:pos])
                value = removeSpace(param[pos + 1:])

                sign = value[0]
                value = int(value[1:])

                match sign:
                    case '+':
                        inGameVars[varName] += value
                    case '-':
                        inGameVars[varName] -= value
                    case '*':
                        inGameVars[varName] *= value
                    case '/':
                        inGameVars[varName] /= value
                    case '**':
                        inGameVars[varName] **= value
                    case '%':
                        inGameVars[varName] %= value
                    case '//':
                        inGameVars[varName] //= value
            case 'Delete-math-var':
                del inGameVars[param]

def condition(condition):
    pos = condition.index(':')
    command = condition[:pos]
    command = removeSpace(command)
    
    param = condition[pos+1:]
    param = removeSpace(param)

    match command:
        case 'money-gold':
            sign = param[0]
            param = param[1:] # zbavi se znaminka ktere ulozil do sign

            if param[0] == '=':
                sign += param[0]
                param = param[1:] # opet zbavi se znaminka ktere ulozil do sign
            
            match sign:
                case '<':
                    res = money['zlaťáky'] < int(param)
                case '<=':
                    res = money['zlaťáky'] <= int(param)
                case '>':
                    res = money['zlaťáky'] > int(param)
                case '>=':
                    res = money['zlaťáky'] >= int(param)
                case '==':
                    res = money['zlaťáky'] == int(param)
                case '!=':
                    res = money['zlaťáky'] != int(param)
                case _: # probehne pokud nenajde spravnou podminku
                    print('chyba - hodnota sign neni z pozadovanych limitu. sign = ',sign)
        case 'money-bronz':
            sign = param[0]
            param = param[1:] # zbavi se znaminka ktere ulozil do sign

            if param[0] == '=':
                sign += param[0]
                param = param[1:] # opet zbavi se znaminka ktere ulozil do sign
            
            match sign:
                case '<':
                    res = money['měďáky'] < int(param)
                case '<=':
                    res = money['měďáky'] <= int(param)
                case '>':
                    res = money['měďáky'] > int(param)
                case '>=':
                    res = money['měďáky'] >= int(param)
                case '==':
                    res = money['měďáky'] == int(param)
                case '!=':
                    res = money['měďáky'] != int(param)
                case _: # probehne pokud nenajde spravnou podminku
                    print('chyba - hodnota sign neni z pozadovanych limitu. sign = ',sign)

        case 'health':
            sign = param[0]
            param = param[1:] # zbavi se znaminka ktere ulozil do sign

            if param[0] == '=':
                sign += param[0]
                param = param[1:] # opet zbavi se znaminka ktere ulozil do sign
            
            match sign:
                case '<':
                    res = health < int(param)
                case '<=':
                    res = health <= int(param)
                case '>':
                    res = health > int(param)
                case '>=':
                    res = health >= int(param)
                case '==':
                    res = health == int(param)
                case '!=':
                    res = health != int(param)
                case _: # probehne pokud nenajde spravnou podminku
                    print('chyba - hodnota sign neni z pozadovanych limitu. sign = ',sign)
        case 'have-itm':
            res = param in inventory
        case 'game-var':
            pos = param.find(';') # variable and its value are separated by ;

            varName = removeSpace(param[:pos])
            value = removeSpace(param[pos + 1:])
            
            keys = inGameVars.keys()
            if varName in keys:
                if inGameVars[varName] == value:
                    res = True
                else:
                    res = False
            else:
                print('ERROR - Game variable ' + varName + ' does NOT EXIST')
        case 'game-math-var':
            pos = param.find(';') # variable and its value are separated by ;

            varName = removeSpace(param[:pos])
            value = removeSpace(param[pos + 1:])
            
            keys = inGameVars.keys()
            
            sign = value[0]
            value = value[1:] # zbavi se znaminka ktere ulozil do sign

            if value[0] == '=':
                sign += value[0]
                value = value[1:] # opet zbavi se znaminka ktere ulozil do sign
            
            match sign:
                case '<':
                    res = money['zlaťáky'] < int(value)
                case '<=':
                    res = money['zlaťáky'] <= int(value)
                case '>':
                    res = money['zlaťáky'] > int(value)
                case '>=':
                    res = money['zlaťáky'] >= int(value)
                case '==':
                    res = money['zlaťáky'] == int(value)
                case '!=':
                    res = money['zlaťáky'] != int(value)
                case _: # probehne pokud nenajde spravnou podminku
                    print('chyba - hodnota sign neni z pozadovanych limitu. sign = ',sign)



            if varName in keys:
                if inGameVars[varName] == value:
                    res = True
                else:
                    res = False
            else:
                print('ERROR - Game variable ' + varName + ' does NOT EXIST')
        case _:
            print('chyba - podminka nebyla nalezena')

    return res

def removeSpace(str):
    while True:
        if str[0] == ' ':
            str = str[1:]
        else:
            break
    
    while True:
        if str[-1] == ' ':
            str = str[:-1]
        else:
            break
    return str


while gameRunning:
    os.system('cls')
    storyNow = storyObj[PosInGame]
    res = choice( storyNow )
    PosInGame = storyNow['links'][res]