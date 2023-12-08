from itertools import cycle

def main():
    with open("../input.txt") as f:
    # with open("../input_example_a2.txt") as f:
        network = {}
        directions = f.readline().strip()
        # new line
        f.readline()

        for line in f:
            node, children = line.split(" = ")
            children = children.strip()[1:-1].split(", ")
            network[node] = children
        
        current_node_children = network["AAA"]
        steps = 0
        
        
        for direction in cycle(directions):
            next_step = current_node_children[0 if direction == "L" else 1]
            
            if (next_step == "ZZZ"):
                return steps + 1
            else:
                current_node_children = network[next_step]
                steps += 1
    return steps
        
print(main())