import re

def find_symbols_indexes(line: str):
    found_symbols = re.finditer(r"[^\w\.\n]", line)
    matches = [x for x in found_symbols]

    return [match.span() for match in matches]

def find_accepted_numbers_in_line(current_line_index: int, lines: list[str]):
    current_line = lines[current_line_index]
    found_numbers = re.finditer(r"\d+", current_line)
    accepted_numbers = []
    
    previous_line_symbols = find_symbols_indexes(lines[current_line_index - 1]) if current_line_index > 0 else None 
    next_line_symbols = find_symbols_indexes(lines[current_line_index + 1]) if current_line_index < (len(lines) - 1) else None 
    
    for number in found_numbers:
        [start, end] = number.span()

        # is previous symbol?
        if start > 0 and re.match(r"[^\w\.\n]", current_line[start - 1]):
            accepted_numbers.append(int(number[0]))
            continue
        
        # is next symbol?
        if end < len(current_line) and re.match(r"[^\w\.\n]", current_line[end]):
            accepted_numbers.append(int(number[0]))
            continue
    
        # is in previous line?
        if previous_line_symbols:
            found_adjacents = [[symbol_start, symbol_end] for [symbol_start, symbol_end] in previous_line_symbols if (start-1 <= symbol_start and symbol_start <= end)]

            if (len(found_adjacents)):
                accepted_numbers.append(int(number[0]))
                continue
        
        # is in next line?
        if next_line_symbols:
            found_adjacents = [[symbol_start, symbol_end] for [symbol_start, symbol_end] in next_line_symbols if (start-1 <= symbol_start and symbol_start <= end)]
            if (len(found_adjacents)):
                accepted_numbers.append(int(number[0]))
                continue
    return accepted_numbers


def main():
    with open("../input.txt") as f:
    # with open("../input_example.txt") as f:
        lines = f.readlines()
        all_accepted_numbers = []
        for index in range(len(lines)):
            line_accepted_numbers = find_accepted_numbers_in_line(index, lines)
            if len(line_accepted_numbers):
                all_accepted_numbers = [*all_accepted_numbers, *line_accepted_numbers]
                # all_accepted_numbers.append(*line_accepted_numbers)

        return sum(all_accepted_numbers)
print(main())
