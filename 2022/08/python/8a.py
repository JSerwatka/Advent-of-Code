def create_array_from_string(line):
    return [int(tree) for tree in line]


def sort_short_to_long_path(tree_ccords, array_length):
    row, column = tree_ccords

    paths = {
        "left": column,  # column
        "top": row,  # row
        "right": array_length - column - 1,
        "bottom": array_length - row - 1
    }
    return {k: v for k, v in sorted(paths.items(), key=lambda item: item[1])}


def check_if_tree_visible(tree_coords, paths_sorted, arr):
    tree_value = arr[tree_coords[0]][tree_coords[1]]

    for direction, steps in paths_sorted.items():
        current_tree = tree_coords.copy()
        for move in range(1, steps + 1):
            match direction:
                case "left":
                    current_tree[1] = current_tree[1] - 1
                case "top":
                    current_tree[0] = current_tree[0] - 1
                case "right":
                    current_tree[1] = current_tree[1] + 1
                case "bottom":
                    current_tree[0] = current_tree[0] + 1
            # Found tree larger then starting tree
            if arr[current_tree[0]][current_tree[1]] >= tree_value:
                break
            # Moved to the end - all trees smaller
            if move == steps:
                return True
    return False

            


def main(input_file):
    arr = []

    with open(input_file) as f:
        for line in f:
            line = line.strip()
            arr.append(create_array_from_string(line))

    array_length = len(arr)
    # Calculate edge trees
    visible_trees = array_length * 4 - 4

    # Go thorugh all non-edge trees
    for row in range(1, array_length - 1):
        for column in range(1, array_length - 1):
            tree_coords = [row, column]

            paths_sorted = sort_short_to_long_path(tree_coords, array_length)
            if check_if_tree_visible(tree_coords, paths_sorted, arr):
                visible_trees += 1
    return visible_trees


print(main("../input.txt"))