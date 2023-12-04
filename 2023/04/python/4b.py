import re

card_count_dict = {}

def get_card_count(line: str):
    card_points = 0
    matches = re.findall(r"Card\s+(\d+): ([\d+ ]+) \| ([\d+ ]+)", line)
    card_number = int(matches[0][0])      
    
    # get numbers
    winning_numbers_raw = matches[0][1].split(" ")
    my_numbers_raw = matches[0][2].split(" ")
    winning_numbers = [*filter(lambda x: len(x) > 0, winning_numbers_raw)]
    my_numbers = [*filter(lambda x: len(x) > 0, my_numbers_raw)]
    
    # count points
    for winning_number in winning_numbers:
        if winning_number in my_numbers:
            card_points += 1
            
    # create card copies
    for card_copy_number in range(card_number + 1, card_number + card_points + 1):
        card_count_dict[card_copy_number] = card_count_dict[card_copy_number] + card_count_dict[card_number]
    
def main():
    with open("../input.txt") as f:
    # with open("../input_example.txt") as f:
        lines = f.readlines()
        for i in range(len(lines)):
            card_count_dict[i+1] = 1
        for line in lines:
            get_card_count(line) 
    return sum(card_count_dict.values())

print(main())