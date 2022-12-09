from math import copysign

moves = {"R":(1,0), "U":(0,1), "L":(-1, 0), "D":(0,-1)}

def sign(a):
    if a == 0:
        return 0
    else:
        return copysign(1, a)

def process_commands(data, rope):
    tail_trail = {(0,0):1}
    
    for line in data:
        line = line.strip()
        command, distance = line.split(" ")
        distance = int(distance)
        
        for _ in range(distance):
            rope[0] = tuple(i+j for i,j in zip(rope[0], moves[command]))
            
            for idx in range(len(rope)-1):
                head, tail = rope[idx], rope[idx+1]
                
                if abs(head[0] - tail[0]) <= 1 and abs(head[1]-tail[1]) <= 1:
                    break
                
                tail = (tail[0] + sign(head[0] - tail[0]), tail[1] + sign(head[1] - tail[1]))
                rope[idx+1] = tail
                
            tail_trail[rope[-1]] = tail_trail.get(rope[-1], 0) + 1
            
    return [(int(x), int(y)) for x, y in list(tail_trail.keys())]

def solution1(data):
    return process_commands(data, [(0,0)]*2)

def solution2(data):
    return process_commands(data, [(0,0)] * 10)

if __name__ == "__main__":
    with open("../input.txt") as f:
        # print(solution1(f))
        print(solution2(f))