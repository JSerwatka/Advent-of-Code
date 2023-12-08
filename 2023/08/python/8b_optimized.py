from itertools import cycle
from collections import defaultdict
from math import lcm

def main():
    with open("../input.txt") as f:
    # with open("../input_example_b.txt") as f:
        network = {}
        directions = f.readline().strip()
        # new line
        f.readline()

        for line in f:
            node, children = line.split(" = ")
            children = children.strip()[1:-1].split(", ")
            network[node] = children
        
        A_starting_nodes = [node for node in network.keys() if node[-1] == "A"]
        
        found_Z = defaultdict(dict)

        for starting_node in A_starting_nodes:
            steps = 0
            current_node = starting_node
            for direction in cycle(directions):
                next_step_index = 0 if direction == "L" else 1
                next_step = network[current_node][next_step_index]
                if next_step[-1] == "Z":
                    # been there and moved to the same place = circles
                    if next_step in found_Z[starting_node] and found_Z[starting_node][next_step]["next_direction"] == next_step_index:
                        break
                    found_Z[starting_node][next_step] = { "steps": steps + 1, "next_direction": next_step_index }
                current_node = next_step
                steps += 1
                
        found_Z_values = found_Z.values()
        all_z_steps = []
        # after testing, I know that for every A_starting_node i get only one Z node before cycling
        if all([len(x) == 1 for x in found_Z_values]):
            for z in found_Z_values:
                first_key = list(z.keys())[0]
                all_z_steps.append(z[first_key]["steps"])
        else:
            raise NotImplementedError("multiple Z for single path not handled")
        
        return lcm(*all_z_steps)
        
print(main())