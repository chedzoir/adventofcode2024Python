from adventofcode import load_content
from grid import create_grid, add_coor, turn_left, print_grid, turn_right, in_grid, set_cell, get_cell

content = load_content(6)

testData = [
"....#.....",
".........#",
"..........",
"..#.......",
".......#..",
"..........",
".#..^.....",
"........#.",
"#.........",
"......#..."
]

def walk_grid(grid):
    start_x =0
    start_y = 0
    for idx, row in enumerate(grid):
        if "^" in row:
            start_y = idx
            start_x = row.index("^")

    direction = (0,-1)
    cur_loc = (start_x, start_y)
    done = False
    loop = False

    visited = {}
    while not done and not loop:

        if cur_loc not in visited:
            visited[cur_loc] = []

        if direction in visited[cur_loc]:
            loop = True
        else:
            visited[cur_loc].append(direction)

        set_cell(grid, cur_loc, 'X')
     

        new_loc = add_coor(cur_loc, direction)
        if not in_grid(grid, new_loc):
            done = True
        elif get_cell(grid, new_loc) == '#' or get_cell(grid, new_loc) == 'O':
            direction = turn_right(direction)
        else:
            cur_loc = new_loc
        

    visted_count = sum([len([ r for r in row if r == 'X']) for row in grid])
    return visted_count, visited.keys(), loop, ( start_x, start_y)

def part1(rows):

    grid = create_grid(rows)

    # print_grid(grid)

    visted_count, visited, loop, start = walk_grid(grid)

    return visted_count

def part2(rows):
    grid = create_grid(rows)

    # print_grid(grid)

    loop_count = 0
    _count, visited, loop, start = walk_grid(grid)

    for loc in visited:
        if loc == start:
            continue

        grid = create_grid(rows)
        set_cell(grid, loc, 'O')

        _count, _visited, loop, _start = walk_grid(grid)

        if loop:
            loop_count += 1

    return loop_count

print("Part 1")
print(f"Test : {part1(testData)}")
print(f"Actual : {part1(content)}")

print("Part 2")
print(f"Test : {part2(testData)} ")
print(f"Actual : {part2(content)} ")
