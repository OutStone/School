from texts import storyObj


alphabeth = 'abcdefghijklmnopqrstuvwxyz'
health = 10
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

    a = "A - " + story['options']['a']
    Options.append(a)
    b = "B - " + story['options']['b']
    Options.append(b)
    c = "C - " + story['options']['c']
    Options.append(c)

    if len(story['conditionalOpt']) > 0:
        for item in story['conditionalOpt']:
            if condition(item['condition']):

                letter = alphabeth[len(Options)]
                text = letter.upper() + ' - ' + item['text']

                Options.append(text)
                story['links'][letter] = item['link']
                

    for option in Options:
        print(option)

    res = input("Volim: ")
    return res


def basicInfo():
    print('Mas ' + str(health) + ' zivotu')
    # print('Je ' + str(time) + ' hodin')

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
            case 'Add-item':
                inventory.append(param)
            case 'Delete-item':
                inventory.remove(param)
            # text in game variables
            case 'Create-var' | 'Change-var':
                pos = param.find(';') # variable and its value are separated by ';'

                varName = param[:pos]
                value = param[pos + 1:]

                inGameVars[varName] = value

            case 'Delete-var':
                del inGameVars[param]
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
    storyNow = storyObj[PosInGame]
    res = choice( storyNow )
    PosInGame = storyNow['links'][res]