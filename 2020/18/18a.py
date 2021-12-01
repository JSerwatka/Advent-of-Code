def generate_new_equation(equation):
    new_equ = ""
    new_idx = 0
    for idx, element in enumerate(equation):
        if new_idx > idx:
            continue
        if element in ["*", "+", " "]:
            new_equ += element
        elif element.isnumeric():
            new_equ = "(" + new_equ + element + ")"
        elif element == "(":
            return_value = generate_new_equation(equation[idx+1:])
            new_idx = idx + return_value[1] + 2
            new_equ = "(" + new_equ + return_value[0] + ")"
        elif element == ")":
            return [new_equ, idx]
    return new_equ

def sum_all_equations():
    result = 0

    with open("input.txt") as f:
        for line in f:
            line = line.rstrip('\n')
            new_val = eval(generate_new_equation(line))
            result += new_val

    return result

print(sum_all_equations())