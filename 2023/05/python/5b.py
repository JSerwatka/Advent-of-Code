from math import e
import re

def string_array_to_array_of_int(string_array):
    return [*map(int, string_array.strip().split(" "))]

def get_seeds(seed_line: str):
    seed_numbers_str_arr = re.findall(r"seeds: ((?:\d+\s?)+)", seed_line)[0]
    seed_numbers = string_array_to_array_of_int(seed_numbers_str_arr)
    seed_numbers_grouped = list(zip(*[iter(seed_numbers)] * 2))
    seed_ranges = [range(range_start, range_start + range_len) for range_start, range_len in seed_numbers_grouped]
    return seed_ranges
    # return [x for seed_range in seed_ranges for x in seed_range]    

def map_seeds_to_new_values(map_values, last_seed_ranges):
    new_seed_range = []

    for seed_range in last_seed_ranges:
        for index, map_value in enumerate(map_values):
            [destination_start, source_start, map_range] = map_value
            map_range = range(source_start, source_start + map_range)
            
            
            within_range = (seed_range[0] >= map_range[0]) and (seed_range[-1] <= map_range[-1])
            outside_range_left = (seed_range[0] < map_range[0]) and (seed_range[-1] <= map_range[-1]) and (seed_range[-1] >= map_range[0])
            outside_range_right = (seed_range[0] >= map_range[0]) and (seed_range[-1] > map_range[-1]) and (seed_range[0] < map_range[-1])

            # within range
            #     [          ] 
            #         #####         
            if within_range:
                shift_start = seed_range[0] - map_range[0]
                shift_end = seed_range[-1] - map_range[0]
                new_seed_range.append(range(destination_start + shift_start, destination_start + shift_end))
                seed_range = []
            
            # outside range left
            #     [          ] 
            #  #########
            elif outside_range_left:
                shift_start = 0
                shift_end = seed_range[-1] - map_range[0]
                new_seed_range.append(range(destination_start + shift_start, destination_start + shift_end))
                seed_range = range(seed_range[0], map_range[0])
                
            # outside range right
            #     [          ] 
            #           ###########
            elif outside_range_right:
                shift_start = seed_range[0] - map_range[0]
                shift_end = map_range[-1]
                new_seed_range.append(range(destination_start + shift_start, destination_start + shift_end))
                seed_range = range(map_range[-1] + 1, seed_range[-1] + 1)
            # outside range
            else:
                if index == (len(map_values) - 1):
                    new_seed_range.append(seed_range)

            if len(seed_range) == 0:
                break
        
    return new_seed_range

def main():
    last_seed_ranges = []
    with open("../input.txt") as f:
    # with open("../input_example.txt") as f:
        file_lines = f.readlines()
        last_seed_ranges = get_seeds(file_lines[0])
        map_values = []

        
        for [index, line] in enumerate(file_lines[2:]):
            map_description = re.fullmatch(r"\D+:\n", line)

            if map_description:
                continue
            if line == "\n":
                last_seed_ranges = map_seeds_to_new_values(map_values, last_seed_ranges)
                map_values = []
                continue
            
            map_values.append(string_array_to_array_of_int(line))

            # handle last line
            rest_file_len = (len(file_lines[2:]) - 1)
            if index == rest_file_len:
                last_seed_ranges = map_seeds_to_new_values(map_values, last_seed_ranges)
            # print("progress: ", round(index * 100 / rest_file_len), "%")
    r = [x[0] for x in last_seed_ranges]
    r.sort()
    print(r)
    return None

print(main())