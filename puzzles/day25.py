from adventofcode import load_content

content = load_content(25)

testData = """#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####""".split("\n")

def parse(rows):


    item = []
    items = [item]

    for row in rows:
        if len(row) == 0:
            item = []
            items.append(item)
        else:
            item.append(row)

    keys = []
    locks = []

    for item in items:
        is_lock = item[0] == "....."

        pins = [ 0,0,0,0,0]

        for item_row in item[1:6]:
            for idx, pin in enumerate(item_row):
                if pin == "#":
                    pins[idx] +=1

        if is_lock:
            locks.append(pins)
        else:
            keys.append(pins)

    return locks, keys


def part1(rows):

    locks, keys = parse(rows)

    match = 0

    for lock in locks:
        for key in keys:
            overlap = [ a + b for a,b in zip(lock, key)]

            if max(overlap) <= 5:
                match += 1
    return match

def part2(rows):
    None

print("Part 1")
print(f"Test : {part1(testData)}")
print(f"Actual : {part1(content)}")

print("Part 2")
print(f"Test : {part2(testData)} ")
print(f"Actual : {part2(content)} ")
