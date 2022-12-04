# accepts "x-y" range 
def generate_range_arrays(string_ranges):
    range_arrays = []
    for string_range in string_ranges:
        first, last = map(int, string_range.split("-"))
        range_arrays.append(list(range(first, last+1)))
    return range_arrays

def is_overlap(range_one, range_two):
    if len(set(range_one) & set(range_two)) > 0:
        return True
    return False

def main(input_path):
    amount_overlap = 0
    with open(input_path) as f:
        for line in f:
            range_arrays = generate_range_arrays(line.strip().split(","))
            if (is_overlap(*range_arrays)):
                amount_overlap += 1
    return amount_overlap

print(main("../input.txt"))