import re
from collections import deque

def move_stack(crates: str, instr: str):
    stacks = []
    for line in crates.splitlines():
        for i, idx in enumerate(range(1, len(line), 4)):
            while i >= len(stacks):
                stacks.append(deque())
            if line[idx] != " ":
                stacks[i].append(line[idx])

    for inst in instr.splitlines():
        a, b, c = map(int, re.findall(r"\d+", inst))
        for i in range(a):
            stacks[c - 1].appendleft(stacks[b - 1].popleft())

    return "".join(x[0] for x in stacks)

def move_stack_multiple(crates: str, instr: str):
    stacks = []

    for line in crates.splitlines():
        for i, idx in enumerate(range(1, len(line), 4)):
            while i >= len(stacks):
                stacks.append(deque())
            if line[idx] != " ":
                stacks[i].append(line[idx])

    for inst in instr.splitlines():
        a, b, c = map(int, re.findall(r"\d+", inst))
        temp = deque()
        for i in range(a):
            temp.appendleft(stacks[b - 1].popleft())
        stacks[c - 1].extendleft(temp)

    return "".join(x[0] for x in stacks)

def read_file(file):
    with open(file) as f:
        return f.read()

if __name__ == "__main__":
    crates, instr = read_file("input.txt").split("\n\n")
    p1 = move_stack(crates, instr)
    print(p1)

    p2 = move_stack_multiple(crates, instr)
    print(p2)