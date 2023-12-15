from collections import Counter
import numpy as np

def check_is_reflection(pattern, index, size, axis, is_smudge_cleaned):
    index_offset_left = -1
    index_offset_right = 2
    last_index = size - 1

    while True:
        if (index + index_offset_left) < 0 or (index + index_offset_right) > last_index:
            return True
        
        col_row = pattern[index + index_offset_left, :] if axis == "row" else pattern[:, index + index_offset_left]
        next_col_row = pattern[index + index_offset_right, :] if axis == "row" else pattern[:, index + index_offset_right]
        
        is_equal, is_smudge_cleaned = check_equality(col_row, next_col_row, is_smudge_cleaned)
        
        if not is_equal:
            return False
        
        index_offset_left -= 1
        index_offset_right += 1

def check_equality(row_col, next_row_col, is_smudge_cleaned):
    difference = sum(np.abs(row_col-next_row_col))
    
    if difference == 0:
        return (True, is_smudge_cleaned)
    if difference == 1 and not is_smudge_cleaned:
        return (True, True)
    return (False, is_smudge_cleaned)

def get_reflection_index(pattern):
    # test column reflections
    col_size = pattern.shape[1]
    for index in range(col_size - 1):
        col = pattern[:, index]
        next_col = pattern[:, index + 1]
        
        is_equal, is_smudge_cleaned = check_equality(col, next_col, False)
        
        if is_equal and check_is_reflection(pattern, index, col_size, "column", is_smudge_cleaned):
            return { "index": index, "type": "column"}
    
    # test row reflections
    row_size = pattern.shape[0]
    for index in range(row_size - 1):
        is_smudge_cleaned = False
        row = pattern[index, :]
        next_row = pattern[index + 1, :]
        
        is_equal, is_smudge_cleaned = check_equality(row, next_row, False)
        
        if is_equal and check_is_reflection(pattern, index, row_size, "row", is_smudge_cleaned):
            return { "index": index, "type": "row"}

    raise ValueError("no reflections")

def calculate_pattern_value(pattern):
    reflection = get_reflection_index(pattern)
    
    if reflection["type"] == "row":
        return (reflection["index"] + 1) * 100
    return reflection["index"] + 1
    
def main():
    total = 0

    # with open("../input.txt") as f:
    with open("../input_example.txt") as f:
        pattern = None
        for line in f:
            if line == "\n":
                total += calculate_pattern_value(pattern)
                pattern = None
            else:
                line_mapped = [0 if sing == "." else 1 for sing in line.strip()]
                if pattern is None:
                    pattern = np.empty((0, len(line_mapped)), dtype=np.int8)
                pattern = np.append(pattern, [line_mapped], axis=0)
        total += calculate_pattern_value(pattern)
    return total

print(main())
