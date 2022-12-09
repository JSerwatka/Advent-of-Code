class Rope:
    def __init__(self):
        self.head = [0, 0]
        self.tail = [0, 0]
        self.visited_places = set([(0, 0)])

    def adjust_tail(self):
        def move_towards_zero(value):
            if value > 0:
                return value - 1
            return value + 1
        
        x_steps_needed = self.head[0] - self.tail[0]
        y_steps_needed = self.head[1] - self.tail[1]
        
        # Do not need adjustment
        if abs(x_steps_needed) <= 1 and abs(y_steps_needed) <= 1:
            return
        
        if abs(x_steps_needed) > abs(y_steps_needed):
            x_steps_needed = move_towards_zero(x_steps_needed)
        else:
            y_steps_needed = move_towards_zero(y_steps_needed)
            
        self.tail[0] += x_steps_needed
        self.tail[1] += y_steps_needed

        self.visited_places.add(tuple(self.tail))    
    
    def move_head(self, direction):
        match direction:
            case "L":
                self.head[0] = self.head[0] - 1
            case "U":
                self.head[1] = self.head[1] + 1
            case "R":
                self.head[0] = self.head[0] + 1
            case "D":
                self.head[1] = self.head[1] - 1
        
        self.adjust_tail()


def handle_command(command, rope):
    direction, steps = command.split(" ")
    for _ in range(int(steps)):
        rope.move_head(direction)

def main(file_path, rope):
    with open(file_path) as f:
        for command in f:
            handle_command(command.strip(), rope)
    return rope.visited_places
            
rope = Rope()          
print(len(main("../input.txt", rope)))

