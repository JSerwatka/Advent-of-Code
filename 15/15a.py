# 15b uses much faster version

li = [2,15,0,9,1,20]

for _ in range(2020-len(li)):
    try:
        curr_number = li[-1]
        reversed_list = li[::-1]
        reversed_list_short = reversed_list[1:]
        recent_idx = len(li)-1-reversed_list.index(curr_number)
        before_recent_idx = len(li)-2-reversed_list_short.index(curr_number)
    except ValueError:
        li.append(0)
    else:
        li.append(recent_idx-before_recent_idx)

print(li[-1])

# Cleaner but slower version
# for _ in range(100000 - len(li)):
#     if li[-1] not in li[:-1]:
#         li.append(0)
#     else:
#         first_idx = -1
#         second_idx = -1
#         for i in reversed(range(len(li))):
#             if i == len(li)-1:
#                 first_idx = i
#             elif li[i] == li[-1]:
#                 second_idx = i
#                 li.append(first_idx-second_idx)
#                 break