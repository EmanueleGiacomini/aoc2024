import re

fin = open("input.txt")

pattern1 = re.compile(r"\d|\d\n")

temp_rules = []
max_page = 0
while True:
    line = fin.readline()
    if pattern1.match(line):
        n1, n2 = list(map(int, re.findall(r"\d+|\d+\n", line)))
        max_page = max(max_page, max(n1, n2))
        temp_rules.append((n1, n2))
    else:
        break
print(f"Read {len(temp_rules)} rules.") 
rule_lut = [[0 for i in range(max_page+1)] for j in range(max_page+1)]
for n1, n2 in temp_rules:
    rule_lut[n1][n2] = 1
    # Penalize inverse rule
    rule_lut[n2][n1] = -1
res0 = 0
incorrect_updates = []
while True:
    line = fin.readline()
    if len(line) <= 1:
        break
    update = list(map(int, line.strip().split(",")))
    not_good = False
    for i in range(len(update)):
        for j in range(i, len(update)):
           n1, n2 = update[i], update[j]
           if rule_lut[n1][n2] < 0:
               not_good = True
               break
        if not_good:
            break
    if not_good:
        incorrect_updates.append(update)
        continue
    res0 += update[(len(update) - 1) // 2]

print(res0)

res1 = 0
for update in incorrect_updates:
    is_bag = True
    while True:
        has_issues = False
        for i in range(len(update)):
            for j in range(i, len(update)):
                n1, n2 = update[i], update[j]
                if rule_lut[n1][n2] < 0:
                    has_issues = True
                    temp = n2
                    update[j] = n1
                    update[i] = temp
        if not has_issues:
            break
    res1 += update[(len(update) - 1) // 2]
print(res1)


