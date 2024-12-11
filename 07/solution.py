import re
from itertools import combinations_with_replacement
from functools import reduce
import operator
with open("input.txt") as f:
    lines = f.readlines()
    equations = []
    for line in lines:
        equation = list(map(int, re.findall(r"\d+", line)))
        equations.append(equation)

res1 = 0
operators = [lambda a, b: a + b, lambda a,b : a * b]
for equation in equations:
    eq_res = equation[0]
    eq_coeffs = equation[1:]
    all_ops = combinations_with_replacement(operators, len(eq_coeffs)-1)
    for ops in all_ops:
        ops_lst = list(ops)
        if reduce(lambda a, b: ops_lst.pop(0)(a, b), eq_coeffs) == eq_res:
            res1 += sum(eq_coeffs)
            break
print(res1)

