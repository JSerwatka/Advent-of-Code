def find_shared_items(first_line, second_line, third_line):
    return set(first_line) & set(second_line) & set(third_line)

def calculate_item_priority(letter):
    if letter.islower():
        return ord(letter) - ord("a") + 1
    else: 
        return ord(letter) - ord("A") + 27

def main(input_path):
    with open(input_path) as f:
        all_ruckcacks = f.read().splitlines()

    ruckcacks_grouped_by_three = [all_ruckcacks[i:i+3] for i in range(0, len(all_ruckcacks), 3)]
    shared_items = [find_shared_items(*three_lines) for three_lines in ruckcacks_grouped_by_three]
    items_values = [calculate_item_priority(*el) for el in shared_items]
    return sum(items_values)



print(main("../input.txt"))