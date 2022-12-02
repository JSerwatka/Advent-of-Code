winning_rules = {
    "AX": 3,
    "AY": 6,
    "AZ": 0,
    "BX": 0,
    "BY": 3,
    "BZ": 6,
    "CX": 6,
    "CY": 0,
    "CZ": 3,
}

shape_rules = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

def find_score():
    score = 0
    with open("../input.txt") as f:
        for combat in f:
            combat_without_spaces = combat.replace(" ", "").strip()
            score += winning_rules[combat_without_spaces]
            score += shape_rules[combat_without_spaces[-1]]
    return score

print(find_score()) 