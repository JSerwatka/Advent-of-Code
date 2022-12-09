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
        sum_of_files_sizes = sum(int(x) for x in self.values.values())
        for child_folder in self.children.values():
            sum_of_files_sizes += int(child_folder.calculate_size())
        return sum_of_files_sizes
    
    def find_children_smaller_than(self, size, small_folders=[]):       
        for child_folder in self.children.values():
            folder_size = int(child_folder.calculate_size())
            if folder_size < size:
                small_folders.append(folder_size)
            child_folder.find_children_smaller_than(size, small_folders)
        return small_folders
    
class FolderStructure:
    def __init__(self):
        self.level = 1
        self.root = Node(None)
        self.current_node = self.root
        
    def handle_dir_change(self, destination):
        match destination:
            case "/":
                return
            case "..":
                self.level -= 1
                self.current_node = self.current_node.parent
                self.current_node.level = self.level
            case _:
                self.level += 1                
                self.current_node = self.current_node.children[destination]
                self.current_node.level = self.level
        
    def handle_new_dir(self, dir_name):
        self.current_node.children.setdefault(dir_name, Node(self.current_node))

    def handle_new_file(self, file_name, file_size):
        self.current_node.values.setdefault(file_name, file_size)
        
    def command_parser(self, command):
        elements = command.strip().split(" ")

        if elements[0] == "$":
            elements = elements[1:]

        match elements[0]:
            case "ls":
                return
            case "cd":
                self.handle_dir_change(elements[1])
            case "dir":
                self.handle_new_dir(elements[1])
            case _:
                self.handle_new_file(elements[1], elements[0])
                
    def __str__(self):
        return str(self.root)

def main(input_file, folder_structure):
    with open(input_file) as f:
        for command in f:
            folder_structure.command_parser(command)

folder_structure = FolderStructure()
main("../input_test.txt", folder_structure)
print(sum(folder_structure.root.find_children_smaller_than(100000)))