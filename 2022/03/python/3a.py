def create_halves(rucksack):
    half_len = int(len(rucksack)/2)
    return rucksack[:half_len], rucksack[half_len:]

def find_shared_items(first_half, second_half):
    return set(first_half) & set(second_half)

def calculate_item_priority(letter):
    if letter.islower():
        return ord(letter) - ord("a") + 1
    else: 
        return ord(letter) - ord("A") + 27

def main(input_path):
    all_items = []
    with open(input_path) as f:
        for rucksack in f:
            first_half, second_half = create_halves(rucksack.strip())
            shared_items = find_shared_items(first_half, second_half)
            all_items.append(*shared_items)
    items_values = [calculate_item_priority(el) for el in all_items]
    return sum(items_values)

print(main("../input.txt"))
