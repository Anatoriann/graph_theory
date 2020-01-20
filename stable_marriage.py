
def stable_marriage(p_chooser: dict, p_chosen: dict) -> dict:
    """
    A function that apply the algorithm of stable marriage
    :param p_chooser: The ones who do the serenade
    :param p_chosen: The ones who  are serenaded
    :return: A dict containing the result of the serenade
    """

    # I have to verify if the total capacity of the chosen is >= to the number of chooser
    k_chosen = p_chosen.keys()
    count = 0
    # Count the capacity of the chosen ones
    for keys in k_chosen:
        count += p_chosen[keys]['capacity']

    # Verify if the capacity of chosen is sufficient to satisfy all the choosers
    if count >= len(p_chooser):
        raise RuntimeError("Not sufficiently capacity for the chosen to satisfy all the choosers")

    # Add a field to know which choices are still available
    k_choser = p_chooser.keys()
    # Add a field to know which is the best choice the chooser can use
    for keys in k_choser:
        print(keys)

    # Need to create a way to see if for the chooser their choices are still available or not
    print("yolo")

    return []