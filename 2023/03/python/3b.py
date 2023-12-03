import re
from functools import reduce

def find_symbols_indexes(line: str):
    found_symbols = re.finditer(r"\*", line)
    matches = [x for x in found_symbols]

    return [match.span() for match in matches]

def find_accepted_numbers_in_line(current_line_index: int, lines: list[str], numbers_by_gear):
    current_line = lines[current_line_index]
    found_numbers = re.finditer(r"\d+", current_line)
    
    previous_line_symbols = find_symbols_indexes(lines[current_line_index - 1]) if current_line_index > 0 else None 
    next_line_symbols = find_symbols_indexes(lines[current_line_index + 1]) if current_line_index < (len(lines) - 1) else None 
    
    for number in found_numbers:
        [start, end] = number.span()
        # is previous symbol?
        if start > 0:
            found_gear = current_line[start - 1] == "*"
            if (found_gear):
                gear_code = f"{current_line_index}{start-1}{start}"
                if gear_code not in numbers_by_gear:
                    numbers_by_gear[gear_code] = []
                
                numbers_by_gear[gear_code].append(int(number[0]))
                continue
        
        # is next symbol?
        if end < len(current_line):
            found_gear = current_line[end] == "*"
            if (found_gear):
                gear_code = f"{current_line_index}{end}{end + 1}"
                if gear_code not in numbers_by_gear:
                    numbers_by_gear[gear_code] = []
                
                numbers_by_gear[gear_code].append(int(number[0]))
                continue
    
        # is in previous line?
        if previous_line_symbols:
            found_gears = [[symbol_start, symbol_end] for [symbol_start, symbol_end] in previous_line_symbols if (start-1 <= symbol_start and symbol_start <= end)]

            for [gear_start, gear_end] in found_gears:
                gear_code = f"{current_line_index - 1}{gear_start}{gear_end}"
                if gear_code not in numbers_by_gear:
                    numbers_by_gear[gear_code] = []
                
                numbers_by_gear[gear_code].append(int(number[0]))
                continue
        
        # is in next line?
        if next_line_symbols:
            found_gears = [[symbol_start, symbol_end] for [symbol_start, symbol_end] in next_line_symbols if (start-1 <= symbol_start and symbol_start <= end)]
            
            for [gear_start, gear_end] in found_gears:
                gear_code = f"{current_line_index + 1}{gear_start}{gear_end}"
                if gear_code not in numbers_by_gear:
                    numbers_by_gear[gear_code] = []
                
                numbers_by_gear[gear_code].append(int(number[0]))
                continue

def main():
    with open("../input.txt") as f:
    # with open("../input_example.txt") as f:
        lines = f.readlines()
        numbers_by_gear = {}
        total = 0
        for index in range(len(lines)):
            find_accepted_numbers_in_line(index, lines, numbers_by_gear)
        for numbers in numbers_by_gear.values():
            if (len(numbers) == 2):
                total += reduce(lambda a,b: a*b, numbers)

        return total
print(main())
