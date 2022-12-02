choosing_roles = {
    "AX": "C",
    "AY": "A",
    "AZ": "B",
    "BX": "A",
    "BY": "B",
    "BZ": "C",
    "CX": "B",
    "CY": "C",
    "CZ": "A",
}

score_rules = {
    "X": 0,
    "Y": 3,
    "Z": 6,
}

shape_rules = {
    "A": 1,
    "B": 2,
    "C": 3,
}

def find_score():
    score = 0
    with open("../input.txt") as f:
        for combat in f:
            combat_without_spaces = combat.replace(" ", "").strip()
            chosen_shape = choosing_roles[combat_without_spaces]
            score += shape_rules[chosen_shape]
            score += score_rules[combat_without_spaces[-1]]
    return score

print(find_score()) 