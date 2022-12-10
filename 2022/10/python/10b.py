LINE_BREAK_INDEXES = [40, 80, 120, 160, 200, 240]

def handle_command(state, command, value=None):
    def draw_on_CRT():
        # reset index if the end of line
        if state["index"] in LINE_BREAK_INDEXES:
            state["index"] = 0
        # check if the current index in the sprite's reach
        if (state["index"]) in range(state["sprite_start_position"], state["sprite_start_position"] + 3):
            state["CRT"] += "#"
        else:
            state["CRT"] += "."
        
        state["cycle"] += 1
        state["index"] += 1
     
    if command == "noop":
        draw_on_CRT()
        return
    
    for _ in range(2):
        draw_on_CRT()
        
    state["sprite_start_position"] += int(value)
    
def print_pixels_for_CRT(pixels):
    # adding 0 at the start for easier calculations
    helper_indexes_copy = [0, *LINE_BREAK_INDEXES]
    
    for idx in range(1, len(helper_indexes_copy)):
        print(pixels[helper_indexes_copy[idx - 1] : helper_indexes_copy[idx]])


def main(input_file):
    state = {
        "cycle": 1,
        "index": 0,
        "sprite_start_position": 0,
        "CRT": ""
    }

    with open(input_file) as f:
        for command in f:
            handle_command(state, *command.strip().split(" "))
        print_pixels_for_CRT(state["CRT"])

main("../input.txt")