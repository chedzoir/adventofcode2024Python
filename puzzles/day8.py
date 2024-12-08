from adventofcode import load_content
from grid import create_grid,create_vector,add_vector,subtract_vector, in_grid

content = load_content(8)

testData = [
"............",
"........0...",
".....0......",
".......0....",
"....0.......",
"......A.....",
"............",
"............",
"........A...",
".........A..",
"............",
"............"
]

def find_anti_node(grid, location, delta, add_until_hit_edge = False):
    res = set()

    current_loc = location

    while True:
        current_loc = add_vector(current_loc, delta)
        if in_grid(grid, current_loc):
            res.add(current_loc)
        if not add_until_hit_edge or not in_grid(grid, current_loc):
            return res

def count_anti_nodes(rows, add_until_hit_edge = False):

    grid = create_grid(rows)

    locs = {}

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell != '.':
                if not cell in locs:
                    locs[cell] = []
                locs[cell].append((x,y))


    anti_nodes = set()
    for coors in locs.values():
        pairs = []
        for i, val in enumerate(coors):
            for j in range(i+1, len(coors)):
                pairs.append((val, coors[j]))

        for pair in pairs:

            (node1, node2) = pair

            delta = create_vector(node1, node2)

            anti_nodes.update(find_anti_node(grid, node1, delta, add_until_hit_edge))
            anti_nodes.update(find_anti_node(grid, node2, (- delta[0], - delta[1]), add_until_hit_edge))

            if add_until_hit_edge:
                anti_nodes.add(node2)
                anti_nodes.add(node1)
    return len(anti_nodes)

def part1(rows):
    return count_anti_nodes(rows)

def part2(rows):
    return count_anti_nodes(rows, True)

print("Part 1")
print(f"Test : {part1(testData)}")
print(f"Actual : {part1(content)}")

print("Part 2")
print(f"Test : {part2(testData)} ")
print(f"Actual : {part2(content)} ")
