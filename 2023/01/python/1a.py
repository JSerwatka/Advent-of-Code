import re

def find_calibration_values(line):
    foundDigitis = re.findall("\d", line)
    return int(foundDigitis[0] + foundDigitis[-1])

def main():
    total = 0
    with open("../input.txt") as f:
        for line in f:
            total += find_calibration_values(line)
    return total

print(main())