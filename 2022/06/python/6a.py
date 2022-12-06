def find_first_marker(code, marker_size = 4):
    try:
        for index in range(len(code) - marker_size):
            potencial_marker = code[index : (index + marker_size)]
            if (len(potencial_marker) == len(set(potencial_marker))):
                return index + marker_size
    except IndexError:
        print("Out of range - check your code")

def main(input_file):
    with open(input_file) as f:
        stream = f.read() 
        marker_index = find_first_marker(stream)
    return marker_index
        
        
print(main("../input.txt"))