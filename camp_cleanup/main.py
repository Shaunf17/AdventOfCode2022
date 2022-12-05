def read_file(file):
    with open(file) as f:
        return f.read().split("\n")

def fully_contained(pairs: list[str]):
    ans = 0
    for p in pairs:
        p1, p2 = p.split(",")
        s1 = set(range(int(p1.split("-")[0]), int(p1.split("-")[1])+1, 1))
        s2 = set(range(int(p2.split("-")[0]), int(p2.split("-")[1])+1, 1))
        if s1.issubset(s2) or s2.issubset(s1):
            ans += 1
    
    return ans

def overlap(pairs: list[str]):
    ans = 0
    for p in pairs:
        p1, p2 = p.split(",")
        s1 = set(range(int(p1.split("-")[0]), int(p1.split("-")[1])+1, 1))
        s2 = set(range(int(p2.split("-")[0]), int(p2.split("-")[1])+1, 1))
        if s1.intersection(s2) or s2.intersection(s1):
            ans += 1
    
    return ans

print(fully_contained(read_file("input.txt")))
print(overlap(read_file("input.txt")))