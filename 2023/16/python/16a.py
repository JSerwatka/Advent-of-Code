import numpy as np

beams = []
energized_places = set()

# don't create beam if it is already in beams or in past beams with the same starting point and direction

class Beam:
    directions = {
        "top": (0, -1),
        "right": (1, 0),
        "bottom": (0, 1),
        "left": (-1, 0),
    }
    space = None
    boundary = None

    @classmethod
    def set_space_and_boundary(cls, space, boundary):
        cls.space = space
        cls.boundary = boundary
    
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

        if self._is_in_boundaries():
            self._energize()
            beams.append(self)
            self._test_position()

    def _is_in_boundaries(self):
        return 0 <= self.x < Beam.boundary and 0 <= self.y < Beam.boundary

    def _energize(self):
        energized_places.add(self.x * 10 + self.y)

    def _test_position(self):
        if self.direction == "right":
            if Beam.space[self.y][self.x] == b"/":
                self.direction = "top"
                return True
            elif Beam.space[self.y][self.x] == b"\\":
                self.direction = "bottom"
                return True
            elif Beam.space[self.y][self.x] == b"|":
                beams.remove(self)
                dx_top, dy_top = Beam.directions["top"]
                dx_bottom, dy_bottom = Beam.directions["bottom"]
                Beam(self.x + dx_top, self.y + dy_top, "top")
                Beam(self.x + dx_bottom, self.y + dy_bottom, "bottom")
                return False

        elif self.direction == "left":
            if Beam.space[self.y][self.x] == b"/":
                self.direction = "bottom"
                return True
            elif Beam.space[self.y][self.x] == b"\\":
                self.direction = "top"
                return True
            elif Beam.space[self.y][self.x] == b"|":
                beams.remove(self)
                dx_top, dy_top = Beam.directions["top"]
                dx_bottom, dy_bottom = Beam.directions["bottom"]
                Beam(self.x + dx_top, self.y + dy_top, "top")
                Beam(self.x + dx_bottom, self.y + dy_bottom, "bottom")
                return False

        elif self.direction in ["top", "bottom"] and Beam.space[self.y][self.x] == b"-":
            beams.remove(self)
            Beam(self.x - 1, self.y, "left")
            Beam(self.x + 1, self.y, "right")
            return False

    def step(self):
        dx, dy = Beam.directions[self.direction]
        self.x += dx
        self.y += dy

        if self._is_in_boundaries():
            self._energize()
            return self._test_position()
        else:
            beams.remove(self)
            return False

def main():
    # with open("../input.txt") as f:
    with open("../input_example.txt") as f:
        space = np.array([list(line.strip()) for line in f], dtype="S1")
        Beam.set_space_and_boundary(space, space.shape[0])
        first_beam = Beam(0, 0, "right")
        while first_beam.step():
            pass
        
        # move one beam 
        # if it is out of boundries -> move to next beam

print(main())
