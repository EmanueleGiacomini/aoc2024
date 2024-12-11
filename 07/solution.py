import re
with open("input.txt") as f:
    lines = f.readlines()
    equations = []
    for line in lines:
        equation = list(map(int, re.findall(r"\d+", line)))
        equations.append(equation)

res1 = 0
for equation in equations:
    eq_res = equation[0]
    eq_coeffs = equation[1:]
    print(eq_coeffs)
    exit(0)

