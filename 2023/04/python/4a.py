import re

def get_card_value(line: str):
    card_points = 0
    matches = re.findall(r"Card\s+\d+: ([\d+ ]+) \| ([\d+ ]+)", line)
    winning_numbers_raw = matches[0][0].split(" ")
    my_numbers_raw = matches[0][1].split(" ")
    
    winning_numbers = [*filter(lambda x: len(x) > 0, winning_numbers_raw)]
    my_numbers = [*filter(lambda x: len(x) > 0, my_numbers_raw)]

    for winning_number in winning_numbers:
        if winning_number in my_numbers:
            card_points = 1 if card_points == 0 else card_points * 2
    return card_points


def main():
    total = 0
    with open("../input.txt") as f:
    # with open("../input_example.txt") as f:
        for line in f:
            total += get_card_value(line) 
    return total

print(main())