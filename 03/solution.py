import re
with open("input.txt") as f:
    total = 0
    for i, line in enumerate(f.readlines()):
        valid_muls=re.findall(r"mul\([0-9]*,[0-9]*\)", line)
        numbers = [list(map(int, re.findall(r"[0-9]*,[0-9]*", vn)[0].split(","))) for vn in valid_muls]
        resmul = sum(map(lambda x: x[0] * x[1], numbers))
        total += resmul
    print(total)

with open("input.txt") as f:
    total = 0
    for i, line in enumerate(f.readlines()):
        iters_dos = re.finditer(r"do\(\)", line)
        iters_donts = re.finditer(r"don't\(\)", line)
        iters_muls = re.finditer(r"mul\([0-9]*,[0-9]*\)", line)

        valid_starts = [0]
        for m in iters_dos:
            valid_starts.append(m.start(0))
        invalid_starts = []
        for m in iters_donts:
            invalid_starts.append(m.start(0))
        invalid_starts.append(len(line))
        # Compute valid ranges for muls
        iter_valid = 0
        iter_invalid = 0
        valid_ranges = []
        while True:
            if iter_valid >= len(valid_starts) or \
                    iter_invalid >= len(invalid_starts):
                break
            va = valid_starts[iter_valid]
            inva = invalid_starts[iter_invalid]
            if len(valid_ranges) > 0 and va < valid_ranges[-1][1]:
                iter_valid += 1
                continue
            if va >= inva:
                iter_invalid += 1
                continue
            if va < inva:
                new_valid_range = (va, inva)
                valid_ranges.append(new_valid_range)
                iter_valid += 1
                iter_invalid += 1
        print("Do's:", valid_starts)
        print("Dont's:", invalid_starts)
        print("Valid ranges are:", valid_ranges)
        row_res = 0
        for m in iters_muls:
            to_process = False
            for r in valid_ranges:
                if m.start(0) >= r[0] and m.start(0) < r[1]:
                    to_process = True
                    break
            if not to_process:
                # print("skipping mul at", m.start(0))
                continue
            numbers = list(map(int, re.findall(r"[0-9]*,[0-9]*", m.group())[0].split(",")))
            resmul = numbers[0] * numbers[1]
            row_res += resmul
        total += row_res

    print(total)

from re import findall

total1 = total2 = 0
enabled = True
data = open("input.txt").read()

for a, b, do, dont in findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", data):
    if do or dont:
        enabled = bool(do)
    else:
        x = int(a) * int(b)
        total1 += x
        total2 += x * enabled

print(total1, total2)
