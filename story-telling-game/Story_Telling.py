from Story_Texts import storyObj
import os


alphabeth = 'abcdefghijklmnopqrstuvwxyz'
health = 10
money = {
    'měďáky' : 0,
    'zlaťáky' : 0,
}
exchangeCurse = 24
# time = 10
#hunger = 0
inGameVars = {}
inventory = []
gameRunning = True
PosInGame = 0

# hlavni funkce, ktera se zavola pri kazde iteraci herniho cycklu
# zde se zpracovává herní objekt a volají se funkce na vykonaní herních akcí/vyhodnocení podmínek, na než jsou vázány další herní možnosti atd... 
def choice(story):
    if len(story['action']) > 0: # pokud má tenhle herní objekt nejakou svojí akci, tak je předána funkci na její provedení
        actionParser(story['action'])

    Options = [] # zde budou uloženy zprávy s možnostmi na výběr pro hráče

    # vypíše herní příběh
    print(story['text'] + '\n')

    # zavolá funci na vypsání základních statistik  - inventář, životy, atd... 
    basicInfo()

    # seznam všech písmenek ze kterých dostane hráč na výběr
    usedKeys = []

    # zpracovani moznosti bez podminek
    mainOpt = list(story['options'].keys())
    for key in mainOpt:
        text = story['options'][key]

        text = key.upper() + ' - ' + text

        Options.append(text) # přidá text herní možnosti do seznamu textů, ze kterýchje na výběr
        usedKeys.append(key)

    # zpracovani moznosti s podminky
    if len(story['conditionalOpt']) > 0:
        for item in story['conditionalOpt']:
            if condition(item['condition']): # zkontroluje podmínku pro danou příběhovou možnost

                letter = alphabeth[len(Options)]
                text = letter.upper() + ' - ' + item['text']

                # přidá text herní možnosti do seznamu textů, ze kterýchje na výběr, a přídá link herní možnosti do seznamu všech linků 
                Options.append(text)
                story['links'][letter] = item['link']

                # zařazení akce, která bude provedena pokud hráč vybere danou možnost, do seznamu všech takovýchto akcí
                story['actions'][letter] = item['action']
                usedKeys.append(letter)

    # zkontroluje jestli má každá z použitých možností na výběr pro hráče svojí akci (klidně jen prázdnou, ale musí tam být)
    # a přidá prázdnou akci pokud ji nějaká herní možnost nemá
    missingActions = compareLists(story['actions'].keys(),usedKeys)
    if len(missingActions) > 0:
        for actionKey in missingActions:
            story['actions'][actionKey] = ''
    
    # vytiskne vsechny moznosti, ze kterych je na vyber
    for option in Options:
        print(option)
    if len(Options) > 0:
        res = input("Volim: ")
        return res.lower()
    else: # pokud není na výběr, tak se ukočí hra
        return 'STOP'

# funkce vypisující herní info - inventář a podobné
def basicInfo():

    print('Mas ' + str(health) + ' zivotu') # zdraví hráče
    # TODO: print('Je ' + str(time) + ' hodin')

    # peníze
    if money['měďáky'] > 0 and money['zlaťáky'] > 0:
        print('Mas ' + str(money['měďáky']) + ' měďáků a '  + str(money['zlaťáky']) + ' zlaťáků')
    elif money['měďáky'] > 0:
        print('Mas ' + str(money['měďáky']) + ' měďáků')
    elif money['zlaťáky'] > 0:
        print('Mas '  + str(money['zlaťáky']) + ' zlaťáků')
    else:
        print("Jsi bez peněz")


    # inventář
    if len(inventory) > 0:
        items = ''
        for itm in inventory:
            items += itm + ', '
        items = items[:-2] # smaže čárku a mezeru za posledním předmětem

        print('V inventari mas ' + items  + '\n')
    else:
        print('Mas prazdny inventar'  + '\n')
    
# funkce, která cyklí skrz seznam akcí, které dostane v podobě dlouhého textového řetězce
def actionParser(action):
    run = True
    while run:

        # Příkaz má dvě části - název a parametry - tyto dvě části jsou oddělěné dvoutečkou.
        # Zde je jedno jesli je v řetezci jeden nebo více příkayů protože funkce .index() najde první výskyt 
        pos = action.index(':')
        command = action[:pos]
        command = removeSpace(command)

        # více příkazů je odděleno dvouznakem &&
        dividerPos = action.find('&&')

        # pokud je rozdělovací dvouznak nalezen, tak je v seznamu jestě aspoň jeden další příkaz
        #  -> program bude dál cyklit, parametr aktualního příkazu se uloží a celý zbytek aktualního příkazu se smaže
        # jinak se cyklení zastaví a aktuální parametr se uloží
        if dividerPos != -1:
            param = action[pos + 1: dividerPos]

            action = action[dividerPos + 2:] # smaze prave se zpracovavajici prikaz
        else:
            run = False
            param = action[pos+1:]

        param = removeSpace(param) # smazání mezer na začátku a konci řetězce

        # hledá požadovaný herní příkaz
        match command:
            # práce s Penězmi
            case 'Money-bronz':
                sign = param[0] # znak označující požadovanou matematickou operaci (+ -)
                value = removeSpace(param[1:])
                value = int(value)

                match sign:
                    case '+': # přičtění peněz
                        money['měďáky'] += value
                    case '-': # odečtení peněz + kontrola jestli nevznikl deficit
                        money['měďáky'] -= value
                        if money['měďáky']<0:
                            if money['zlaťáky'] > 0: # pokud jsou peníze s vyšší hodnotou, tak se jimi možná dá splatit deficit
                                money['měďáky'] += money['zlaťáky']*exchangeCurse

                            if money['měďáky']<0: # pokud převod vyšší měnny nebyl dostačující, tak nastane error
                                print('ERROR - you do not have enought money - currentely ' + money['měďáky'])

                # pokud má hráč více menších peněz, tak jsou vyměněny za peníze s vyšší hodnotou
                while money['měďáky'] > exchangeCurse:
                        money['zlaťáky'] += 1
                        money['měďáky'] -= exchangeCurse

            case 'Money-gold':
                sign = param[0] # znak označující požadovanou matematickou operaci (+ -)
                value = removeSpace(param[1:])
                value = int(value)

                match sign:
                    case '+': # přičtění peněz
                        money['zlaťáky'] += value
                    case '-': # odečtení peněz + kontrola jestli nevznikl deficit
                        money['zlaťáky'] -= value
                        if money['zlaťáky']<0:
                            print('ERROR - you do not have enought money - currentely ' + money['zlaťáky'])

            # práce s inventářem
            case 'Add-item':
                inventory.append(param)
            case 'Delete-item':
                inventory.remove(param)

            # Herní proměnné s textem
            case 'Create-var' | 'Change-var':
                pos = param.find(';') # jmého a hodnota proměnné jsou oddělené znakem ;

                varName = removeSpace(param[:pos])
                value = removeSpace(param[pos + 1:])

                inGameVars[varName] = value # přidání proměnné do seznamu všech proměnných

            case 'Delete-var':
                del inGameVars[removeSpace(param)]

            # Herní proměnné s číslnými hodnotami
            case 'Create-math-var':
                pos = param.find(';') # jmého a hodnota proměnné jsou oddělené znakem ;

                varName = removeSpace(param[:pos])
                value = removeSpace(param[pos + 1:])
                value = int(value)

                inGameVars[varName] = value
            case 'Change-math-var':
                pos = param.find(';') # jmého a hodnota proměnné jsou oddělené znakem ;

                varName = removeSpace(param[:pos])
                value = removeSpace(param[pos + 1:])

                # první jedno nebo dvě místa označují operaci, která má být provedena s danou hodnotou
                sign = value[0]
                value = value[1:]
                if value[0] == '*' or value[0] == '/':
                    sign += value[0]
                    value = value[1:]

                value = int(value)

                # hledáni správné matimatické operace
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

# funkce na vyhodnocení podmínek - výsledek se vrátí ve formě True-False. tato hodnota je ve funkci uložena v proměnné 'res' 
def condition(condition):
    pos = condition.index(':') # název podmínky a parametr proměnné jsou odděleny dvoutečkou
    command = condition[:pos]
    command = removeSpace(command)
    
    param = condition[pos+1:]
    param = removeSpace(param)

    # hledání správné herní podmínky
    match command:
        # peníze
        case 'Money-gold':
            # znamínko operace je uloženo na prvním jednom nebo dvou místech
            sign = param[0]
            param = param[1:]

            if param[0] == '=':
                sign += param[0]
                param = param[1:]
            
            # hledání správného porovnávacího znamínka
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
                case _: # proběhne pokud program nenajde správnou podmínku
                    print('ERROR - comparing condition ' + sign + ' does NOT EXIST')
        case 'Money-bronz':
            # znamínko operace je uloženo na prvním jednom nebo dvou místech
            sign = param[0]
            param = param[1:]

            if param[0] == '=':
                sign += param[0]
                param = param[1:]
            
            # hledání správného porovnávacího znamínka
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
                case _: # proběhne pokud program nenajde správnou podmínku
                    print('ERROR - comparing condition ' + sign + ' does NOT EXIST')
        # zdraví hráče
        case 'Health':
            # znamínko operace je uloženo na prvním jednom nebo dvou místech
            sign = param[0]
            param = param[1:]

            if param[0] == '=':
                sign += param[0]
                param = param[1:]
            
            # hledání správného porovnávacího znamínka
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
                case _: # proběhne pokud program nenajde správnou podmínku
                    print('ERROR - comparing condition ' + sign + ' does NOT EXIST')
        # kontrola jestli má hráč požadovanou věc ve svém inventáři
        case 'Have-item':
            res = param in inventory
        # kontrola hodnoty herní proměnné (textový řetězec)
        case 'Game-var':
            pos = param.find(';') # název proměnné a její požadovaná hodnota jsou odděleny znakem ;

            varName = removeSpace(param[:pos])
            value = removeSpace(param[pos + 1:])
            
            # kontrola jestli daná hodnota existuje, pokud ne tak je program vrátí hodno´tu False, když proměnná existuje, tak program zkontroluje její hodnotu 
            keys = inGameVars.keys()
            if varName in keys:
                res = inGameVars[varName] == value
            else:
                res = False
        # kontrola hodnoty herní proměnné (číslená hodnota)
        case 'Game-math-var':
            pos = param.find(';') # název proměnné a její požadovaná hodnota jsou odděleny znakem ;

            varName = removeSpace(param[:pos])
            value = removeSpace(param[pos + 1:])
            
            keys = inGameVars.keys()
            
            # znamínko logické operace je uloženo na prvním jednom nebo dvou místech v řetězci
            sign = value[0]
            value = value[1:]

            if value[0] == '=':
                sign += value[0]
                value = value[1:]
            
            value = int(value)

            # kontrola jestli kontrolovaná proměnná existuje
            #  NE  -> program vrátí False
            #  ANO -> program zkontroluje hodnotu proměnné
            if varName in keys:

                # hledání správné logické operace
                match sign: # TODO: NOW!
                    case '<':
                        res = inGameVars[varName] < int(value)
                    case '<=':
                        res = inGameVars[varName] <= int(value)
                    case '>':
                        res = inGameVars[varName] > int(value)
                    case '>=':
                        res = inGameVars[varName] >= int(value)
                    case '==':
                        res = inGameVars[varName] == int(value)
                    case '!=':
                        res = money['zlaťáky'] != int(value)
                    case _: # proběhne pokud program nenajde správnou podmínku
                        print('ERROR - comparing condition ' + sign + ' does NOT EXIST')
            else:
                res = False
        # pokud nebyl nalezen správný příkaz, tak se vypíše error
        case _:
            print('ERROR - Game condition ' + command + ' does NOT EXIST')
            res = False

    return res

# funkce na mazání mezer ze začátku a konce daného textového řetězce
def removeSpace(str):
    while True: # mezerz na začátku
        if str[0] == ' ':
            str = str[1:]
        else:
            break
    
    while True: # mezerz na konci
        if str[-1] == ' ':
            str = str[:-1]
        else:
            break
    return str

# funkce, která najde všechny data v listu b, které nejsou obsažené v listu a
def compareLists(a,b):
    a = list(a)
    b = list(b)
    res = []
    for B_item in b:
        if B_item in a:
            a.remove(B_item)
        else:
            res.append(B_item)
    
    return res

# hlavní herní cyklus
while gameRunning:
    os.system('cls') # smaže konzoli
    storyNow = storyObj[PosInGame]
    res = choice( storyNow )

    # pokud nebyla na výběr zádná možnost, tak se hra ukočí - fuknce choice() vrátí automaticky hodnotu STOP+
    if res == 'STOP':
        gameRunning = False
        continue
    
    # jeliže má hráčem vybraná možnost nějakou na sebe se važící akci, tak ji systém vykoná
    if len(storyNow['actions'][res]) > 0: 
        actionParser(storyNow['actions'][res])
    
    PosInGame = storyNow['links'][res]