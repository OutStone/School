storyObj = {
    0: {
        'action' : '',
        'text' : 
"""Píše se rok 1257 od narození Páně a jen z Boží milosti je z tebe bohabojný prostáček,
pekař ve slavném něměckém městě Hammeln. Jenže toto převeliké město má jeden problém.
A tím je maličký tvoreček, jenž obývá každý temný kout a živí se vším, co se kde válí, klidně i dětmi - KRYSA

Neslavnější konšelé města se po letech dlouhých diskuzí přece jen shodli na řešení tohoto nepříjemného problému -
- pozvali krysaře. Ano, toho nanicovatého hudebníčka, co si píská na píšťalku a krysou za ním jdou v houfu jak za králem.
Aspoň to o něm tvrdívali oni bahotí kupci z předalekých měst, kde jim údajně již pomohl zbavit se záplavy těchto hlodavců.

Jenže tady to bylo jinak.
Krysař přišel, poklonil se pámům konšelům a pak strávil celé odpoledne popíjením v krčmě. Až když už bylo slunko za horami
a na město se snesla tma, tak až tehdy vyšel a začal hrát. Chodil a hrál dlouho do noci a až když půlnoc odbila,
tak s houfem krys za sebou vyšel ze města a odvedl je někam do lesů a jeskyň, co jich kolem jen bylo.

Následující den přišel kolem poledne zpět a vymáhal svoji odměnu za splnění úkolu, jenže nic nedostal. Dlouho předloho
se hadal s konšeli na náměstí před radnicí a padlo přitom nesmírné množsví úražek na cti.

Ješte tentýž včerejší večer vzal znovu píšťalku a opět chodil chodil po městě a hrál - tentokrát to ovšem byly písně ješte
cizokrajnější a pohádkovější. Ta melodie skoro uspávala...

Ale teď je ráno, svítalo už asi před hodinou a ty už jsi dávno po skromné rodinné snídani. Teda skoro rodinné -
- nebyli na ní tvoje dvě děti Johan a Erika, ale co na tom sejde, třeba ještě spí a ty máš teď jiné věci na starost měl by
jsi jít prodávat do svého obchůdku, aby tvoji zákazníci nečekali""",
        'options' : {
            'a' : 'Jdu prodávat chleba',
            'b' : 'Musím najít děti! Začnu poptáním se u sousedů'
            #'c' : 'Jdu vzbudit děti' # TODO
        },
        'links' : {
            'a' : 'SellingPath-1',
            'b' : 'Ask-Neighbors',
            'c' : '' # TODO
        },
        'conditionalOpt' : []
    },
    'SellingPath-1': {
        'action' : 'Create-var: Meet-Kovar; Ano',
        'text' : 
"""Napekl jsi čerstvý chleba a čekáš na svého prvního zákazníka dne.
...
..
.

A hle, tady je! Jde k tobě tvůj soused kovář a vypadá docela nervózně.

Kovář: Zdař bůh, neviděl jsi někde mého synka? Hledám Karla celé ráno, ale jakoby se do země propadl.""",
        'options' : {
            'a' : 'Karla? Ne, toho jsem jeste nepotkal. Ale to nevadí on se najde. Nechceš chleba?',
            'b' : 'To je divné... Moje děti taky někam zmizeli! Měli bychom se zeptat u sousedů.',
            # 'c' : 'Mám tvoje děti a už je nikdy neuvidíš!' # TODO
        },
        'links' : {
            'a' : 'SellingPath-2',
            'b' : 'Ask-Neighbors',
            'c' : '' # TODO
        },
        'conditionalOpt' : []
    },
    'SellingPath-2': {
        'action' : 'Money-bronz: +1',
        'text' : 
"""Kovář: Jo, chleba bych si vzal. Tady máš 1 mědák.""",
        'options' : {
            'a' : 'Poděkuju Kovářovi a půjdu dál prodávat',
            'b' : 'Chci od kováře víc peněž',
            # 'c' : 'Mám tvoje děti a už je nikdy neuvidíš!' # TODO
        },
        'links' : {
            'a' : 'SellingPath-Loop-1',
            'b' : 'SellingPath-More-Money', # TODO
            'c' : '' # TODO
        },
        'conditionalOpt' : []
    },
    'SellingPath-Loop-1': {
        'action' : '',
        'text' : 
"""Nic se neděje a děti pořád nikde. Možná bych je měl jít hledat.""",
        'options' : {
            'a' : 'NE, kašlu na to, jdu dál prodávat',
            'b' : 'Jdu se poptat u sousedů',
            'c' : 'Ukončit hru'
        },
        'links' : {
            'a' : 'SellingPath-Loop-2',
            'b' : 'Ask-Neighbors',
            'c' : 'END'
        },
        'conditionalOpt' : []
    },
    'SellingPath-Loop-2': {
        'action' : 'Create-var: Meet-Kovar; Ano',
        'text' : 
"""Napekl jsi znova čerstvý chleba a čekáš na svého dalšího zákazníka dne.

...
..
.
..
...

A hle, tady je! Jde k tobě tvůj soused kovář a vypadá docela nervózně.

Kovář: Zdař bůh, neviděl jsi někde mého synka Karla? Hledám ho celou věčnost, ale jakoby se do země propadl.""",
        'options' : {
            'a' : 'Karla? Ne, toho jsem jeste nepotkal. Ale to nevadí on se najde. Nechceš chleba?',
            'b' : 'To je divné... Moje děti taky někam zmizeli! Měli bychom se zeptat u sousedů.',
            # 'c' : 'Mám tvoje děti a už je nikdy neuvidíš!' # TODO
        },
        'links' : {
            'a' : 'SellingPath-Loop-3',
            'b' : 'Ask-Neighbors',
            'c' : '' # TODO
        },
        'conditionalOpt' : []
    },
    'SellingPath-Loop-3': {
        'action' : 'Money-bronz: +1',
        'text' : 
"""Kovář: Jo, chleba bych si vzal. Tady máš 1 mědák.""",
        'options' : {
            'a' : 'Poděkuju Kovářovi a půjdu dál prodávat',
            'b' : 'Chci od kováře víc peněž',
            # 'c' : 'Mám tvoje děti a už je nikdy neuvidíš!' # TODO
        },
        'links' : {
            'a' : 'SellingPath-Loop-1',
            'b' : 'SellingPath-More-Money',
            'c' : '' # TODO
        },
        'conditionalOpt' : []
    },
    'SellingPath-More-Money': {
        'action' : 'Money-bronz: +2',
        'text' : 
"""Ty: Heeej, kováři, tenhle chleba je kvalitní. Koukej mi dát další 2 měďáky!
Kovář: No dobře, tady máš ty peníze.""",
        'options' : {
            'a' : 'Poděkuju Kovářovi a půjdu dál prodávat',
            'b' : 'Chci od kováře víc peněž',
            # 'c' : 'Mám tvoje děti a už je nikdy neuvidíš!' # TODO
        },
        'links' : {
            'a' : 'SellingPath-Loop-1',
            'b' : 'SellingPath-More-Money',
            'c' : '' # TODO
        },
        'conditionalOpt' : []
    },
    'Ask-Neighbors': {
        'action' : '',
        'text' : 
"""Zaťukáš na dveře sousedního domu a skoro hned otevře sousedka.

Ty: Pozdrav bůh! Neviděli jste někde mé děti? Nikde je nemůžu najít.
Sousedka: Bohužel ne, ale počkat, naše děti jsou pryč také!""",
        'options' : {
            'a' : 'To je divné, pojdmě se poptat dále',
            'b' : 'Asi si někde hrají. Já jdu prodávat chleba',
            # 'c' : 'Mám tvoje děti a už je nikdy neuvidíš!' # TODO
        },
        'links' : {
            'a' : 'Ask-Neighbors-2',
            'b' : 'SellingPath-1',
            'c' : '' # TODO
        },
         'conditionalOpt' : [{
            'text' : 'Kováři zmizeli děti také, takže bychom se měli jít poptat dále',
            'condition' : 'game-var: Meet-Kovar; Ano',
            'link' : 'Ask-Neighbors-2'
        }]
    },
    'Ask-Neighbors-2': {
        'action' : 'Add-item: starý železný meč tvého souseda',
        'text' : 
"""Jdeš o dům dál a tam zaťukáš. Po chvilce se ve dveřích objeví soused a ty hned spustíš:
Ty: Dobrý den sousede! Neviděli jste někde mé děti? Nikde je nemůžu najít.
Soused: Děti jsem nikde neviděl, ale myslím, že je odvedl ten divný, slizký krysař! Na tady máš můj rodiný meč a najdi krysaře a přiveď svoje a moje aaa vlastně všechny děti zpátky domů.
""",
        'options' : {
            'a' : 'Ó děkuji za tento převzácný dar a slibuji, že se tohoto úkolu zhostím jak nejlépe to jen dokážu!',
            #'b' : '',# TODO
            # 'c' : '' # TODO
        },
        'links' : {
            'a' : 'END',
            'b' : '', # TODO
            'c' : '' # TODO
        },
         'conditionalOpt' : []
    },
    'END': {
        'action' : '',
        'text' : 
"""
Zde prozatím příběh končí a na pokračování si budeš muset chvíli počkat

díky za tvou pozornost
copyright @ David Laušman
""",
        'options' : {
        },
        'links' : {
        },
         'conditionalOpt' : []
    }
}