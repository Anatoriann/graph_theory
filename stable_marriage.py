
def stable_marriage(p_chooser: dict, p_chosen: dict) -> dict:
    """
    A function that apply the algorithm of stable marriage
    :param p_chooser: The ones who do the serenade
    :param p_chosen: The ones who  are serenaded
    :return: A dict containing the result of the serenade
    """

    # I have to verify if the total capacity of the chosen is >= to the number of chooser
    k_chosen = p_chosen.keys()
    count_chosen = 0
    # Count the capacity of the chosen ones
    for keys in k_chosen:
        count_chosen += p_chosen[keys]['capacity']
        # Init an empty list of chooser for each step
        p_chosen[keys]['pretendant'] = []

    # Count the capacity of chooser
    k_chooser = p_chooser.keys()
    count_chooser = 0
    # Count the capacity of the chosen ones
    for keys in k_chooser:
        count_chooser += p_chooser[keys]['capacity']

    # Verify if the capacity of chosen is sufficient to satisfy all the choosers
    if count_chosen != count_chooser:
        raise RuntimeError("Different number of chooser and chosen")

    sorted_choice_chooser = {}
    # Create of list that are sorted for the choosers
    for chooser in k_chooser:
        sorted_choice_chooser[chooser] = []
        # We know that each ranking is unical so we can use the number of
        # keys to sort
        for i in range(1, len(p_chooser[chooser]['ranking']) + 1):
            # Iterate on the chosen of the chooser
            for chosen in p_chooser[chooser]['ranking'].keys():
                # If we have the right rank, we append to have the right index
                if p_chooser[chooser]['ranking'][chosen] == i:
                    sorted_choice_chooser[chooser].append(chosen)
                    break

    # In the field ranking, we going to have 3 possible values :
    # - A : Accepted by the chosen
    # - R : Rejected by the chosen
    # - a name : Representing the chosen we want, the chooser don't have seen the chosen yet

    # Ending condition
    verified = False

    while not verified:
        # Attribute the chooser to the chosen
        for chooser in k_chooser:
            nb_attribuate = 0
            pretendant_capacity = p_chooser[chooser]['capacity']
            # Parcourir les clé des prétendants pour voir combien sont attribuées
            # Et attribuer si besoin
            for i in range(len(sorted_choice_chooser[chooser])):
                # If the chooser is already serenading, we increment the nb of already attribuate for the step
                if sorted_choice_chooser[chooser][i].lower() == 'a':
                    nb_attribuate += 1
                # Since we know that the chosen are sort, we can just see if it's not attributed yet and attribute it
                elif nb_attribuate < pretendant_capacity:
                    if sorted_choice_chooser[chooser][i].lower() != 'r':
                        # Add the chooser to the chosen list
                        p_chosen[sorted_choice_chooser[chooser][i]]['pretendant'].append(chooser)
                        nb_attribuate += 1
                        sorted_choice_chooser[chooser][i] = 'a'

        verified = True
        for chosen in k_chosen:
            # If we have more pretendant than the capacity, reject the worst one
            if len(p_chosen[chosen]['pretendant']) > p_chosen[chosen]['capacity']:
                verified = False
                # Sort the list of pretendant
                tri = False
                while not tri:
                    tri = True
                    for i in range(len(p_chosen[chosen]['pretendant']) - 1):
                        if p_chosen[chosen]['ranking'][p_chosen[chosen]['pretendant'][i]] > p_chosen[chosen]['ranking'][p_chosen[chosen]['pretendant'][i + 1]]:
                            tri = False
                            tmp = p_chosen[chosen]['pretendant'][i]
                            p_chosen[chosen]['pretendant'][i] = p_chosen[chosen]['pretendant'][i + 1]
                            p_chosen[chosen]['pretendant'][i + 1] = tmp

                # Cut the last elements and says it's rejected to the chooser
                r_chooser = p_chosen[chosen]['pretendant'][p_chosen[chosen]['capacity']:len(p_chosen[chosen]['pretendant'])]
                p_chosen[chosen]['pretendant'] = p_chosen[chosen]['pretendant'][0:p_chosen[chosen]['capacity']]

                for chooser in r_chooser:
                    # Get the rank of the school for the chooser
                    chooser_rank = p_chooser[chooser]['ranking'][chosen]
                    # Say rejected
                    sorted_choice_chooser[chooser][chooser_rank - 1] = 'r'

    # Create a dict with only the name of the chosen and the list of chooser
    return_dict = {}
    for chosen in k_chosen:
        return_dict[chosen] = p_chosen[chosen]['pretendant']

    return return_dict