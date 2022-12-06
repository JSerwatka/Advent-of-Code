from collections import deque
import re

starting_stack = {
	1: deque("RGHQSBTN"),
	2: deque("HSFDPZJ"),
	3: deque("ZHV"),
	4: deque("MZJFGH"),
	5: deque("TZCDLMSR"),
	6: deque("MTWVHZJ"),
	7: deque("TFPLZ"),
	8: deque("QVWS"),
	9: deque("WHLMTDNC")
}

starting_stack_test = {
    1: deque("ZN"),
    2: deque("MCD"),
    3: deque("P")
}

def find_moves(command):
    pattern = re.compile("move (\d+) from (\d+) to (\d+)")
    return pattern.findall(command)[0]

def move_crates(move_how_many, move_from, move_to, stack):
    for _ in range(move_how_many):
        element = stack[move_from].pop()
        stack[move_to].append(element)
        
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

