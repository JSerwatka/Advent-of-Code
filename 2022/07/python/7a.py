from functools import reduce


class Node:
    def __init__(self, parent):
        self.values = {}
        self.children = {}
        self.parent = parent
        self.level = 0

    def __str__(self):
        folder_structure = "\\"
        tabs = self.level * 4 * " "
        folder_structure += f" - folder file size: {self.calculate_size()}\n"
        for file_name, file_size in self.values.items():
            folder_structure += f"{tabs}{file_name} ({file_size})\n"
        for folder_name, folder_node in self.children.items():
            folder_structure += f"{tabs}{folder_name}"
            folder_structure += str(folder_node)
        
        return folder_structure

    def calculate_size(self):
        sum_of_files_sizes = reduce(lambda x, y: int(x) + int(y), self.values.values())
        for child_folder in self.children.values():
            sum_of_files_sizes += int(child_folder.calculate_size())
        return sum_of_files_sizes
        
current_node = Node(None)
level = 1
root_ref = current_node
        
def handle_dir_change(destination):
    global current_node
    global level
    match destination:
        case "/":
            return
        case "..":
            level -= 1
            current_node = current_node.parent
            current_node.level = level
        case _:
            level += 1                
            current_node = current_node.children[destination]
            current_node.level = level

def handle_new_dir(dir_name):
    current_node.children.setdefault(dir_name, Node(current_node))

def handle_new_file(file_name, file_size):
    current_node.values.setdefault(file_name, file_size)
        
def command_parser(command):
    elements = command.strip().split(" ")

    if elements[0] == "$":
        elements = elements[1:]

    match elements[0]:
        case "ls":
            return
        case "cd":
            handle_dir_change(elements[1])
        case "dir":
            handle_new_dir(elements[1])
        case _:
            handle_new_file(elements[1], elements[0])


def main(input_file):
    with open(input_file) as f:
        for command in f:
            command_parser(command)

main("../input_test.txt")
print(root_ref)
# print(root_ref.calculate_size())