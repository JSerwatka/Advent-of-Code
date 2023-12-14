from typing import List


def get_line_value(numbers: List[int]):
    uniq_numbers = set(numbers)
    if len(uniq_numbers) == 1 and list(uniq_numbers)[0] == 0:
        return 0

    next_line = []
    for index in range(len(numbers)):
        try:
            difference = numbers[index + 1] - numbers[index]
            next_line.append(difference)
        except IndexError:
            history = get_line_value(next_line)
            history = numbers[-1] + history
            return history
        
def main():
    with open("../input.txt") as f:
    # with open("../input_example.txt") as f:
        total = 0
        for line in f:
            numbers = [*map(int, line.strip().split(" "))]
            history = get_line_value(numbers)
            total += history
    return total

print(main())