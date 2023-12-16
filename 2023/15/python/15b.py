from collections import defaultdict, deque

label_to_box_map = {}
initialization_sequence = defaultdict(deque)
label_to_focal_length_map = {}

def hash_alorithm(string: str):
    current_value = 0
    for char in string:
        ascii_value = ord(char)
        after_multiplication = (current_value + ascii_value) * 17
        current_value = after_multiplication % 256
    return current_value

def get_step_elements(step:str):
    if "-" in step:
        return (step[:-1], "sub", None)
    else:
        label, focal_lenght = step.split("=")
        return (label, "add", focal_lenght)

def get_box_number(label: str):
    if label in label_to_box_map:
        return label_to_box_map[label]
    else:
        box_number = hash_alorithm(label)
        label_to_box_map[label] = box_number
        return box_number
    
def handle_operation(box_number, label, operation, focal_lenght):
    if operation == "sub":
        try:
            initialization_sequence[box_number].remove(label)
        except ValueError:
            pass
    else:
        if label_to_focal_length_map.get(label) is None:
            initialization_sequence[box_number].append(label)
    label_to_focal_length_map[label] = focal_lenght

def main():
    total = 0
    with open("../input.txt") as f:
    # with open("../input_example.txt") as f:
        steps = f.readlines()[0].split(",")
        for step in steps:
            label, operation, focal_lenght = get_step_elements(step)
            box_number = get_box_number(label)
            handle_operation(box_number, label, operation, focal_lenght)

    for box in initialization_sequence:
        for index, label in enumerate(initialization_sequence[box]):
            box_number = box + 1
            slot = index + 1
            focal_lenght = label_to_focal_length_map[label]
            total += box_number * slot * int(focal_lenght)
    return total

print(main())