from adventofcode import load_content
from grid import create_grid, create_nm_grid, get_cell, set_cell, neighbours, in_grid, add_coor

content = load_content(12)

testData = [
    "RRRRIICCFF",
    "RRRRIICCCF",
    "VVRRRCCFFF",
    "VVRCCCJFFF",
    "VVVVCJJCFE",
    "VVIVCCJJEE",
    "VVIIICJJEE",
    "MIIIIIJJEE",
    "MIIISIJEEE",
    "MMMISSJEEE"    
]

def find_range(grid, chk_grid, coor, range_count):
    set_cell(chk_grid, coor, range_count)
    val = get_cell(grid, coor)

    res = [coor]
    for neighbour in neighbours(coor):
        if in_grid(grid, neighbour) and get_cell(grid, neighbour) == val and get_cell(chk_grid, neighbour) == -1:
            res += find_range(grid, chk_grid, neighbour, range_count)

    return res

def calc_ranges(grid):
    chk_grid = create_nm_grid(len(grid), len(grid[0]), -1)
        
    range_count = 0
    ranges = []
    for y, row in enumerate(chk_grid):
        for x, cell in enumerate(row):
            if cell == -1:
                range_coors = find_range(grid, chk_grid, (x,y), range_count)
                ranges.append(range_coors)
                range_count += 1

    return chk_grid, range_count, ranges

def count_contiguous_edges(vals):

    if len(vals) == 1:
        return 1
    
    return len([ t for t in vals if not t+1 in vals])

def count_edges(range_coors, cells, x_delta, y_delta):

    edge = [ e for e in cells if not ( e[0] + x_delta, e[1] + y_delta ) in range_coors]

    return count_contiguous_edges([ x if x_delta == 0 else y for (x,y) in edge])

def part1(rows):

    grid = create_grid(rows)

    chk_grid, range_count, _ranges = calc_ranges(grid)
    
    area = [ 0 for r in range(0, range_count)]
    permimeter = [ 0 for r in range(0, range_count)]

    for y, row in enumerate(grid):
        for x, _cell in enumerate(row):
            rng = get_cell(chk_grid, (x,y))
            area[rng] += 1
            for neighbour in neighbours((x,y)):
                if not in_grid(chk_grid, neighbour) or get_cell(chk_grid, neighbour) != rng:
                    permimeter[rng] += 1

    return sum( a * p for (a,p) in zip(area, permimeter))
         


def part2(rows):
    grid = create_grid(rows)

    _chk_grid, _range_count,ranges = calc_ranges(grid)
    
    area = []

    edge_counts = []
    for range_coors in ranges:
        area.append(len(range_coors))

        min_x = min(c[0] for c in range_coors)
        max_x = max(c[0] for c in range_coors)
        min_y = min(c[1] for c in range_coors)
        max_y = max(c[1] for c in range_coors)

        edge_count = 0
        
        # Count horizontal edges
        for y in range(min_y, max_y+1):
            row = [ e for e in range_coors if e[1] == y]

            edge_count += count_edges(range_coors, row, 0, -1) + count_edges(range_coors, row, 0, 1)

        # Count vertical edges
        for x in range(min_x, max_x + 1):
            column = [ e for e in range_coors if e[0] == x]

            edge_count += count_edges(range_coors, column, -1, 0) + count_edges(range_coors, column, 1, 0)

        edge_counts.append(edge_count)

    return sum( a * p for (a,p) in zip(area, edge_counts))

print("Part 1")
print(f"Test : {part1(testData)}")
print(f"Actual : {part1(content)}")

print("Part 2")
print(f"Test : {part2(testData)} ")
print(f"Actual : {part2(content)} ")
