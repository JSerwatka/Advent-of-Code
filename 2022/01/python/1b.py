
def find_top3_calories():
    single_elf_total = 0
    total_array = []
    with open("../input.txt") as f:
        for line in f:
            if line == "\n":
                total_array.append(single_elf_total)
                single_elf_total = 0
            else:
                single_elf_total += int(line)

    total_array.sort(reverse=True)

    return total_array[:3]

top_three_calories = find_top3_calories()
print(sum(top_three_calories)) # 200158
