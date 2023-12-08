from itertools import cycle

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
        current_nodes_children = [network[node] for node in A_starting_nodes]
        steps = 0
        
        for direction in cycle(directions):
            next_step_index = 0 if direction == "L" else 1
            next_steps = [children[next_step_index] for children in current_nodes_children]
            
            if all([next_step[-1] == "Z" for next_step in next_steps]):
                return steps + 1
            else:
                current_nodes_children = [network[node] for node in next_steps]
                steps += 1
    return steps
        
print(main())