directions = {
    "UP":(0,-1),
    "RIGHT":(1,0),
    "DOWN": (0,1),
    "LEFT": (-1,0)
}

def create_grid(rows):
    return [ [ r for r in row] for row in rows]

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
    
    if y >= len(grid) or x >= len(grid[0]):
        return False
    return True