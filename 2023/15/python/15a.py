def hash_alorithm(string: str):
    current_value = 0
    for char in string:
        ascii_value = ord(char)
        after_multiplication = (current_value + ascii_value) * 17
        current_value = after_multiplication % 256
    return current_value

def main():
    total = 0
    with open("../input.txt") as f:
    # with open("../input_example.txt") as f:
        steps = f.readlines()[0].split(",")
        for step in steps:
            total += hash_alorithm(step)
    return total

print(main())