
from collections import defaultdict
import re

workflows = {}
parts = []
accepted = []

def process_workflows(workflow):
    workflow_name, workflow_logic = re.findall(r"^(.*){(.*)}$", workflow)[0]
    workflow_steps = workflow_logic.split(",")
    workflows[workflow_name] = workflow_steps

def process_parts(part):
    part_as_arr = part[1:-1].split(",")
    part_as_dict = {k: int(v) for k,v in (part_el.split("=") for part_el in part_as_arr)}
    parts.append(part_as_dict)
    
def sort_part(part=None, start_workflow = "in"):
    if start_workflow == "A":
        accepted.append(part)
        return    
    if start_workflow == "R":
        return
    
    current_workflow_steps = workflows[start_workflow]
    for name, rating in part.items():
        locals()[name] = rating
    for step in current_workflow_steps:
        step_splited = step.split(":")
        
        if len(step_splited) == 1:
            sort_part(part, step_splited[0])
        else:
            if eval(step_splited[0]):
                return sort_part(part, step_splited[1])
                
def get_part_value(part: dict):      
    return sum(part.values())

def main():
    with open("../input.txt") as f:
    # with open("../input_example.txt") as f:
        process_function = process_workflows
        for line in f:
            if line == "\n":
                process_function = process_parts
                continue
            process_function(line.strip()) 
    for part in parts:
        sort_part(part)
    
    return sum([get_part_value(part) for part in accepted])

print(main())