
def is_contained(range_one_string, range_two_string):
    arr_range = list(map(int, range_one_string.split("-")))
    arr_range_two = list(map(int, range_two_string.split("-")))
    
    if arr_range[0] >= arr_range_two[0] and arr_range[1] <= arr_range_two[1]:
        return True
    if arr_range[0] <= arr_range_two[0] and arr_range[1] >= arr_range_two[1]:
        return True
    return False
    
def main(input_path):
    amount_of_contained = 0
    with open(input_path) as f:
        for line in f:
            range_one_string, range_two_string =  line.strip().split(",")
            if (is_contained(range_one_string, range_two_string)):
                amount_of_contained += 1
    return amount_of_contained
            
print(main("../input.txt"))