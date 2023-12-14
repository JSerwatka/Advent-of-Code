from itertools import combinations
import numpy as np

def find_empty_spaces(space):
    space_length = space.shape[1]

    empty_rows_indexes = []    
    empty_columns_indexes = []    
    for index in (range(space_length)):

        # expand column
        if np.all(space[:, index] == b"."):
            empty_columns_indexes.append(index)
            
        # expand row
        if np.all(space[index, :] == b"."):
            empty_rows_indexes.append(index)
    return (empty_rows_indexes, empty_columns_indexes)

def update_galaxy_position(empty_rows_indexes, empty_columns_indexes, galaxy_position, number_of_additional_space):
    row_offset = len([x for x in empty_rows_indexes if x < galaxy_position[0]]) * number_of_additional_space
    column_offset = len([y for y in empty_columns_indexes if y < galaxy_position[1]]) * number_of_additional_space
    return (galaxy_position[0] + row_offset, galaxy_position[1] + column_offset)

def main(space_multipier = 1000000):
    with open("../input.txt") as f:
    # with open("../input_example.txt") as f:
        space = np.array([list(line.strip()) for line in f], dtype="S1")
        galaxies_indexes = zip(*np.where(space == b"#"))
        
        galaxies_dict = { id: index for id, index in enumerate(galaxies_indexes)}
        galaxies_ids = galaxies_dict.keys()
        all_galaxy_pairs = combinations(galaxies_ids, 2)
        empty_rows_indexes, empty_columns_indexes = find_empty_spaces(space)

        for galaxy_id in galaxies_ids:
            galaxies_dict[galaxy_id] = update_galaxy_position(empty_rows_indexes, empty_columns_indexes, galaxies_dict[galaxy_id], space_multipier - 1)

        sum_of_paths = 0
        for galaxy_pair in all_galaxy_pairs:
            galaxy_point_1 = np.array(galaxies_dict[galaxy_pair[0]])
            galaxy_point_2 = np.array(galaxies_dict[galaxy_pair[1]])
            
            # manhatan distance
            sum_of_paths += np.abs(galaxy_point_1 - galaxy_point_2).sum() 
        
    return sum_of_paths

print(main())
