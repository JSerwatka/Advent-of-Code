from collections import Counter
import numpy as np

def main():
    total = 0
    with open("../input.txt") as f:
    # with open("../input_example.txt") as f:
        platform = np.array([list(line.strip()) for line in f], dtype="S1")
        # I know that column and row lengths are the same
        platform_len = platform.shape[0]
        platform_tilted =  np.empty((platform_len, 0), dtype="S1")

        for line_index in range(platform_len):
            original_column = platform[:, line_index]
            last_obstacle_index = -1
            for index, sing in enumerate(original_column):
                match sing:
                    case b"#":
                        last_obstacle_index = index
                    case b"O":
                        original_column[index] = b"."
                        original_column[last_obstacle_index + 1] = b"O"
                        last_obstacle_index = last_obstacle_index + 1
            platform_tilted = np.column_stack((platform_tilted, original_column))
        
        rounded_rocks_by_row = Counter(np.where(platform_tilted == b"O")[0])
        
        for row_index, rounded_rocks_count in rounded_rocks_by_row.items():
            total += (platform_len - row_index) * rounded_rocks_count

    return total

print(main())
