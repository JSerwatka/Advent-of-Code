from functools import reduce
import re


def get_number(line: str):
    return int("".join(re.findall(r"\d+", line)))

def main():
    with open("../input.txt") as f:
    # with open("../input_example.txt") as f:
        number_of_ways = 0
        lines = f.readlines()
        race_time = get_number(lines[0])
        race_distance = get_number(lines[1])
        
        for test_time in range(1, race_time):
            speed = test_time
            time_left = race_time - test_time
            test_distance = speed * time_left
            
            if test_distance > race_distance:
                number_of_ways += 1
    return number_of_ways

print(main())