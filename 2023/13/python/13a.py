import numpy as np

# Compare the first and second column
# are_equal = np.array_equal(arr[:, 0], arr[:, 1])

def count_reflections(pattern, index, axis):
    reflection_count = 1
    index_offset_left = -1
    index_offset_right = 2
    
    while True:
        try:
            col_row = pattern[index + index_offset_left, :] if axis == "row" else pattern[:, index + index_offset_left]
            next_col_row = pattern[index + index_offset_right, :] if axis == "row" else pattern[:, index + index_offset_right]
            
            is_equal = np.array_equal(col_row, next_col_row)
            if is_equal:
                reflection_count += 1
            else:
                return reflection_count
            
            index_offset_left -= 1
            index_offset_right += 1
        except IndexError:
            return reflection_count

def get_reflection_count(pattern):
    best_column_reflection_count = 0
    best_row_reflection_count = 0
    
    # test column reflections
    for index in range(pattern.shape[1] - 1):
        equal_columns = np.array_equal(pattern[:, index], pattern[:, index + 1])
        
        if equal_columns:
            reflections_count = count_reflections(pattern, index, "column")
            best_column_reflection_count = best_column_reflection_count if best_column_reflection_count > reflections_count else reflections_count
    
    # test row reflections
    for index in range(pattern.shape[0] - 1):
        equal_row = np.array_equal(pattern[index, :], pattern[index + 1, :])
        
        if equal_row:
            reflections_count = count_reflections(pattern, index, "row")
            best_row_reflection_count = best_row_reflection_count if best_row_reflection_count > reflections_count else reflections_count

    return  best_column_reflection_count if best_column_reflection_count > best_row_reflection_count else best_row_reflection_count
    
def main():
    # with open("../input.txt") as f:
    with open("../input_example.txt") as f:
        pattern = None
        for line in f:
            if line == "\n":
                print(get_reflection_count(pattern))
                pattern = None
            else:
                line_mapped = [0 if sing == "." else 1 for sing in line.strip()]
                if pattern is None:
                    pattern = np.empty((0, len(line_mapped)))
                pattern = np.append(pattern, [line_mapped], axis=0)
        # get_pattern_summary(pattern)

print(main())