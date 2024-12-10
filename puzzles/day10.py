from adventofcode import load_content
from grid import get_cell, in_grid

content = load_content(10)

testData = [
    "89010123",
"78121874",
"87430965",
"96549874",
"45678903",
"32019012",
"01329801",
"10456732"
]

def walk(grid, paths, current_val):
    res = []
    next_val = current_val + 1

    for path in paths:
        (x,y) = path[-1]
        coors = [(x+1,y), (x-1,y), (x, y-1), (x, y+1)]
        for coor in coors:
            if in_grid(grid, coor) and get_cell(grid, coor) == next_val:
                res.append(path + [coor])

    if next_val == 9:
        return res

    return walk(grid, res, next_val)

def score_trails(rows):

    grid = [ [ int(r) for r in row] for row in rows]

    trail_heads = []
    for y, row in enumerate(grid):
        for x, cell in enumerate(grid[y]):
            if cell == 0:
                trail_heads.append((x,y))

    sum_score = 0
    sum_rating = 0
    for trail_head in trail_heads:
        paths = walk(grid, [[trail_head]], 0 )

        trail_ends = set()
        for path in paths:
            trail_ends.add(path[-1])
        sum_score += len(trail_ends)
        sum_rating += len(paths)

    return sum_score, sum_rating

def part1(rows):
    sum_score, _sum_rating = score_trails(rows)

    return sum_score

def part2(rows):
    _sum_score, sum_rating = score_trails(rows)

    return sum_rating

print("Part 1")
print(f"Test : {part1(testData)}")
print(f"Actual : {part1(content)}")

print("Part 2")
print(f"Test : {part2(testData)} ")
print(f"Actual : {part2(content)} ")
