def find_bags(all_bags=set(), current_bags=set(["shiny_gold"])):
    next_bags = set()

    if len(current_bags) == 0:
        return len(all_bags)

    f = open("input_clean_list_2.txt", "r")
    for line in f:
        bag_name = line.split(": ")[0]
        contain = [el.strip() for el in line.split(": ")[1].split(", ")]
        for bag in current_bags:
            if bag in contain:
                all_bags.add(bag_name)
                next_bags.add(bag_name)
    
    return find_bags(current_bags=next_bags, all_bags=all_bags)

print(find_bags())