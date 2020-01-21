import stable_marriage
import yaml

if __name__ == "__main__":
    print('parser')
    global_dict = {}
    # chooser = {'cyril': {'capacity': 1, 'ranking': {'enseeiht': 1, 'ensimag': 2}},
    #            'guilhem': {'capacity': 1, 'ranking': {'enseeiht': 1, 'ensimag': 2}},
    #            'titouan': {'capacity': 1, 'ranking': {'ensimag': 2, 'enseeiht': 1}}}
    # chosen = {'enseeiht': {'capacity': 1, 'ranking': {'cyril': 1, 'guilhem': 2, 'titouan': 3}},
    #           'ensimag': {'capacity': 2, 'ranking': {'cyril': 2, 'titouan': 3, 'guilhem': 1}}}
    # global_dict['seta'] = chooser
    # global_dict['setb'] = chosen

    with open("test2.yaml", "r") as file:
        global_dict = yaml.safe_load(file)

    choice = 'n'
    while choice.lower() not in ["s", "f"]:
        choice = input("Which set is the chooser (the one which do the serenade)? first (f) or second (s)\n")

    l_key = list(global_dict.keys())
    if choice == 'f':
        chooser = global_dict[l_key[0]]
        chosen = global_dict[l_key[1]]
    else:
        chooser = global_dict[l_key[0]]
        chosen = global_dict[l_key[1]]

    matching_dict = stable_marriage.stable_marriage(chooser, chosen)

    with open("result.yaml", "w") as file:
        yaml.dump(matching_dict, file)

    print("Results in ./result.yaml")
