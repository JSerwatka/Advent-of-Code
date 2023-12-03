import re

digitsMap = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def find_calibration_values(line):
    keys = "|".join(digitsMap.keys())
    pattern = "(?=(\d|" + keys + "))"
    foundDigitis = re.findall(pattern, line)
    
    firstDigit = digitsMap.get(foundDigitis[0], foundDigitis[0])
    lastDigit = digitsMap.get(foundDigitis[-1], foundDigitis[-1])
    return int(firstDigit + lastDigit)

def main():
    total = 0
    with open("../input.txt") as f:
        for line in f:
            total += find_calibration_values(line)
    return total


print(main())
