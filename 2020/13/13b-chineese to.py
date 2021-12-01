import os
from typing import Tuple, List

def parse_input(file_name: str) -> Tuple[int, List[int]]:
    with open(file_name) as f:
        time_of_departure = int(f.readline().strip())
        bus_ids = []
        for a, b_id in enumerate(f.readline().strip().split(',')):
            if not b_id == 'x':
                bus_ids.append((-1 * a, int(b_id)))
        return time_of_departure, bus_ids 

# Source of egcd and modinv
# https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

# With chinese remainder theorem
# https://math.stackexchange.com/questions/1108111/solving-modulus-equation-systems
def calculate_answer(time_of_departure: int, bus_ids: List[int]) -> int:
    mod_prod = 1
    for bus_id in bus_ids:
        mod_prod *= bus_id[1]

    a = 0
    for bus_id in bus_ids:
        ai, mi = bus_id
        Mi = int(mod_prod / mi)
        Mi_ = modinv(Mi, mi)
        a += ai*Mi*Mi_
    return a % mod_prod

if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, 'input.txt')
    time_of_departure, bus_ids = parse_input(file_path)
    answer = calculate_answer(time_of_departure, bus_ids)
    print(answer)