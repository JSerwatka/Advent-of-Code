class Node:
    def __init__(self, parent):
        self.values = {}
        self.children = {}
        self.parent = parent
        self.level = 0


class Tree:
    def __init__(self):
        self.root = Node(None)
        self.currentNode = self.root
    
    def __str__(self):
        traverseNode = self.root

        if traverseNode.parent is None:
            print("/")
        else:
            traverseNode(traverseNode)
            
    def traverse(self, currentNode):
        # Jeśli nie ma już dzieci - wypisz tylko pliki i idź wyżej
        if len(currentNode.children) == 0:
            [print(f"{file_name} (file, size: {file_size}" for file_name, file_size in currentNode.values.items())]
            self.traverse(currentNode.parent)
        # Jeśli ma dzieci - wypisz je i wejdź do następneg (jeśli index != 0 - nie wypisuje, jeśli index większy niż ilość dzieci, idź wyżej)
        else:
            [print(f"{file_name} (file, size: {file_size}" for file_name, file_size in currentNode.values.items())]
            [print(f"{dir_name} (dir)") for dir_name in currentNode.children.keys()]
        
        
        
file_tree = Tree()
        
        
def handle_dir_change(destination):
    match destination:
        case "/":
            return
        case "..":
            file_tree.currentNode = file_tree.currentNode.parent
            file_tree.currentNode.level -= 1
        case _:
            file_tree.currentNode = file_tree.currentNode.children[destination]
            file_tree.currentNode.level += 1                

def handle_new_dir(dir_name):
    file_tree.currentNode.children.setdefault(dir_name, Node(file_tree.currentNode))

def handle_new_file(file_name, file_size):
    file_tree.currentNode.values.setdefault(file_name, file_size)
        
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
print(file_tree)

