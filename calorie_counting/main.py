# with open("input.txt") as f:
#     lines = f.read()
#     split = str.split(lines, "\n\n")
    
#     highest_cal = 0
#     for i in split:
#         total = 0
#         items = str.split(i, "\n")
#         print(items)
#         for x in items:
#             total += int(x)

#         print("total: ", total)

#         if total > highest_cal:
#             highest_cal = total

#     print("highest cal: ", highest_cal)

class Elf:
    def __init__(self, total, cals):
        self.total = total
        self.cals = cals

    def __str__(self):
        return f"CALS: {self.cals}\nTOTAL: {self.total}\n"

def get_list():
    with open("input.txt") as f:
        lines = f.read()
        split = str.split(lines, "\n\n")

        list = []
        for i in split:
            total = 0
            item = str.split(i, "\n")
            for cal in item:
                total += int(cal)
            list.append(Elf(total, item))

        return list

def sort_list(list, r):
    return sorted(list, key=lambda x: x.total, reverse=r)

def print_list(list):
    for i in l_sorted:
        print(i)

def combined_total_cals(list, n):
    combined_total = 0
    for i in range(n):
        combined_total += list[i].total

    return combined_total

l_sorted = sort_list(get_list(), True)
print_list(l_sorted)
c = combined_total_cals(l_sorted, 3)
print(c)