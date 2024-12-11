from pathlib import Path
from functools import reduce

def read_input(fin: Path):
    reports = []
    with open(fin, "r") as f:
        for line in f.readlines():
            reports.append(list(map(lambda x: int(x), line.split())))
    return reports

def solution_first_part(fin: Path):
    reports = read_input(fin)

    def is_valid(report):
        diff = list(map(lambda a, b : a - b, report[:-1], report[1:]))
        num_negative = len(list(filter((lambda a: a < 0), diff)))
        num_positive = len(list(filter((lambda a: a >= 0), diff)))
        absdiff = list(map(lambda a: abs(a), diff))
        num_exceede_max = len(list(filter(lambda x: x > 3, absdiff)))
        num_exceede_min = len(list(filter(lambda x: x < 1, absdiff)))
        num_exceede = num_exceede_max + num_exceede_min
        num_invalid_levels = len(diff) - max(num_negative, num_positive)
        num_invalid = num_invalid_levels + num_exceede
        print(diff, num_negative, num_positive, num_invalid_levels, num_exceede_max, num_exceede_min, num_exceede, num_invalid <= 1)
        return num_invalid <= 0 
    
    num_valid = len(list(filter(lambda re: is_valid(re), reports)))
    return num_valid

def solution_second_part(fin: Path):
    reports = read_input(fin)

    def is_valid(report):
        diff = list(map(lambda a, b : a - b, report[:-1], report[1:]))
        num_negative = len(list(filter((lambda a: a < 0), diff)))
        num_positive = len(list(filter((lambda a: a >= 0), diff)))
        absdiff = list(map(lambda a: abs(a), diff))
        num_exceede_max = len(list(filter(lambda x: x > 3, absdiff)))
        num_exceede_min = len(list(filter(lambda x: x < 1, absdiff)))
        num_exceede = num_exceede_max + num_exceede_min
        num_invalid_levels = len(diff) - max(num_negative, num_positive)
        num_invalid = num_invalid_levels + num_exceede
        return num_invalid == 0 
    
    num_valid = sum([any([is_valid(re[:i] + re[i+1:]) for i in range(len(re))]) for re in reports])
    return num_valid



if __name__ == "__main__":
    print("Solution half:", solution_first_part("input.txt"))
    print("Solution second half:", solution_second_part("input.txt"))
    
    exit(0)


