def parse(equation):
    for i in range(len(equation) - 1):
        if equation[i] == '=' and equation[i + 1] == '=':
            equation = equation[:i] + equation[i + 1:]
    for i in range(len(equation) - 1):
        if equation[i].isalpha() and equation[i + 1].isdigit():
            equation = equation[:i + 1] + '^' + equation[i + 1:]
    return equation


print(parse('a3+3b+==aa'))