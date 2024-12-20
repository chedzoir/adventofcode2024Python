directions = {
    "UP":(0,-1),
    "RIGHT":(1,0),
    "DOWN": (0,1),
    "LEFT": (-1,0)
}

arrow_directions = { "^":(0,-1),"v":(0,1),">":(1,0),"<":(-1,0)}

def opposite(direction):
    if direction == "^":
        return "v"
    if direction == "v":
        return "^"
    if direction == ">":
        return "<"
    if direction == "<":
        return ">"

def create_grid(rows):
    return [ list(row) for row in rows]

def create_nm_grid(m, n, value = 0):
    return [ [ value for _i in range(0,m)] for _j in range(0,n) ]

def print_grid(grid):
    print("\n".join([ "".join(g) for g in grid]))

def add_coor(a,b):
    return (a[0]+b[0], a[1] + b[1])

def turn_right(a):
    (x,y) = a
    return ( -1 * y,  x)

def turn_left(a):
    (x,y) = a
    return ( y, -1 * x)

def get_cell(grid, coor):
    return grid[coor[1]][coor[0]]

def set_cell(grid, coor, value) :
    (x,y) = coor
    grid[y][x] = value

def in_grid(grid, coor):
    (x,y) = coor
    if x < 0 or y < 0:
        return False
    
    if y >= len(grid) or x >= len(grid[y]):
        return False
    return True

def create_vector(coor1, coor2):
    (x1,y1) = coor1
    (x2,y2) = coor2

    return (x1-x2, y1-y2)

def add_vector(coor, vector):
    (x,y) = coor
    (x_delta, y_delta) = vector
    return ( x + x_delta, y + y_delta)

def subtract_vector(coor, vector):
    (x,y) = coor
    (x_delta, y_delta) = vector
    return ( x - x_delta, y - y_delta)

def neighbours(coor):
    return [ add_coor(coor, dir) for dir in directions.values()]

def manhatten_distance(coor1, coor2):
    return abs(coor1[0] - coor2[0]) + abs(coor1[1] - coor2[1])