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
    
    def find_all_children_folders(self, folders={}):       
        for child_folder_name, child_folder in self.children.items():
            folder_size = int(child_folder.calculate_size())
            folders.setdefault(child_folder_name, folder_size)
            child_folder.find_all_children_folders(folders)
        return folders
    
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

def find_the_smallest_folder(free_space_needed, folder_sizes):
    folders_big_enough_sizes = [file_size for file_size in folder_sizes if file_size >= free_space_needed]
    folders_big_enough_sizes.sort()
    
    return folders_big_enough_sizes[0]
    

def main(input_file, folder_structure):
    with open(input_file) as f:
        for command in f:
            folder_structure.command_parser(command)
    
    used_space = folder_structure.root.calculate_size()
    unused_space = 70000000 - used_space
    free_space_needed = 30000000 - unused_space
    all_foldes = {"/": used_space, **folder_structure.root.find_all_children_folders()}

    return find_the_smallest_folder(free_space_needed, all_foldes.values())
    
    


folder_structure = FolderStructure()
print(main("../input.txt", folder_structure))


