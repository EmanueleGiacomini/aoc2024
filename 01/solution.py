from pathlib import Path
from typing import List
from functools import reduce

def read_input(fin: Path):
    list_a, list_b = [], []
    with open(fin, 'r') as f:
        for l in f.readlines():
            num_a, num_b = l.strip().split()
            list_a.append(int(num_a))
            list_b.append(int(num_b))
    return sorted(list_a), sorted(list_b)

def solve_first_half(fin: Path):
    list_a, list_b = read_input(fin)
    return sum(map(lambda x, y : abs(x - y), list_a, list_b ))

def solve_second_half(fin:Path):
    list_a, list_b = read_input(fin)
    common_map = map(lambda to_filter: (to_filter, len(list(filter(lambda x : x == to_filter, list_b)))), list_a)
    similarity_score = sum(map(lambda x: x[0] * x[1], common_map))
    print(len(list_a), len(list_b))
    print(similarity_score)
    return similarity_score

if __name__ == "__main__":
    input_filename = "input.txt"
    print("First half solution =", solve_first_half(input_filename))
    print("Second half solution =", solve_second_half(input_filename))

    exit(0)
