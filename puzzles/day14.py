from adventofcode import load_content

content = load_content(14)

testData = [
    "p=0,4 v=3,-3",
"p=6,3 v=-1,-3",
"p=10,3 v=-1,2",
"p=2,0 v=2,-1",
"p=0,0 v=1,3",
"p=3,0 v=-2,-2",
"p=7,6 v=-1,-3",
"p=3,0 v=-1,-2",
"p=9,3 v=2,3",
"p=7,3 v=-1,2",
"p=2,4 v=2,-3",
"p=9,5 v=-3,-3"

]

def parse(rows):
    res = []
    for row in rows:
        [start, velocity] = row.split(' ')
        start_coors = [int(t) for t in start[2:].split(',')]
        velocity_vector = [ int(t) for t in velocity[2:].split(',')]

        res.append((start_coors, velocity_vector))

    return res

def print_grid(robot_locations, width, height):

    grid = [ [ '.' for x in range(0, width)] for y in range(0, height)]

    for (x,y) in robot_locations:
        grid[y][x] = "x"

    print("\n".join(["".join(row) for row in grid]))

def part1(rows, width, height):

    robots = parse(rows)

    ending_locations = []

    for robot in robots:
        [start, velocity] = robot

        final_pos = (( start[0] + 100 * velocity[0] ) % width, (start[1] + 100 * velocity[1]) % height)

        ending_locations.append(final_pos)


        
    quad_count = [ 0,0,0,0]
    quad_height = height // 2
    quad_width = width // 2

    for (x,y) in ending_locations:
        quad = -1

        if x < quad_width:
            if y < quad_height:
                quad = 0
            elif y > quad_height:
                quad =  2
        elif x > quad_width:
            if y < quad_height:
                quad = 1
            elif y > quad_height:
                quad =  3

        if quad > -1:
            quad_count[quad] += 1

    res = 1
    for q in quad_count:
        res *= q

    return res

def part2(rows):

    robots = parse(rows)

    height = 103
    width  = 101

    move = 1

    while True:
        ending_locations = []
        for robot in robots:
            [start, velocity] = robot

            final_pos = (( start[0] + move * velocity[0] ) % width, (start[1] + move * velocity[1]) % height)

            ending_locations.append(final_pos)
 
        if len(ending_locations) == len(set(ending_locations)):
            print_grid(ending_locations, width, height)
            break

        move += 1
    
    return move

print("Part 1")
print(f"Test : {part1(testData, 11, 7)}")
print(f"Actual : {part1(content,101,103)}")

print("Part 2")
# print(f"Test : {part2(testData)} ")
print(f"Actual : {part2(content)} ")
