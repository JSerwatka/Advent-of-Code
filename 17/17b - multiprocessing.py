import copy
import itertools
import concurrent.futures

class Point:
    def __init__(self, x, y, z, w, state):
        self.x = x
        self.y = y
        self.z = z
        self.w = w
        self.state = state
    
    def __str__(self):
        return(f"P({self.x}, {self.y}, {self.z}, {self.w}): {self.state}")

    def __eq__(self, other): 
        if not isinstance(other, Point):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.x == other.x and self.y == other.y and self.z == other.z and self.w == other.w

    def is_active(self):
        if self.state == "#":
            return True
        else:
            return False

    def __activate_point(self):
        self.state = "#"

    def __deactivate_point(self):
        self.state = "."
        
    def __generate_neighbor_points(self):
        neighbor_points = []

        for idx in itertools.product([-1,0,1], repeat=4):
            if idx[0] == 0 and idx[1] == 0 and idx[2] == 0 and idx[3] == 0:
                continue
            neighbor_points.append(
                [self.x + idx[0], self.y + idx[1], self.z + idx[2], self.w + idx[3]]
            )
        return neighbor_points 

    def __count_neighbors(self, other_list):
        neighbor_points = self.__generate_neighbor_points()
        neighbor_count = 0

        for other in other_list:
            if [other.x, other.y, other.z, other.w] in neighbor_points and other.state == "#":
                neighbor_count += 1
        return neighbor_count

    def apply_rules(self, other_list):
        neighbor_count = self.__count_neighbors(other_list)

        if self.is_active() and neighbor_count not in [2, 3]:
            self.__deactivate_point()
        elif (not self.is_active()) and neighbor_count == 3:
            self.__activate_point()

def generate_points_from_input():
    points = []

    with open("input.txt") as f:
        read_data = []
        for line in f:
            read_data.append(line.rstrip('\n'))

    for y, line in enumerate(read_data):
        for x, state in enumerate(line):
            points.append(Point(x=x, y=(len(read_data)-1)-y, z=0, w=0, state=state))

    return points

def generate_new_cube(list_of_points):
    x_list = [point.x for point in list_of_points]
    z_list = [point.z for point in list_of_points]
    min_cube_xy = min(x_list) - 1
    max_cube_xy = max(x_list) + 1
    min_cube_zw = min(z_list) - 1
    max_cube_zw = max(z_list) + 1

    list_of_new_points = []

    for x in range(min_cube_xy, max_cube_xy+1):
        for y in range(min_cube_xy, max_cube_xy+1):
            for z in range(min_cube_zw, max_cube_zw+1):
                for w in range(min_cube_zw, max_cube_zw+1):
                    new_point = Point(x, y, z, w, ".")
                    if new_point not in list_of_points:
                        list_of_new_points.append(new_point)
    return list_of_points + list_of_new_points

def alter_points(cube, ranges):
    new_list_of_points = []
    for i in range(ranges[0], ranges[1]):
        new_point = cube.pop(i)
        old_point = copy.deepcopy(new_point)
        new_point.apply_rules(cube)
        new_list_of_points.append(new_point)
        cube.insert(i, old_point)
    return new_list_of_points

def cube_after_n_cycles(n, list_of_points):
    nb_of_cores = 8-1
    new_list_of_points = list_of_points
    for i in range(n):
        new_cube = generate_new_cube(new_list_of_points)
        new_list_of_points = []
        cube_len = len(new_cube)
        nb_of_ranges = cube_len//nb_of_cores
        ranges_min = [x for x in range(0, cube_len, nb_of_ranges)]
        ranges_max = [y for y in range(nb_of_ranges, cube_len, nb_of_ranges)]
        ranges_max.append(cube_len)
        with concurrent.futures.ProcessPoolExecutor() as executor:
            ranges = list(zip(ranges_min, ranges_max))
            results = executor.map(alter_points, itertools.repeat(new_cube), ranges)

            for result in results:
                new_list_of_points += result
    return new_list_of_points


def calculate_active(list_of_points):
    counter = 0
    for point in list_of_points:
        if point.is_active():
            counter += 1
    return counter


if __name__ == "__main__":
    list_of_points = generate_points_from_input()
    new_cube = cube_after_n_cycles(6, list_of_points)
    print(calculate_active(new_cube))
