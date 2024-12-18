from adventofcode import load_content
from grid import create_nm_grid, print_grid, set_cell, get_cell, neighbours, in_grid

content = load_content(18)

testData = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0""".split("\n")

def to_coord(val):
    [x,y] = [ int(t) for t in val.split(",")]
    return (x,y)

def parse(rows):
    return [ to_coord(row) for row in rows]

def find_shortest_distance(grid, size):

    start = (0,0)
    end = (size-1, size-1)

    locs = {start}
    visited = {start : 0}

    while len(locs) > 0:
        new_locs= set()

        for loc in locs:
            distance = visited[loc]

            for neighbour in neighbours(loc):
                if in_grid(grid, neighbour) and  get_cell(grid, neighbour) != '#':
                    if neighbour not in visited:
                        visited[neighbour] = distance + 1
                        new_locs.add(neighbour)
                    elif visited[neighbour] > distance + 1:
                        visited[neighbour] = distance + 1
                        new_locs.add(neighbour)

        locs = new_locs

    if end not in visited:
        return None

    return visited[end]

def part1(rows, size, count):

    coords = parse(rows)

    grid = create_nm_grid(size, size, ".")

    for i in range(count):
        set_cell(grid, coords[i], '#')

    return find_shortest_distance(grid, size)

def part2(rows, size):
    coords = parse(rows)

    grid = create_nm_grid(size, size, ".")

    for c in coords:
        set_cell(grid, c, '#')
        if find_shortest_distance(grid, size) is None:
            return c

print("Part 1")
print(f"Test : {part1(testData, 7, 12)}")
print(f"Actual : {part1(content, 71, 1024)}")

print("Part 2")
print(f"Test : {part2(testData, 7)} ")
print(f"Actual : {part2(content, 71)} ")
