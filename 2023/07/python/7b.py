from collections import Counter, defaultdict

card_to_value_map =  {
    "A": 14,  
    "K": 13,
    "Q": 12,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "J": 1,
}

def count_card_strenght(cards: str):
    counted_cards = Counter(cards)
    
    # Handle jokers
    number_of_jokers = counted_cards["J"]
    if number_of_jokers == 5:
        return 7
    counted_cards.pop("J", None)
    card_with_highest_count = max(counted_cards, key=counted_cards.get)
    counted_cards[card_with_highest_count] += number_of_jokers

    match len(counted_cards):
        # Five of a kind
        case 1:
            return 7
        case 2:
            # Four of a kind
            if 4 in counted_cards.values():
                return 6
            # Full house
            else:
                return 5
        case 3:
            # Three of a kind
            if 3 in counted_cards.values():
                return 4
            # 2 pairs
            else:
                return 3
        # 1 pair
        case 4:
            return 2
        # High card
        case 5:
            return 1
        case _:
            print("Error: ", counted_cards)
            
  
def sort_cards(cards):
    return tuple(card_to_value_map[card] for card in cards)

def main():
    total = 0
    with open("../input.txt") as f:
    # with open("../input_example.txt") as f:
        lines = f.readlines()
        split_lines = [line.split(" ") for line in lines]
        card_to_bid_dict = {card:int(bid) for card, bid in split_lines}     
        
        cards_grouped_by_strength = defaultdict(list)
        cards_list_sorted = []
        for card in card_to_bid_dict.keys():
            cards_grouped_by_strength[count_card_strenght(card)].append(card)
        
        for strenght in sorted(cards_grouped_by_strength.keys()):
            for card in sorted(cards_grouped_by_strength[strenght], key=sort_cards):
                cards_list_sorted.append(card)

        for index, card in enumerate(cards_list_sorted):
            total += card_to_bid_dict[card] * (index + 1)
        
        return total
            
print(main())