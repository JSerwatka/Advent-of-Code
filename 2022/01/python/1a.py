
def find_highest_calories():
    total = 0
    highest_total = 0
    with open("../input.txt") as f:
        for line in f:
            if line == "\n":
                highest_total = total if total > highest_total else highest_total
                total = 0
            else:
                total += int(line)
    return highest_total

print(find_highest_calories()) # 67658