from itertools import groupby


class Ground:
    def __init__(self):
        self.current_position = (0,0)
        self.perimeter = set()
        
    def step(self, direction: str, step_size: int):
        move_by = None
        match direction:
            case "U":
                move_by = (0, -step_size)
            case "R":
                move_by = (step_size, 0)
            case "L":
                move_by = (-step_size, 0)
            case "D":
                move_by = (0, step_size)
            case _:
                raise ValueError
        new_position = (self.current_position[0] + move_by[0], self.current_position[1] + move_by[1])
        self._get_all_points_between(self.current_position, new_position)
        self.current_position = new_position
        
    def _get_all_points_between(self, start_point, end_point):
        smallest_x, largest_x = (start_point[0], end_point[0]) if start_point[0] < end_point[0] else (end_point[0], start_point[0])
        smallest_y, largest_y = (start_point[1], end_point[1]) if start_point[1] < end_point[1] else (end_point[1], start_point[1])
        
        for x in range(smallest_x, largest_x + 1):
            for y in range(smallest_y, largest_y + 1):
                self.perimeter.add((x,y))
    
    def _get_points_by_y(self):
        sorted_points = sorted(self.perimeter, key=lambda point: point[1])
        return groupby(sorted_points, lambda point: point[1])
    
    def print_area(self):
        
    
    def get_area(self):
        points_grouped_by_y = self._get_points_by_y()
        area_size = 0
        for y, points in points_grouped_by_y:
            x_points_list = [point[0] for point in points]
            # print(y, sorted(x_points_list))
            min_x = min(x_points_list)
            max_x = max(x_points_list)
            # print(abs(min_x - max_x))
            area_size += abs(min_x - max_x) + 1
            # print("------")
        return area_size
    # +size_by_y(self):
        
        

def main():
    with open("../input.txt") as f:
    # with open("../input_example.txt") as f:
        ground = Ground()
        for line in f:
            direction, step_size, color = line.split(" ")
            step_size = int(step_size)
            ground.step(direction, step_size)
        print(ground.get_area())
print(main())