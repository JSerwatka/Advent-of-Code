import math
import numpy as np

arrival_time = 1006401
bus_ids = [17, 37, 449, 23, 13, 19, 607, 41, 29]

def generate_nearest_bus_list(arrival_time, bus_ids):
    nearest_list = []
    for bus_id in bus_ids:
        nearest_list.append([bus_id, math.ceil(arrival_time/bus_id) * bus_id])
        
    return nearest_list

def calculate_result(nearest_list, arrival_time):
    min_bus_time = min([row[1] for row in nearest_list])
    
    for row in nearest_list:
        if row[1] == min_bus_time:
            min_bus_id = row[0] 
            break

    return (min_bus_time - arrival_time) * min_bus_id

nearest_list = generate_nearest_bus_list(arrival_time, bus_ids)
result = calculate_result(nearest_list, arrival_time)
print(nearest_list)
print(result)