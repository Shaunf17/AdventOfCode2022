def read_file(file):
    with open(file) as f:
        return f.read()

def find_marker(stream: str, stop = 4):
    for i, c in enumerate(stream):
        if i == len(stream) - stop:
            break
        a = list(stream[i:i+stop])
        if len(a) == len(set(a)):
            return i + stop

if __name__ == "__main__":
    m = find_marker(read_file("input.txt"))
    print(m)

    m2 = find_marker(read_file("input.txt"), 14)
    print(m2)