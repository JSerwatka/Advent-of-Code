points = 0

f = open("input.txt", "r")
all_forms = []
current_group = ""
for line in f:
    # for line break pause - add new group and clear var
    if line == "\n":
        all_forms.append(current_group)
        current_group = ""
    else:
        current_group += line.strip("\n")

all_forms.append("tibudoaobuatifgp")

for group_answ in all_forms:
    group_answ_set = set(group_answ)
    points += len(group_answ_set)

print(points)