from functools import reduce

def create_array_from_string(line):
    return [int(tree) for tree in line]


def get_paths(tree_ccords, array_length):
    row, column = tree_ccords

    return {
        "left": column,
        "top": row,
        "right": array_length - column - 1,
        "bottom": array_length - row - 1
    }


def get_scenic_score(tree_coords, paths, arr):
    tree_value = arr[tree_coords[0]][tree_coords[1]]
    scenic_scores = []

    for direction, steps in paths.items():
        scenic_score_for_direction = 0
        current_tree = tree_coords.copy()
        for _ in range(1, steps + 1):
            match direction:
                case "left":
                    current_tree[1] = current_tree[1] - 1
                case "top":
                    current_tree[0] = current_tree[0] - 1
                case "right":
                    current_tree[1] = current_tree[1] + 1
                case "bottom":
                    current_tree[0] = current_tree[0] + 1
            
            scenic_score_for_direction += 1
            # Found tree larger then starting tree
            if arr[current_tree[0]][current_tree[1]] >= tree_value:
                break

        scenic_scores.append(scenic_score_for_direction)

    return reduce((lambda x, y: x * y), scenic_scores)

def main(input_file):
    arr = []
    highest_scenic_score = 0
    with open(input_file) as f:
        for line in f:
            line = line.strip()
            arr.append(create_array_from_string(line))

    array_length = len(arr)

    # Go thorugh all non-edge trees
    for row in range(1, array_length - 1):
        for column in range(1, array_length - 1):
            tree_coords = [row, column]

            paths = get_paths(tree_coords, array_length)
            scenic_score = get_scenic_score(tree_coords, paths, arr)
            
            if scenic_score > highest_scenic_score:
                highest_scenic_score = scenic_score
    return highest_scenic_score


print(main("../input.txt"))