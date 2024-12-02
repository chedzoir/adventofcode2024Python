from adventofcode import load_content

content = load_content(2)

testData = [
    "7 6 4 2 1",
"1 2 7 8 9",
"9 7 6 2 1",
"1 3 2 4 5",
"8 6 4 4 1",
"1 3 6 7 9"
]

def calc_diffs(reports):
    res = []
    for i in range(0, len(reports) -1):
        res.append(reports[1+i] - reports[i])

    return res

def levels_safe(levels):
    diffs = calc_diffs(levels)
    min_level = min(diffs)
    max_level = max(diffs)

    return min_level > 0 and max_level <= 3 or min_level >= -3 and max_level < 0

def levels_safe_with_dampner(levels):
    if levels_safe(levels):
        return True

    for i in range(0, len(levels)) :
        level_x = levels[0:i] + levels[i+1:]
        if levels_safe(level_x):
            return True
        
    return False

def part1(rows):

    reports = [ [ int(r) for r in row.split(' ')] for row in rows]

    vals = [ levels for levels in reports if levels_safe(levels) ]

    return len(vals)

def part2(rows):
    reports = [ [ int(r) for r in row.split(' ')] for row in rows]

    vals = [ levels for levels in reports if levels_safe_with_dampner(levels) ]

    return len(vals)

print("Part 1")
print(f"Test : {part1(testData)}")
print(f"Actual : {part1(content)}")

print("Part 2")
print(f"Test : {part2(testData)} ")
print(f"Actual : {part2(content)} ")
