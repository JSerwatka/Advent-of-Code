import re

limit_by_color = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def get_game_data(line):
    pattern = r"Game (\d+): (.*)"
    match = re.search(pattern, line)
    return [match.group(1), match.group(2)]
    
def check_if_game_possible(game_result):
    cubes = re.findall(r"(\d+) (red|green|blue)", game_result)
    for cube in cubes:
        [cube_count, cube_color] = cube
        if int(cube_count) > limit_by_color[cube_color]:
            return False

    return True

def main():
    total = 0
    
    with open("../input.txt") as f:
        for line in f:
            [game_id, game_result] = get_game_data(line)
            if check_if_game_possible(game_result):
                total += int(game_id)
    return total

print(main())