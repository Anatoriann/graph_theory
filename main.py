import stable_marriage

chooser = {'cyril': {'capacity': 1, 'ranking': {'enseeiht': 1}}, 'guilhem': {'capacity': 1, 'ranking': {'enseeiht': 1}}}
chosen = {'enseeiht': {'capacity': 5, 'ranking': {'cyril': 1, 'guilhem': 2}}}

stable_marriage.stable_marriage(chooser, chosen)

