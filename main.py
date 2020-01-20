import stable_marriage

chooser = {'cyril': {'capacity': 1, 'ranking': {'enseeiht': 1, 'ensimag': 2}},
           'guilhem': {'capacity': 1, 'ranking': {'enseeiht': 1, 'ensimag': 2}},
           'titouan': {'capacity': 1, 'ranking': {'ensimag': 2, 'enseeiht': 1}}}
chosen = {'enseeiht': {'capacity': 1, 'ranking': {'cyril': 1, 'guilhem': 2, 'titouan': 3}},
          'ensimag': {'capacity': 2, 'ranking': {'cyril': 2, 'titouan': 3, 'guilhem': 1}}}

print(stable_marriage.stable_marriage(chooser, chosen))

