def get_result_2(round: str):
    o, p = round.lower().split(" ")
    # plyr_choice = {i for i in result if result[opp[o]][i] == plyr_2[p]}
    plyr_choice = {i for i in result if result[opp[o][0]][i] == plyr_2[p]}
    #val = choice[plyr_choice]
    #return val
    return plyr_choice