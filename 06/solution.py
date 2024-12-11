import copy
fin = open("input.txt")

world = []
start_position = (0, 0)
for line in fin.readlines():
    row = list(map(lambda x: 0 if x == '.' else 1 if x == '#' else 2, list(line.strip())))
    if 2 in row:
        start_row = len(world)
        start_col = next(filter(lambda x: x[1] == 2, enumerate(row)))[0]
        start_position = (start_row, start_col)
        print("Found starting position at row=", start_row, "col=", start_col)

    world.append(row)

cy, cx = start_position
h, w = len(world), len(world[0])
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
cdir = 0
world_cpy = copy.deepcopy(world)

visited_cells = 0
while True:
    if cy < 0 or cy >= h or cx < 0 or cx >= w:
        break
    if world[cy][cx] != 3:
        visited_cells += 1
        world[cy][cx] = 3
    # Move
    direction = directions[cdir % len(directions)]
    temp_cy = cy + direction[0]
    temp_cx = cx + direction[1]
    if world[temp_cy][temp_cx] == 1:
        cdir += 1
        continue
    else:
        cy = temp_cy
        cx = temp_cx
print(visited_cells)

possible_positions = 0
for obst_v in range(h):
    for obst_u in range(w):
        # Set obstacle
        world = copy.deepcopy(world_cpy)
        prev_cell = world[obst_v][obst_u]
        if prev_cell == 1 or prev_cell == 2:
            continue
        # Place obstacle
        world[obst_v][obst_u] = 1
        got_out = False
        print(f"\r{float((obst_v * w + obst_u)) / (h*w):.2f}", end="")
        cdir = 0
        cy, cx = start_position
        for iterations in range(10_000):
            if cy < 0 or cy >= h or cx < 0 or cx >= w:
                got_out = True
                break
        
            if world[cy][cx] != 3:
                visited_cells += 1
                world[cy][cx] = 3
            # Move
            direction = directions[cdir % len(directions)]
            temp_cy = cy + direction[0]
            temp_cx = cx + direction[1]
            if temp_cy >= 0 and temp_cy < h and temp_cx >= 0 and temp_cx < w:
                if world[temp_cy][temp_cx] == 1:
                    cdir += 1
                    continue
            cy = temp_cy
            cx = temp_cx
        if not got_out:
            possible_positions += 1
print("\n", possible_positions)







