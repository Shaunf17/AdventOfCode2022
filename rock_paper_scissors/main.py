result = { "rock" : { "rock" : 3, "paper" : 0, "scissors" : 6},
            "paper" : { "rock" : 6, "paper": 3, "scissors": 0},
            "scissors" : {"rock" : 0, "paper": 6, "scissors": 3}}

choice = { "rock": 1, "paper": 2, "scissors": 3}
opp = { "a": ["rock", 1], "b": ["paper", 2], "c": ["scissors", 3]}
plyr = { "x": opp["a"], "y": opp["b"], "z": opp["c"]}
plyr_2 = { "x": 0, "y": 3, "z": 6}

def read_file(file: str):
    with open(file) as f:
        return f.read().split("\n")

def get_result(round: str):
    o, p = round.lower().split(" ")
    return plyr[p][1] + result[plyr[p][0]][opp[o][0]]

def get_result_2(round: str):
    o, p = round.lower().split(" ")
    plyr_choice = {i for i in result if result[opp[o]][i] == plyr_2[p]}


if __name__ == "__main__":
    res = 0
    for round in read_file("input.txt"):
        res += get_result(round)

    print(opp["c"].get("scissors"))