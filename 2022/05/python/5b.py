from collections import deque
import re

starting_stack ={
	1: "RGHQSBTN",
	2: "HSFDPZJ",
	3: "ZHV",
	4: "MZJFGH",
	5: "TZCDLMSR",
	6: "MTWVHZJ",
	7: "TFPLZ",
	8: "QVWS",
	9: "WHLMTDNC"
}

starting_stack_test = {
    1: "ZN",
    2: "MCD",
    3: "P"
}

def find_moves(command):
    pattern = re.compile("move (\d+) from (\d+) to (\d+)")
    return pattern.findall(command)[0]

def move_crates(move_how_many, move_from, move_to, stack):
    moved_elements = stack[move_from][-move_how_many:]
    stack[move_from] = stack[move_from][:-move_how_many]
    stack[move_to] += moved_elements
        
def find_top_crates(stack):
    top_crates = ""
    for _, stack in stack.items():
        try:
            top_crates += stack[-1]
        except IndexError:
            continue
    return top_crates

def main(input_file, stack):
    with open(input_file) as f:
        for command in f:
            move_how_many, move_from, move_to = map(int, find_moves(command))
            move_crates(move_how_many, move_from, move_to, stack)
    return find_top_crates(stack)
            
print(main("../input.txt", starting_stack))

