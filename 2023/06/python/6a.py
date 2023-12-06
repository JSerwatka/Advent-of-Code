from functools import reduce
import re


def get_numbers(line: str):
    return map(int, re.findall(r"\d+", line))

def main():
    with open("../input.txt") as f:
    # with open("../input_example.txt") as f:
        numbers_of_ways = []
        lines = f.readlines()
        time_numbers = get_numbers(lines[0])
        distance_numbers = get_numbers(lines[1])
        
        for time, distance in zip(time_numbers, distance_numbers):
            way_per_time = 0
            for test_time in range(1, time):
                speed = test_time
                time_left = time - test_time
                test_distance = speed * time_left
                
                if test_distance > distance:
                    way_per_time += 1
            numbers_of_ways.append(way_per_time)
    return reduce(lambda x, y: x*y, numbers_of_ways)

print(main())