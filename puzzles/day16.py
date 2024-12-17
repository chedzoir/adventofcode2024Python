from adventofcode import load_content
from grid import create_grid, print_grid, arrow_directions, add_coor, turn_left, turn_right, get_cell, opposite

content = load_content(16)

testData = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############""".split('\n')


testData2 = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################""".split('\n')


def find_dir(direction):
    for v in arrow_directions.items():
        if v[1] == direction:
            return v[0]

def update_visited(visited, coor, direction, score, next_locs, end_loc):
    dir_str = find_dir(direction)
    if coor not in visited:
        visited[coor] = {}

    if dir_str not in visited[coor] or visited[coor][dir_str] > score:
        visited[coor][dir_str] = score
        if coor != end_loc:
            next_locs.append((dir_str, coor))
    
def is_next(coor, locs):
    for t in locs:
        if t[1] == coor:
            return True
    return False

def print_this_grid(grid, locs):

    for y, row in enumerate(grid):
        for x, _cell in enumerate(row):
            if (x,y) in locs:
                print("O", end='')
            else:
                print(grid[y][x], end='')
        print('')

def find_path(grid):

    start = end = None
    for y, row in enumerate(grid):
        if 'S' in row:
            start = (row.index("S"), y)
        if 'E' in row:
            end = (row.index("E"), y)

    print(f"Start {start}, end {end}")

    locs = [ (">", start)]
    visted = { start: {">": 0}}
    while True:
        next_locs = []
        for direction, coord in locs:
            
            current_score = visted[coord][direction]
            dir_vec = arrow_directions[direction]
            left_vec = turn_left(dir_vec)
            right_vec = turn_right(dir_vec)
            next_pos = add_coor(coord, dir_vec)
            left_pos = add_coor(coord,  left_vec)
            right_pos = add_coor(coord, right_vec)

            if get_cell(grid, next_pos) != "#":
                update_visited(visted, next_pos, dir_vec, current_score + 1,next_locs, end)
            if get_cell(grid, left_pos) != "#":
                update_visited(visted, left_pos, left_vec, current_score + 1001,next_locs, end)
            if get_cell(grid, right_pos) != "#":
                update_visited(visted, right_pos, right_vec, current_score + 1001,next_locs,end)

        if len(next_locs) == 0:
            break

        # print_this_grid(grid, visted, next_locs)
        locs = next_locs

    return visted, end, start


def part1(rows):
    grid = create_grid(rows)

    visited, end, start = find_path(grid)

    return min(visited[end].values())

def find_direction(distance, cell):
    for t in cell.items():
        if t[1] == distance:
            return t[0]

    return None

def part2(rows):

    grid = create_grid(rows)

    visited, end, start = find_path(grid)

    distance = part1(rows)

    distance_counter = { end: distance}

    cell = visited[end]
    distance = min(cell.values())
    starting_direction = find_direction(distance, cell)
    cur_locs = [(starting_direction, end)]

    visited_locs = {end}
    while len(cur_locs) > 0 and start not in cur_locs:
    # while cur_loc != start:

        new_cur_loc = []

        for cur_loc in cur_locs:
            cell = visited[cur_loc[1]]
            cur_distance = distance_counter[cur_loc[1]]
            for t in cell.items():

                dir_into = t[0]
                if t[1] > cur_distance:
                    continue
                step_back = opposite(dir_into)
                new_loc = add_coor(cur_loc[1], arrow_directions[step_back])

                if t[1] <= distance_counter[cur_loc[1]]:
                    if t[0] == cur_loc[0]:
                        distance_counter[new_loc] = distance_counter[cur_loc[1]] - 1
                    else:
                        distance_counter[new_loc] = distance_counter[cur_loc[1]] - 1001

                    if new_loc not in new_cur_loc and new_loc != start:
                        new_cur_loc.append((dir_into, new_loc))
                    visited_locs.add(new_loc)

        cur_locs = new_cur_loc

        # cell = visited[cur_loc]
        # distance = min(cell.values())
        # dir_into = find_direction(distance, cell)
        # step_back = opposite(dir_into)
        # cur_loc = add_coor(cur_loc, arrow_directions[step_back])
        # locs.append(cur_loc)


    print_this_grid(grid, visited_locs)

    return len(visited_locs)

print("Part 1")
print(f"Test : {part1(testData)}")
print(f"Test : {part1(testData2)}")
print(f"Actual : {part1(content)}")

print("Part 2")
print(f"Test : {part2(testData)} ")
print(f"Test : {part2(testData2)}")
print(f"Actual : {part2(content)} ")
