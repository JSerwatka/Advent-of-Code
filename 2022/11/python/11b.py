from input import *
from math import lcm

class Monkey:
    def __init__(self, hold_items, operation, test_number, true_destination, false_destination):
        self.hold_items = hold_items
        self.amount_of_inspections = 0
        self.test_number = test_number
        self.true_destination = true_destination
        self.false_destination = false_destination
        self.operation = operation
        
    def run_turn(self, my_lcm):
        items_by_monkey = []
        for item in self.hold_items:
            item = self.operation(item)
            item %= my_lcm
            if item % self.test_number == 0:
                items_by_monkey.append((self.true_destination, item, self.test_number))
            else:
                items_by_monkey.append((self.false_destination, item))
            self.amount_of_inspections += 1

        self.hold_items = []
        return items_by_monkey

    def __str__(self):
        items_as_string = " ".join(map(str, self.hold_items))
        tab = 4 * " "
        ouput_string = "Monkey:\n"
        ouput_string += f"{tab}Items: {items_as_string}\n"
        ouput_string += f"{tab}Amount of inspections: {self.amount_of_inspections}\n"
        
        return ouput_string
    
    def __repr__(self):
        return self.__str__()


def caluclate_monkey_bussiness(monkeys):
    inspection_amounts = []
    for monkey in monkeys:
        inspection_amounts.append(monkey.amount_of_inspections)
        
    inspection_amounts.sort(reverse=True)
    return inspection_amounts[0] * inspection_amounts[1]
        
def main(monkeys_logic, amount_of_rounds):
    monkeys_dict = {}
    for monkey_number, monkey_logic in enumerate(monkeys_logic):
        monkeys_dict[monkey_number] = Monkey(monkey_logic["starting_items"], monkey_logic["operation"], monkey_logic["test_number"], monkey_logic["true_destination"], monkey_logic["false_destination"])
    
    # We don't care about the exact value but if it is divisable by test_numbers
    my_lcm = lcm(*[monkey.test_number for monkey in monkeys_dict.values()])
    for _ in range(amount_of_rounds):
        for current_monkey in monkeys_dict.values():
            items_to_throw = current_monkey.run_turn(my_lcm)
            
            for item_to_throw in items_to_throw:
                monkeys_dict[item_to_throw[0]].hold_items.append(item_to_throw[1])

    for monkey in monkeys_dict.values():
        print(monkey)
    print(caluclate_monkey_bussiness(monkeys_dict.values()))

main(monkeys, 10000)