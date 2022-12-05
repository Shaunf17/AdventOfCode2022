from string import ascii_lowercase, ascii_uppercase

def get_priority():
    priority = {}
    i = 0
    for s in ascii_lowercase:
        i += 1
        priority[s] = i

    for s in ascii_uppercase:
        i += 1
        priority[s] = i

    return priority

def read_file(file: str) -> list[str]:
    with open(file) as f:
        return f.read().split("\n")

def get_comparts(item: str) -> list[str]:
    return item[:len(item)//2], item[len(item)//2:]

def get_common_char(s1: str, s2: str, s3 = None):
    if s3 == None:
        c =  set(s1) & set(s2)
    else:
        c = set(s1) & set(s2) & set(s3)
    return ''.join(c)

def get_groups(l: list):
    g = []
    for i in range(0, len(l), 3):
        try:
            g.append([l[i], l[i+1], l[i+2]])
        except IndexError:
            print("Index error")

    return g

if __name__ == "__main__":
    p = get_priority()
    list = read_file("input.txt")
    comparts = []
    common = []
    
    for item in list:
        c = get_comparts(item)
        comparts.append(c)
        common.append(get_common_char(c[0], c[1]))

    total = 0
    for i in common:
        total += p[i]

    print("PART 1: ", total)

    groups = get_groups(list)
    total_g = 0
    for g in groups:
        total_g += p[get_common_char(g[0], g[1], g[2])]

    print("PART 2: ", total_g)