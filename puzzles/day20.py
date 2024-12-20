from adventofcode import load_content
from grid import create_grid, neighbours, get_cell, set_cell, manhatten_distance

content = load_content(20)

testData = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############""".split("\n")

def walk_path(grid):

    start = None
    end = None
    for y, row in enumerate(grid):
        if 'S' in row:
            start = (row.index('S'), y)
        if 'E' in row:
            end = (row.index('E'), y)
            
    distances = {}
    steps = 0
    curloc = start
    while curloc != end:
        distances[curloc] = steps
        if curloc != start:
            set_cell(grid, curloc, "o")
        for neighbour in neighbours(curloc):
            if (get_cell(grid, neighbour) == "." and neighbour not in distances) or neighbour == end:
                curloc = neighbour
                break

        steps += 1

    distances[end] = steps

    return distances

def calc_cheats(distances, duration):

    short_cuts = []
    path = list(distances.keys())

    for i, start in enumerate(path):
        for end in path[i+1:]:
            if manhatten_distance(start, end) <= duration:
                short_cut = abs(distances[start] - distances[end]) - manhatten_distance(start, end)
                if short_cut >= duration:
                    short_cuts.append(short_cut)

    return short_cuts


def calcuate(rows, cheat_time):
    grid = create_grid(rows)
    distances = walk_path(grid)
    short_cuts = calc_cheats(distances, cheat_time)
    return len([ s for s in short_cuts if s >= 100])

def part1(rows):
    return calcuate(rows, 2)

def part2(rows):
    return calcuate(rows, 20)


print("Part 1")
print(f"Test : {part1(testData)}")
print(f"Actual : {part1(content)}")

print("Part 2")
print(f"Test : {part2(testData)} ")
print(f"Actual : {part2(content)} ")
