import re

def string_array_to_array_of_int(string_array):
    return [*map(int, string_array.strip().split(" "))]

def get_seeds(seed_line: str):
    seed_numbers = re.findall(r"seeds: ((?:\d+\s?)+)", seed_line)[0]
    return string_array_to_array_of_int(seed_numbers)

def map_seeds_to_new_values(map_values, last_seeds):
    new_seeds = []
    
    for seed in last_seeds:
        new_seed = None
        for map_value in map_values:
            [destination_start, source_start, map_range] = map_value

            if seed in range(source_start, source_start + map_range):
                new_seed = destination_start + (seed - source_start)
                break
        new_seeds.append(new_seed if new_seed else seed)
    return new_seeds

def main():
    all_mapped_seeds = []
    # with open("../input.txt") as f:
    with open("../input_example.txt") as f:
        file_lines = f.readlines()
        all_mapped_seeds.append(get_seeds(file_lines[0]))
        map_values = []
        
        for [index, line] in enumerate(file_lines[2:]):
            map_description = re.fullmatch(r"\D+:\n", line)

            if map_description:
                continue
            if line == "\n":
                all_mapped_seeds.append(map_seeds_to_new_values(map_values, all_mapped_seeds[-1]))
                map_values = []
                continue
            
            map_values.append(string_array_to_array_of_int(line))

            # handle last line
            if index == (len(file_lines[2:]) - 1):
                all_mapped_seeds.append(map_seeds_to_new_values(map_values, all_mapped_seeds[-1]))
    
    print(all_mapped_seeds)
    return min(all_mapped_seeds[-1])

print(main())