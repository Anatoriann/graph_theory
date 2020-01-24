import yaml
from algorithms import stable_marriage
from algorithms.yaml_parser import parser

if __name__ == "__main__":

    yaml_path = input("Please enter the path to the YAML file : \n")

    global_dict = parser(yaml_path)

    choice = 'n'
    while choice.lower() not in ["s", "f"]:
        choice = input("Please enter which set of your file will do the bidding [first set (f) / second set (s)] : \n")

    l_key = list(global_dict.keys())
    if choice == 'f':
        chooser = global_dict[l_key[0]]
        chosen = global_dict[l_key[1]]
    else:
        chooser = global_dict[l_key[1]]
        chosen = global_dict[l_key[0]]

    matching_dict = stable_marriage.stable_marriage(chooser, chosen)

    with open("result.yaml", "w") as file:
        yaml.dump(matching_dict, file)

    print("You can find the results in ./result.yaml")
