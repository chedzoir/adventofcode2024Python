from adventofcode import load_content
import math

content = load_content(11)

testData = [
    "125 17"
]

def split(stone):

    return len(str(stone)) % 2 == 0

def split_stone(stone):

    if stone == 10:
        return [1,0]

    digits = math.ceil(math.log10(stone))
    mult = math.pow(10, digits //2)
    right = stone % mult
    left = (stone - right)  // mult

    return [left, right]

def blink_stone(stone):
    if stone == 0:
        return [1]
    elif split(stone):
        return split_stone(stone)
    else:
        return [ stone * 2024]

def blink(stones):

    res = {}

    for stone, count in stones.items():
        blinked = blink_stone(stone)

        for t in blinked:
            if not t in res :
                res[t] = 0
            res[t] += count
    
    return res

def blink_blink(stone_input, count):

    stones = { int(r) : 1 for r in stone_input.split(' ')}

    for _i in range(0, count):
        stones = blink(stones)

    return sum(stones.values())

def part1(rows):
    return blink_blink(rows[0], 25)
    
def part2(rows):
    return blink_blink(rows[0], 75)

print("Part 1")
print(f"Test : {part1(testData)}")
print(f"Actual : {part1(content)}")

print("Part 2")
print(f"Test : {part2(testData)} ")
print(f"Actual : {part2(content)} ")
