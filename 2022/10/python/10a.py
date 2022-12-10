from functools import reduce


def handle_command(state, command, value=None):
    def handle_single_strength_cycle(cycle):
        if cycle in state["signal_strengths_cycles"]:
            state["signal_strengths"].append((cycle, cycle * state["value"]))
    
    handle_single_strength_cycle(state["cycle"])
    
    if command == "noop":
        state["cycle"] += 1
        return
    
    handle_single_strength_cycle(state["cycle"] + 1)

    state["value"] += int(value)
    state["cycle"] += 2
    

def main(input_file):
    state = {
        "cycle": 1,
        "value": 1,
        "signal_strengths_cycles": [20, 60, 100, 140, 180, 220],
        "signal_strengths": []
    }

    with open(input_file) as f:
        for command in f:
            handle_command(state, *command.strip().split(" "))
    return reduce(lambda x, y: x + y, [x[1] for x in state["signal_strengths"]])   

print(main("../input_test.txt"))