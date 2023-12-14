from itertools import combinations
import numpy as np


def expand_space(input_file: str):
    with open(f"../{input_file}.txt") as f:
        space = np.array([list(line.strip()) for line in f], dtype="S1")
        space_expanded = np.copy(space)
        space_length = space.shape[1]

        col_offset = 0
        row_offset = 0        
        for index in (range(space_length)):

            # expand column
            if np.all(space[:, index] == b"."):
                empty_col = list("." * space_expanded.shape[0])
                space_expanded = np.insert(space_expanded, index + col_offset, empty_col, axis=1)
                col_offset += 1
            # expand row
            if np.all(space[index, :] == b"."):
                empty_row = list("." * space_expanded.shape[1])
                space_expanded = np.insert(space_expanded, index + row_offset, empty_row, axis=0)
                row_offset += 1
    with open(f"../{input_file}_expanded.txt", "w") as f:
        for line in space_expanded:
            line_mapped = "".join([char.decode('UTF-8') for char in line])
            f.write(line_mapped + "\n")

def main():
    with open("../input_expanded.txt") as f:
        space = np.array([list(line.strip()) for line in f], dtype="S1")
        galaxies_indexes = zip(*np.where(space == b"#"))
        
        galaxies_dict = { id: index for id, index in enumerate(galaxies_indexes)}
        galaxies_ids = galaxies_dict.keys()
        all_galaxy_pairs = combinations(galaxies_ids, 2)
        
        sum_of_paths = 0
        for galaxy_pair in all_galaxy_pairs:
            galaxy_point_1 = np.array(galaxies_dict[galaxy_pair[0]])
            galaxy_point_2 = np.array(galaxies_dict[galaxy_pair[1]])
            
            # manhatan distance
            sum_of_paths += np.abs(galaxy_point_1 - galaxy_point_2).sum() 
        
    return sum_of_paths        

print(main())
