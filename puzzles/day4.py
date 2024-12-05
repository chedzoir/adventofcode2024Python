from adventofcode import load_content

content = load_content(4)

testData = [
    "MMMSXXMASM",
"MSAMXMSMSA",
"AMXSXMAAMM",
"MSAMASMSMX",
"XMASAMXAMM",
"XXAMMXXAMA",
"SMSMSASXSS",
"SAXAMASAAA",
"MAMMMXMMMM",
"MXMXAXMASX"
]

def get_val(grid, x,y):
    if 0 <= y < len(grid):
        if 0 <= x < len(grid[y]):
            return grid[y][x]
    return ''

def get_xmas(rows, x, y, x_factor, y_factor, start = 0, limit = 4):
    return ''.join([ get_val(rows,x + x_factor * i, y + y_factor * i) for i in range(start,limit)])

def count_xmas(rows, x, y):
    up = get_xmas(rows, x,y,0,-1)
    down = get_xmas(rows, x,y,0,1)
    left = get_xmas(rows, x,y,-1,0)
    right = get_xmas(rows, x,y,1,0)


    d1 = get_xmas(rows, x,y,-1,-1)
    d2 = get_xmas(rows, x,y,-1,1)
    d3 = get_xmas(rows, x,y,1,-1)
    d4 = get_xmas(rows, x,y,1,1)


    vals = [up, down, left, right, d1,d2,d3,d4]

    return len([ v for v in vals if v == 'XMAS'])

def count_x_mas(rows, x, y):
     d1 = get_val(rows, x-1, y-1) + get_val(rows, x,y) + get_val(rows, x+1, y+1)
     d2 = get_val(rows, x-1, y+1) + get_val(rows, x,y) + get_val(rows, x+1, y-1)

     if (d1 == 'MAS' or d1 == 'SAM') and (d2 == 'MAS' or d2 == 'SAM'):
          return 1
     return 0

def part1(rows):

    count = 0
    for y, row in enumerate(rows):
        for x, row in enumerate(row):
            if get_val(rows, x,y) == 'X':
                count += count_xmas(rows, x, y)

    return count

def part2(rows):
    count = 0
    for y, row in enumerate(rows):
        for x, row in enumerate(row):
            if get_val(rows, x,y) == 'A':
                count += count_x_mas(rows, x, y)

    return count

print("Part 1")
print(f"Test : {part1(testData)}")
print(f"Actual : {part1(content)}")

print("Part 2")
print(f"Test : {part2(testData)} ")
print(f"Actual : {part2(content)} ")
