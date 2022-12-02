result = { "rock" : { "rock" : 3, "paper" : 0, "scissors" : 6},
            "paper" : { "rock" : 6, "paper": 3, "scissors": 0},
            "scissors" : {"rock" : 0, "paper": 6, "scissors": 3}}

choice = { "rock": ["rock", 1], "paper": ["paper", 2], "scissors": ["scissors", 3]}
opp = { "a": choice["rock"], "b": choice["paper"], "c": choice["scissors"]}
plyr = { "x": choice["rock"], "y": choice["paper"], "z": choice["scissors"]}
plyr_2 = { "x": 0, "y": 3, "z": 6}

def read_file(file: str):
    with open(file) as f:
        return f.read().split("\n")

def get_result(round: str):
    o, p = round.lower().split(" ")
    return plyr[p][1] + result[plyr[p][0]][opp[o][0]]

def get_result_2(round: str):
    o, p = round.lower().split(" ")
    plyr_choice = ""
    for k, v in result.items():
        for i in v:
            if v[opp[o][0]] == plyr_2[p]:
                plyr_choice = k
    return choice[plyr_choice][1] + plyr_2[p]

if __name__ == "__main__":
    res = 0
    for round in read_file("input.txt"):
        res += get_result(round)

    print("Part 1:", res)

    res2 = 0
    for round in read_file("input.txt"):
        res2 += get_result_2(round)

    print("Part 2:", res2)