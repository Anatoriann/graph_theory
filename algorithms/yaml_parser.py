import yaml


def parser(path):
    """
    Parses the input YAML File : Add's a capacity of one to each values dict that doesn't contain this key:value
    Checks if every values of a set A contains every values of a set B and if the raking values are unique
    :param path: The path of the YAML File
    :return: The parsed and modified data structure found in the input YAML file
    """
    with open(path, 'r') as file:
        loaded_data = yaml.safe_load(file)
    keys_data = loaded_data.keys()
    set_a = list(keys_data)[0]
    set_b = list(keys_data)[1]
    set_a_capacity = 0
    set_b_capacity = 0
    nb_elements_set_a = 0
    nb_elements_set_b = 0
    errors_found = False

    for keys in list(keys_data):
        for values in loaded_data[keys]:
            if keys == set_a:
                nb_elements_set_a += 1
            elif keys == set_b:
                nb_elements_set_b += 1
            struct = loaded_data[keys][values]
            if "capacity" not in struct:
                struct["capacity"] = 1

    for a_val in loaded_data[set_a]:
        for ranks_a in loaded_data[set_a][a_val]["ranking"].values():
            if not 1 <= ranks_a <= nb_elements_set_b:
                print("ERROR : One or more ranks of the element '" + str(a_val) + "' in the data set '" + str(set_a) + "' have an incorrect value. \n")
                errors_found = True

    for b_val in loaded_data[set_b]:
        for ranks_b in loaded_data[set_b][b_val]["ranking"].values():
            if not 1 <= ranks_b <= nb_elements_set_a:
                print("ERROR : One or more ranks of the element '" + str(b_val) + "' in the data set '" + str(set_b) + "' have an incorrect value. \n")
                errors_found = True

    for a_val in loaded_data[set_a]:
        set_a_capacity += loaded_data[set_a][a_val]["capacity"]
        for b_val in loaded_data[set_b]:
            if b_val not in list(loaded_data[set_a][a_val]["ranking"].keys()):
                print("ERROR : The data set '" + str(a_val) + "' is missing value : " + str(b_val) + "\n")
                errors_found = True

    for b_val in loaded_data[set_b]:
        set_b_capacity += loaded_data[set_b][b_val]["capacity"]
        for a_val in loaded_data[set_a]:
            if a_val not in list(loaded_data[set_b][b_val]["ranking"].keys()):
                print("ERROR : The data set '" + str(b_val) + "' is missing value : " + str(a_val) + "\n")
                errors_found = True

    if set_a_capacity != set_b_capacity:
        print("ERROR : The total capacity of the data set '" + str(set_a) + "' is not equals to the total capacity of "
                                                                            "the data set `" + str(set_b) + "`\n")
        errors_found = True

    for keys in list(keys_data):
        for values in loaded_data[keys]:
            struct = loaded_data[keys][values]["ranking"].values()
            if duplicates_check(list(struct)):
                print("ERROR : Ranking values are not unique in the '" + str(values) + "' data set\n")
                errors_found = True

    if errors_found:
        raise RuntimeError("INVALID YAML FILE, PLEASE CHECK THE ERROR(S) LOG(S) SHOWN ABOVE")

    return loaded_data


def duplicates_check(elements_list):
    """
    Checks if a given list contains any duplicates
    :param elements_list: A simple python list
    :return: Boolean -> True if the list contains dupes, False if not
    """
    if len(elements_list) == len(set(elements_list)):
        return False
    return True
