storyObj = {
    0: {
        'action' : '',
        'text' : 'Jsi sam doma a mas hlad. Nikde neni, co jist, jenze ty vazne potrebujes neco do ust.',
        'options' : {
            'a' : 'condition',
            'b' : 'text var',
            'c' : 'math var'
        },
        'links' : {
            'a' : 1,
            'b' : 8,
            'c' : 11
        },
        'conditionalOpt' : []
    },
    1 : {
        'action' : 'Add-item: lahev',
        'text' : 'pridat lahev do inventare',
        'options' : {
            'a' : 'pridat chlebicek',
            'b' : 'smazat lahev',
            'c' : 'rozcesti'
        },
        'links' : {
            'a' : 4,
            'b' : 5,
            'c' : 0
        },
        'conditionalOpt' : [
            {
                'text' : 'dva',
                'condition' : 'health: >5',
                'link' : 2
            }
        ]
    },
    2: {
        'action' : '',
        'text' : 'jsi ve dvojce',
        'options' : {
            'a' : 'condition',
            'b' : 'text var',
            'c' : 'math var'
        },
        'links' : {
            'a' : 1,
            'b' : 8,
            'c' : 11
        },
        'conditionalOpt' : [
            {
                'text' : 'dva',
                'condition' : 'health: <5',
                'link' : 2
            }
        ]
    },
}