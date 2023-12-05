import re

def string_array_to_array_of_int(string_array):
    return [*map(int, string_array.strip().split(" "))]

def get_seeds(seed_line: str):
    seed_numbers_str_arr = re.findall(r"seeds: ((?:\d+\s?)+)", seed_line)[0]
    seed_numbers = string_array_to_array_of_int(seed_numbers_str_arr)
    seed_numbers_grouped = list(zip(*[iter(seed_numbers)] * 2))
    seed_ranges = [range(range_start, range_start + range_len) for range_start, range_len in seed_numbers_grouped]
    
    return [x for seed_range in seed_ranges for x in seed_range]

def map_seeds_to_new_values(map_values, last_seeds):
    new_seeds = []
    
    for seed in last_seeds:
        new_seed = None
        for map_value in map_values:
            [destination_start, source_start, map_range] = map_value

            if seed in range(source_start, source_start + map_range):
                new_seed = destination_start + (seed - source_start)
                break
        new_seeds.append(new_seed if new_seed else seed)
    return new_seeds

def main():
    last_seed_numbers = []
    with open("../input.txt") as f:
    # with open("../input_example.txt") as f:
        file_lines = f.readlines()
        last_seed_numbers = get_seeds(file_lines[0])
        map_values = []
        
        for [index, line] in enumerate(file_lines[2:]):
            map_description = re.fullmatch(r"\D+:\n", line)

            if map_description:
                continue
            if line == "\n":
                last_seed_numbers = map_seeds_to_new_values(map_values, last_seed_numbers)
                map_values = []
                continue
            
            map_values.append(string_array_to_array_of_int(line))

            # handle last line
            rest_file_len = (len(file_lines[2:]) - 1)
            if index == rest_file_len:
                last_seed_numbers = map_seeds_to_new_values(map_values, last_seed_numbers)
            print("progress: ", round(index * 100 / rest_file_len), "%")
            
    return min(last_seed_numbers)

print(main())
# import sys
# import re
# from collections import defaultdict
# D = open(sys.argv[1]).read().strip()
# L = D.split('\n')

# parts = D.split('\n\n')
# seed, *others = parts
# seed = [int(x) for x in seed.split(':')[1].split()]

# class Function:
#   def __init__(self, S):
#     lines = S.split('\n')[1:] # throw away name
#     # dst src sz
#     self.tuples: list[tuple[int,int,int]] = [[int(x) for x in line.split()] for line in lines]
#     #print(self.tuples)
#   def apply_one(self, x: int) -> int:
#     for (dst, src, sz) in self.tuples:
#       if src<=x<src+sz:
#         return x+dst-src
#     return x

#   # list of [start, end) ranges
#   def apply_range(self, R):
#     A = []
#     for (dest, src, sz) in self.tuples:
#       src_end = src+sz
#       NR = []
#       while R:
#         # [st                                     ed)
#         #          [src       src_end]
#         # [BEFORE ][INTER            ][AFTER        )
#         (st,ed) = R.pop()
#         # (src,sz) might cut (st,ed)
#         before = (st,min(ed,src))
#         inter = (max(st, src), min(src_end, ed))
#         after = (max(src_end, st), ed)
#         if before[1]>before[0]:
#           NR.append(before)
#         if inter[1]>inter[0]:
#           A.append((inter[0]-src+dest, inter[1]-src+dest))
#         if after[1]>after[0]:
#           NR.append(after)
#       R = NR
#     return A+R

# Fs = [Function(s) for s in others]

# def f(R, o):
#   A = []
#   for line in o:
#     dest,src,sz = [int(x) for x in line.split()]
#     src_end = src+sz

# P1 = []
# for x in seed:
#   for z in Fs:
#     x = z.apply_one(x)
#   P1.append(x)
# print(min(P1))

# P2 = []
# pairs = list(zip(seed[::2], seed[1::2]))
# for st, sz in pairs:
#   # inclusive on the left, exclusive on the right
#   # e.g. [1,3) = [1,2]
#   # length of [a,b) = b-a
#   # [a,b) + [b,c) = [a,c)
#   R = [(st, st+sz)]
#   for x in Fs:
#     R = x.apply_range(R)
#   #print(len(R))
#   P2.append(min(R)[0])
# print(min(P2))