
from collections import defaultdict
import re
from pprint import pprint


def dfs(graph, start_node, end_node):
    stack = [(start_node, [start_node], [], [])]
    while stack:
        (node, path, conditions_path, negative_conditions_path) = stack.pop()
        for index, (next_node, condition) in enumerate(graph[node].items()):
            negative_conditions = list(graph[node].values())[:index]
            # prevent circular
            if next_node not in path:
                if next_node == end_node:
                    yield { "path": [*path, next_node], "conditions": [*conditions_path, condition], "negative_conditions": [*negative_conditions_path, *negative_conditions] }
                elif next_node == "R":
                    continue
                else:
                    stack.append((next_node, [*path, next_node], [*conditions_path, condition], [*negative_conditions_path, *negative_conditions] ))

def process_workflows(workflow, graph):
    workflow_name, workflow_logic = re.findall(r"^(.*){(.*)}$", workflow)[0]
    workflow_steps_splited = workflow_logic.split(",")
    
    # FIXME nie uwzględnia sytuacji gdy wiele warunkow doprowadza do jednego miejsca
    if workflow_name == "lnx":
        pass
    for step in workflow_steps_splited:
        step_splited = step.split(":")
        if len(step_splited) == 1:
            graph[workflow_name][step_splited[0]] = True
        else:
            graph[workflow_name][step_splited[1]] = step_splited[0]
    return graph

def get_combinations_from_condition(conditions, negative_conditions):
    combinations_per_letter = {}
    for letter in ["x", "m", "a", "s"]:
        combinations_per_letter[letter] = [0, 4001]
    
    for condition in conditions:
        if condition is True:
            continue
        letter, sign, value = condition[0], condition[1], condition[2: ]
        new_value = int(value)
        if sign == ">":
            current_value = combinations_per_letter[letter][0]
            combinations_per_letter[letter][0] = new_value if new_value > current_value else current_value
        else:
            current_value = combinations_per_letter[letter][1]
            combinations_per_letter[letter][1] = new_value if new_value < current_value else current_value
            
    for condition in negative_conditions:
        if condition is True:
            continue
        letter, sign, value = condition[0], condition[1], condition[2: ]
        sign = ">" if sign == "<" else "<"
        new_value = int(value)
        if sign == ">":
            current_value = combinations_per_letter[letter][0]
            combinations_per_letter[letter][0] = new_value if new_value > current_value else current_value
        else:
            current_value = combinations_per_letter[letter][1]
            combinations_per_letter[letter][1] = new_value if new_value < current_value else current_value
    print(combinations_per_letter)
    print("==============")
    
    total_path_combinations = 1
    for _, combinations in combinations_per_letter.items():
        total_path_combinations *= combinations[1] - combinations[0] - 1
    return total_path_combinations
    
        

def main():
    graph = defaultdict(dict)
    graph["A"], graph["R"] = {}, {}
    total = 0
    # with open("../input.txt") as f:
    with open("../input_example.txt") as f:
        for line in f:
            if line == "\n":
                break
            graph = process_workflows(line.strip(), graph)

    for path in dfs(graph, "in", "A"):
        print(path["path"])
        print(path["conditions"])
        print(path["negative_conditions"])
        total += get_combinations_from_condition(path["conditions"], path["negative_conditions"])
    return total

    
print(main())