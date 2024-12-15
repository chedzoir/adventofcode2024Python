from adventofcode import load_content
from grid import create_grid,add_coor,get_cell, set_cell

content = load_content(15)

robot_directions = { "^":(0,-1),"v":(0,1),">":(1,0),"<":(-1,0)}

testData = [
    "########",
    "#..O.O.#",
    "##@.O..#",
    "#...O..#",
    "#.#.O..#",
    "#...O..#",
    "#......#",
    "########",
    "",
    "<^^>>>vv<v>>v<<"
]

testData2= [
    "##########",
    "#..O..O.O#",
    "#......O.#",
    "#.OO..O.O#",
    "#..O@..O.#",
    "#O#..O...#",
    "#O..O..O.#",
    "#.OO.O.OO#",
    "#....O...#",
    "##########",
    "",
    "<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^",
    "vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v",
    "><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<",
    "<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^",
    "^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><",
    "^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^",
    ">^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^",
    "<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>",
    "^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>",
    "v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"
]

testData3 = [
    "#######",
    "#...#.#",
    "#.....#",
    "#..OO@#",
    "#..O..#",
    "#.....#",
    "#######",
    "",
    "<vv<<^^<<^^"
]

def parse(rows):
    grid_info = []
    instructions = []
    to_grid= True
    for row in rows: 
        if not row == "":
            if to_grid:
                grid_info.append(row)
            else:
                instructions.append(row)
        else:
            to_grid = False 

    return create_grid(grid_info), "".join(instructions)

def boxes_to_bump(grid, loc, direction):
    cur_loc = loc
    bump = [cur_loc]
    while True:
        cur_loc = add_coor(cur_loc, direction)
        bump.append(cur_loc)
        if get_cell(grid, cur_loc) == "#":
            return []
        if get_cell(grid, cur_loc) == ".":
            return bump
        
def find_boxes_to_move(grid, direction, boxes):
    next_boxes = []
    for box in boxes:
        left = box
        right = add_coor(box, (1,0))

        next_left = add_coor(left, direction)
        next_right = add_coor(right, direction)

        if get_cell(grid, next_left) == "#" or get_cell(grid, next_right) == "#":
            return None
        
        if get_cell(grid, next_left) == "[":
            next_boxes.append(next_left)
        elif get_cell(grid, next_left) == "]":
            next_boxes.append(add_coor(next_left, (-1,0)))

        if get_cell(grid, next_right) == "[":
            next_boxes.append(next_right)

    if len(next_boxes) == 0:
        return [boxes]
    
    next_row = find_boxes_to_move(grid, direction, next_boxes)

    if next_row is None:
        return None
    
    return next_row + [boxes]

def move(grid, direction, x, y):
    new_loc = add_coor((x,y),direction)
    
    next_cell = get_cell(grid, new_loc)

    if next_cell == ".":
        set_cell(grid, (x,y), '.')
        set_cell(grid, new_loc, "@")
    elif next_cell == "#":
        new_loc = (x,y)
    else:

        if next_cell == "O" or direction == (-1,0) or direction == (1,0):
            bumps = boxes_to_bump(grid, new_loc, direction)

            if len(bumps) > 0:
                for idx in range(len(bumps)-1, 0, -1):
                    set_cell(grid, bumps[idx], get_cell(grid,bumps[idx-1]))
                set_cell(grid, new_loc, "@") 
                set_cell(grid, (x,y), '.')
            else:
                new_loc = (x,y)
        else:
            box1 = new_loc
            if next_cell == "]":
                box1 = add_coor(new_loc, (-1,0))

            boxes = find_boxes_to_move(grid, direction, [box1])

            if boxes is None:
                new_loc = (x,y)
            else:
                for row in boxes:
                    for left in row:
                        right = add_coor(left, (1,0))
                        next_left = add_coor(left, direction)
                        next_right = add_coor(right, direction)

                        set_cell(grid, next_left, "[")
                        set_cell(grid, next_right, "]")
                        set_cell(grid, left, ".")
                        set_cell(grid, right, ".")
                set_cell(grid, new_loc, "@")
                set_cell(grid, (x,y), ".")

    return new_loc

def find_start(grid):
    start_x = start_y = 0

    for y,row in enumerate(grid):
        if "@" in row:
            start_x = row.index("@")
            start_y = y

    return (start_x, start_y)

def score_grid(grid):
    score = 0
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == "O" or cell == "[":
                score += x + 100 * y
    return score

def part1(rows):

    grid, instructions = parse(rows)

    x,y = find_start(grid)

    for i in instructions:
        x,y = move(grid, robot_directions[i],x,y)

    return score_grid(grid)

def double(cell):
    if cell == ".":
        return [".","."]
    if cell == "@":
        return ["@","."]
    if cell == "#":
        return ["#","#"]
    return ["[","]"]

def part2(rows):

    grid, instructions = parse(rows)

    large_grid = []
    for row in grid:
        large_row = []
        for cell in row:
            large_row += double(cell)
        large_grid.append(large_row)

    x,y = find_start(large_grid)

    for i in instructions:
        x,y = move(large_grid, robot_directions[i],x,y)
            
    return score_grid(large_grid)


print("Part 1")
print(f"Test : {part1(testData)}")
print(f"Test : {part1(testData2)}")
print(f"Actual : {part1(content)}")

print("Part 2")
print(f"Test : {part2(testData3)} ")
print(f"Test : {part2(testData2)} ")
print(f"Actual : {part2(content)} ")
