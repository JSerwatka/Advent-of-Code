import re
from functools import reduce

def get_game_data(line):
    pattern = r"Game (\d+): (.*)"
    match = re.search(pattern, line)
    return [match.group(1), match.group(2)]
    
def find_highest_cubes_in_game(game_result):
    max_value_by_color = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    
    cubes = re.findall(r"(\d+) (red|green|blue)", game_result)
    for cube in cubes:
        [cube_count, cube_color] = cube
        if int(cube_count) > max_value_by_color[cube_color]:
            max_value_by_color[cube_color] = int(cube_count)

    return reduce(lambda a,b: a*b, max_value_by_color.values())

def main():
    total = 0
    
    with open("../input.txt") as f:
        for line in f:
            [game_id, game_result] = get_game_data(line)
            total += find_highest_cubes_in_game(game_result)

    return total

print(main())