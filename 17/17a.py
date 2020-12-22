class Point:
    def __init__(self, x, y, z, state):
        self.x = x
        self.y = y
        self.z = z
        self.state = state
    
    def __str__(self):
        return(f"P({self.x}, {self.y}, {self.z}): {self.state}")

    def is_active(self):
        if self.state == "#":
            return True
        else:
            return False

    def activate_point(self):
        self.state = "#"

    def deactivate_point(self):
        self.state = "."
    
    def __generate_neighbor_window(self):
        neighbor_idxs = [] 
        for x in [-1,0,1]:
            for y in [-1,0,1]:
                for z in [1,0,1]:
                    if x == 0 and y == 0 and z == 0:
                        continue
                    neighbor_idxs.append([x,y,z])
        return neighbor_idxs
    
    def __generate_neighbor_points(self):
        neighbor_window = self.__generate_neighbor_window()
        neighbor_points = []

        for idx in neighbor_window:
            neighbor_points.append(
                [self.x + idx[0], self.y + idx[1], self.z + idx[2]]
            )
        return neighbor_points 

    def count_neighbors(self, other_list):
        neighbor_points = self.__generate_neighbor_points()
        neighbor_count = 0

        for other in other_list:
            if [other.x, other.y, other.z] in neighbor_points and other.state == "#":
                neighbor_count += 1
        return neighbor_count

    def apply_rules(self, other_list):
        neighbor_count = self.count_neighbors(other_list)

        if self.is_active() and neighbor_count not in [2, 3]:
            self.deactivate_point()
        elif (not self.is_active()) and neighbor_count == 3:
            self.activate_point()


# point = Point(1, 1, 0, ".")


arr_of_points = [
    Point(0, 0, 0, "#"),
    Point(1, 0, 0, "#"),
    Point(2, 0, 0, "#"),
    Point(0, 1, 0, "."),
    Point(1, 1, 0, "."),
    Point(2, 1, 0, "#"),
    Point(0, 2, 0, "."),
    Point(1, 2, 0, "#"),
    Point(2, 2, 0, ".")
]

my_point = arr_of_points.pop(3)
print(my_point.is_active())
my_point.activate_point()
print(my_point.is_active())

# print(my_point.count_neighbors(arr_of_points))