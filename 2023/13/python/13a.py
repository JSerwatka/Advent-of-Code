import numpy as np

def check_is_reflection(pattern, index, size, axis):
    index_offset_left = -1
    index_offset_right = 2
    last_index = size - 1

    while True:
        if (index + index_offset_left) < 0 or (index + index_offset_right) > last_index:
            return True
        
        col_row = pattern[index + index_offset_left, :] if axis == "row" else pattern[:, index + index_offset_left]
        next_col_row = pattern[index + index_offset_right, :] if axis == "row" else pattern[:, index + index_offset_right]
        
        is_equal = np.array_equal(col_row, next_col_row)
        
        if not is_equal:
            return False
        
        index_offset_left -= 1
        index_offset_right += 1

def get_reflection_index(pattern):
    # test column reflections
    col_size = pattern.shape[1]
    for index in range(col_size - 1):
        equal_columns = np.array_equal(pattern[:, index], pattern[:, index + 1])
        
        if equal_columns and check_is_reflection(pattern, index, col_size, "column"):
            return { "index": index, "type": "column"}
    
    # test row reflections
    row_size = pattern.shape[0]
    for index in range(row_size - 1):
        equal_row = np.array_equal(pattern[index, :], pattern[index + 1, :])
        
        if equal_row and check_is_reflection(pattern, index, row_size, "row"):
            return { "index": index, "type": "row"}

    raise ValueError("no reflections")

def calculate_pattern_value(pattern):
    reflection = get_reflection_index(pattern)
    
    if reflection["type"] == "row":
        return (reflection["index"] + 1) * 100
    return reflection["index"] + 1
    
def main():
    total = 0

    with open("../input.txt") as f:
    # with open("../input_example.txt") as f:
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
