import concurrent.futures

test_input_1 = [7,13,"x","x",59,"x",31,19] # OK
test_input_2 = [17,"x",13,19] # OK
test_input_3 = [67,7,59,61] # OK
test_input_4 = [67,"x",7,59,61] # OK
test_input_5 = [67,7,"x",59,61] # OK
test_input_6 = [1789,37,47,1889] # OK
bus_ids = [17, "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", 37, "x", "x", "x", "x", "x", 449, "x", "x", "x", "x", "x", "x", "x", 23, "x", "x", "x", "x", 13, "x", "x", "x", "x", "x", 19, "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", 607, "x", "x", "x", "x", "x", "x", "x", "x", "x", 41, "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", 29]

def calculate_delay(bus_ids):
    counter = 0
    list_with_delays = []

    for bus_id in bus_ids:
        if bus_id != "x":
            list_with_delays.append([bus_id, counter])
        counter += 1

    return list_with_delays

def find_earliest_timestamp(list_with_delays, step, offset):
    first_bus_timestamp = offset
    first_bus_timestamp_original = list_with_delays[0][0]

    # while True:
    for i in range(step):
        correct_timestamps_counter = 0
        # For every row different than first (reference)
        for row in list_with_delays[1:]:
            # Check if the current first number multiple + next bus's delay divides without a reminder
            if (first_bus_timestamp + row[1]) % row[0] == 0:
                correct_timestamps_counter += 1
            else:
                break
        # If amount of divisions without a reminder is equal to list of bus ids (without the first one - reference) 
        if correct_timestamps_counter == len(list_with_delays) - 1:
            return first_bus_timestamp
        # Else get the next multiple of the reference
        else:
            first_bus_timestamp += first_bus_timestamp_original

    return f"Not in set {offset} - {first_bus_timestamp}"

if __name__=="__main__":
    list_with_delays = calculate_delay(bus_ids)
    # step = 1000000000
    step = 1000000
    offsets =  [x*step*list_with_delays[0][0] for x in range(42657000, 42657019)]
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results =  [executor.submit(find_earliest_timestamp, list_with_delays, step, offset) for offset in offsets]
    
        for f in concurrent.futures.as_completed(results):
            print(f.result())