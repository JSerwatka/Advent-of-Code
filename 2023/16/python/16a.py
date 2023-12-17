import numpy as np

beams = {}
energized_places = set()

class Beam:
    directions = {
        "top": (0, -1),
        "right": (1, 0),
        "bottom": (0, 1),
        "left": (-1, 0),
    }
    debug = True

    @classmethod
    def set_space_and_boundary(cls, space, boundary):
        cls.space = space
        cls.space_result = np.copy(space)
        cls.boundary = boundary
    
    def __init__(self, x, y, direction):
        # to prevent beams we already now route of
        self.beam_hash = f"{x}_{y}_{direction}"
        if self.beam_hash in beams:
            return

        self.x = x
        self.y = y
        self.direction = direction

        if self._is_in_boundaries():
            self._energize()
            beams[self.beam_hash] = self
            self._test_position()

    def __repr__(self):
        return self.beam_hash

    def _is_in_boundaries(self):
        return 0 <= self.x < Beam.boundary and 0 <= self.y < Beam.boundary

    def _energize(self):
        if (Beam.debug):
            Beam.space_result[self.y][self.x] = b"#"
        energized_places.add(self.x * 10 + self.y)
        
    def _remove_current_beam(self):
        del beams[self.beam_hash]

    def _test_position(self):
        if self.direction == "right":
            if Beam.space[self.y][self.x] == b"/":
                self.direction = "top"
                return True
            elif Beam.space[self.y][self.x] == b"\\":
                self.direction = "bottom"
                return True
            elif Beam.space[self.y][self.x] == b"|":
                # self._remove_current_beam()
                dx_top, dy_top = Beam.directions["top"]
                dx_bottom, dy_bottom = Beam.directions["bottom"]
                Beam(self.x + dx_top, self.y + dy_top, "top")
                Beam(self.x + dx_bottom, self.y + dy_bottom, "bottom")
                return False
            return True

        elif self.direction == "left":
            if Beam.space[self.y][self.x] == b"/":
                self.direction = "bottom"
                return True
            elif Beam.space[self.y][self.x] == b"\\":
                self.direction = "top"
                return True
            elif Beam.space[self.y][self.x] == b"|":
                # self._remove_current_beam()
                dx_top, dy_top = Beam.directions["top"]
                dx_bottom, dy_bottom = Beam.directions["bottom"]
                Beam(self.x + dx_top, self.y + dy_top, "top")
                Beam(self.x + dx_bottom, self.y + dy_bottom, "bottom")
                return False
            return True

        elif self.direction in ["top", "bottom"] and Beam.space[self.y][self.x] == b"-":
            # self._remove_current_beam()
            dx_left, dy_left = Beam.directions["left"]
            dx_right, dy_right = Beam.directions["right"]
            Beam(self.x + dx_left, self.y + dy_left, "left")
            Beam(self.x + dx_right, self.y + dy_right, "right")
            return False

        return True

    def step(self):
        dx, dy = Beam.directions[self.direction]
        self.x += dx
        self.y += dy

        if self._is_in_boundaries():
            self._energize()
            return self._test_position()
        else:
            # beams.remove(self)
            return False

def main():
    # with open("../input.txt") as f:
    with open("../input_example.txt") as f:
        space = np.array([list(line.strip()) for line in f], dtype="S1")
        Beam.set_space_and_boundary(space, space.shape[0])
        first_beam = Beam(0, 0, "right")
        while beams:
                _, beam = beams.popitem()
                while beam.step():
                    pass
        print(energized_places)
        
        if Beam.debug:
            for line in Beam.space_result:
                print(line.tobytes().decode())

        return len(energized_places)
        # move one beam 
        # if it is out of boundries -> move to next beam

print(main())
