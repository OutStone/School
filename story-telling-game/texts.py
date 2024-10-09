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
se hadal s konšeli na náměstí před radnicí a padlo přitom mnoho nesmírné množsví úražek na cti.

Ješte tentýž včerejší večer vzal znovu píšťalku a opět chodil chodil po městě a hrál - tentokrát to ovšem byly písně ješte
cizokrajnější a pohádkovější. Ta melodie skoro uspávala...

Ale teď je ráno, svítalo už asi před hodinou a ty už jsi dávno po skromné rodinné snídani. Teda skoro rodinné -
- nebyli na ní tvoje dvě děti Johan a Erika, ale co na tom sejde, třeba ještě spí a ty máš teď jiné věci na starost měl by
jsi jít prodávat do svého obchůdku, aby tvoji zákazníci nečekali""",
        'options' : {
            'a' : 'Jdu prodávat chleba',
            'b' : 'Jdu vzbudit děti', # TODO
            'c' : 'Kašlu na obchod - jdu kecat se sousedy' # TODO
        },
        'links' : {
            'a' : 1,
            'b' : 8, # TODO
            'c' : 11 # TODO
        },
        'conditionalOpt' : []
    },
    1: {
        'action' : '',
        'text' : 
"""Napekl jsi čerstvý chleba a čekáš na svého prvního zákazníka dne.
...
..
.

A hle, tady je! Jde k tobě tvůj soused kovář a vypadá docela nervózně.

Kovář: Zdař bůh, neviděl jsi někde mého synka? Hledám Karla celé ráno, ale jakoby se do země propadl.
Kovář: Jo, chleba bych si vzal. """,
        'options' : {
            'a' : 'Karla? Ne, toho jsem jeste nepotkal. ale to nevadí on se najde. Nechceš chleba?',
            'b' : 'To je divné... Moje děti taky někam zmizeli! Měli bychom se zeptat u sousedů.', # TODO
            # 'c' : 'Mám tvoje děti a už je nikdy neuvidíš!' # TODO
        },
        'links' : {
            'a' : 2,
            'b' : 8, # TODO
            'c' : 11 # TODO
        },
        'conditionalOpt' : []
    },
    1: {
        'action' : '',
        'text' : 
"""Kovář: Jo, chleba bych si vzal. Tady máš 1 mědák.
A hle, tady je! Jde k tobě tvůj soused kovář a vypadá docela nervózně.

Kovář: Zdař bůh, neviděl jsi někde mého synka? Hledám Karla celé ráno, ale jakoby se do země propadl.
Kovář: Jo, chleba bych si vzal. """,
        'options' : {
            'a' : 'Karla? Ne, toho jsem jeste nepotkal. ale to nevadí on se najde. Nechceš chleba?',
            'b' : 'To je divné... Moje děti taky někam zmizeli! Měli bychom se zeptat u sousedů.', # TODO
            # 'c' : 'Mám tvoje děti a už je nikdy neuvidíš!' # TODO
        },
        'links' : {
            'a' : 2,
            'b' : 8, # TODO
            'c' : 11 # TODO
        },
        'conditionalOpt' : []
    }
}