from collections import Counter
import numpy as np

def pretty_print_platform(platform):
    for line in platform:
        print(line.tobytes().decode())

def tilt(platform, platform_len, tilt_direction):    
    tilt_settings = {
        "north": {
            "platform_size": (platform_len, 0),
            "row_col": lambda index: platform[:, index],
            "range": range(platform_len),
            "starting_point": -1,
            "index_update": 1,
            "append_func": lambda platform_tilted, col: np.column_stack((platform_tilted, col))
        },
        "south": {
            "platform_size": (platform_len, 0),
            "row_col": lambda index: platform[:, index],
            "range": range(platform_len-1, -1, -1),
            "starting_point": platform_len,
            "index_update": -1,
            "append_func": lambda platform_tilted, col: np.column_stack((platform_tilted, col))
        },
        "west": {
            "platform_size": (0, platform_len),
            "row_col": lambda index: platform[index, :],
            "range": range(platform_len),
            "starting_point": -1,
            "index_update": 1,
            "append_func": lambda platform_tilted, row: np.row_stack((platform_tilted, row))
        },
        "east": {
            "platform_size": (0, platform_len),
            "row_col": lambda index: platform[index, :],
            "range": range(platform_len-1, -1, -1),
            "starting_point": platform_len,
            "index_update": -1,
            "append_func": lambda platform_tilted, row: np.row_stack((platform_tilted, row))
        },
    }
    
    platform_tilted =  np.empty(tilt_settings[tilt_direction]["platform_size"], dtype="S1")
            
    for line_index in range(platform_len):
        row_col = tilt_settings[tilt_direction]["row_col"](line_index)
        last_obstacle_index = tilt_settings[tilt_direction]["starting_point"]
        for index in tilt_settings[tilt_direction]["range"]:
            sing = row_col[index]
            match sing:
                case b"#":
                    last_obstacle_index = index
                case b"O":
                    row_col[index] = b"."
                    new_stone_index = last_obstacle_index + tilt_settings[tilt_direction]["index_update"]
                    row_col[new_stone_index] = b"O"
                    last_obstacle_index = new_stone_index
        platform_tilted = tilt_settings[tilt_direction]["append_func"](platform_tilted, row_col)
    
    return platform_tilted

def main(number_of_cycles):
    total = 0
    with open("../input.txt") as f:
    # with open("../input_example.txt") as f:
        platform = np.array([list(line.strip()) for line in f], dtype="S1")
        # I know that column and row lengths are the same
        platform_len = platform.shape[0]
        for _ in range(number_of_cycles):
            for tilt_direction in ["north", "west", "south", "east"]:
                platform = tilt(platform, platform_len, tilt_direction)
        
        rounded_rocks_by_row = Counter(np.where(platform == b"O")[0])
        
        for row_index, rounded_rocks_count in rounded_rocks_by_row.items():
            total += (platform_len - row_index) * rounded_rocks_count

    return total

print(main(1_000_000_000))
