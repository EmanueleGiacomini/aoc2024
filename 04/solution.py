

matrix = []
for line in open("input.txt").readlines():
    matrix.append(list(line.strip()))

h, w = len(matrix), len(matrix[0])

def search_xmas(start, dx, dy, state: int = 0):
    i, j = start
    if i < 0 or i >= h or j < 0 or j >= w:
        return False
    new_start = (i + dy, j + dx)

    if state == 0: # X
        if matrix[i][j] == "X":
            return search_xmas(new_start, dx, dy, state + 1)
        else:
            return False
    elif state == 1: # M
        if matrix[i][j] == "M":
            return search_xmas(new_start, dx, dy, state + 1)
        else:
            return False
    elif state == 2: # A
        if matrix[i][j] == "A":
            return search_xmas(new_start, dx, dy, state + 1)
        else:
            return False
    elif state == 3: # S
        if matrix[i][j] == "S":
            return True
        else:
            return False

directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
xmas_counter = 0
for i in range(h):
    for j in range(w):
        for dx, dy in directions:
            xmas_counter += 1 * search_xmas((i, j), dx, dy)
print("total xmas =", xmas_counter)
        

def search_mas(start):
    i, j = start
    if i < 1 or i >= (h - 1) or j < 1 or j >= (w - 1):
        return False

    if matrix[i][j] != "A":
        return False

    # -1, -1 | 0, -1 | 1, -1
    # -1,  0 | 0,  0 | 1,  0
    # -1,  1 | 0,  1 | 1,  1

    diag1 = [matrix[i-1][j-1], matrix[i][j], matrix[i+1][j+1]]
    diag2 = [matrix[i+1][j-1], matrix[i][j], matrix[i-1][j+1]]
    gt = ["M", "A", "S"]
    return True if (gt == diag1 or gt == diag1[::-1]) and (gt == diag2 or gt == diag2[::-1]) else False

mas_counter = 0
for i in range(h):
    for j in range(w):
        mas_counter += 1 * search_mas((i, j))
print("total X-mas=", mas_counter) 
