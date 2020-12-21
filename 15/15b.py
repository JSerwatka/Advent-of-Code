li = [2,15,0,9,1,20]

def list_to_dict(numbers):
    last_occure_dict = dict([])
    for idx, number in enumerate(numbers):
        last_occure_dict[number] = idx+1
    return [idx+1, last_occure_dict]


def find_nth_value(n, numbers):
    counter, last_occure_dict = list_to_dict(numbers)
    new_value = li[-1]

    for _ in range(n - len(numbers)):
        if new_value not in last_occure_dict:
            last_occure_dict[new_value] = counter
            new_value = 0
        else:
            last_occure = last_occure_dict[new_value]
            last_occure_dict[new_value] = counter
            new_value = counter - last_occure
        counter += 1
    return new_value

print(find_nth_value(30000000, li))