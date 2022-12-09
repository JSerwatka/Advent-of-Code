class Rope:
    def __init__(self):
        self.knots = [[0, 0] for _ in range(10)]
        self.visited_places = set([(0, 0)])

    def adjust_tail(self):
        def move_towards_zero(value):
            if value > 0:
                return value - 1
            if value < 0:
                return value + 1
            return 0

        for index in range(1, len(self.knots)):           
            x_steps_needed = self.knots[index - 1][0] - self.knots[index][0]
            y_steps_needed = self.knots[index - 1][1] - self.knots[index][1]
                    
            # Do not need adjustment
            if abs(x_steps_needed) <= 1 and abs(y_steps_needed) <= 1:
                return

            if abs(x_steps_needed) > abs(y_steps_needed):
                x_steps_needed = move_towards_zero(x_steps_needed)
            elif abs(x_steps_needed) < abs(y_steps_needed):
                y_steps_needed = move_towards_zero(y_steps_needed)
            else:
                x_steps_needed =  move_towards_zero(x_steps_needed)
                y_steps_needed = move_towards_zero(y_steps_needed)
            
            self.knots[index][0] += x_steps_needed
            self.knots[index][1] += y_steps_needed
            
            # Save last knot
            if index == (len(self.knots) - 1):
                self.visited_places.add(tuple(self.knots[-1]))  

         
    
    def move_head(self, direction):
        head = self.knots[0]
        
        match direction:
            case "L":
                head[0] = head[0] - 1
            case "U":
                head[1] = head[1] + 1
            case "R":
                head[0] = head[0] + 1
            case "D":
                head[1] = head[1] - 1
        
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

