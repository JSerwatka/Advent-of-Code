# joltage_ratings_test_1 = [1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19]
# joltage_ratings_test_2 = [0, 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31, 32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 48, 49, 52]

# input with padding zero at the end to compensate idx+1 out of range
joltage_ratings = [0, 1, 2, 5, 6, 9, 12, 13, 14, 15, 16, 19, 20, 21, 24, 25, 26, 27, 28, 31, 32, 35, 36, 37, 40, 41, 44, 45, 46, 47, 
                   48, 51, 52, 53, 54, 55, 58, 61, 62, 63, 64, 65, 68, 69, 70, 71, 72, 75, 76, 77, 78, 79, 82, 85, 86, 87, 88, 91, 92, 93, 96, 
                   97, 98, 99, 100, 103, 104, 105, 106, 107, 110, 111, 112, 113, 114, 117, 118, 119, 122, 123, 124, 125, 126, 129, 130, 131, 132, 133, 136, 137, 138, 139, 140, 143, 0]

def find_adapters_path(joltage_ratings):
    counter = 0
    one_difference_streak = []
    for idx in range(len(joltage_ratings) - 1):
        if joltage_ratings[idx + 1] - joltage_ratings[idx] == 1:
            counter += 1
        else:
            if counter > 1:
                one_difference_streak.append(counter + 1)
            counter = 0

    return one_difference_streak

# Fibonacci sequence? 
# 2 - x1  | +1
# 3 - x2  | +2
# 4 - x4  | +3
# 5 - x7  | +5
# 6 - x12 |

print(find_adapters_path(joltage_ratings))