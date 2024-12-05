from adventofcode import load_content
import re

content = load_content(3)

testData = ["xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"]
testData2 = ["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"]

def part1(rows):

    res = 0

    for memory in rows:

        muls = re.findall(r'mul\((\d+),(\d+)\)', memory)

        for mul in muls:
            res += int(mul[0]) * int(mul[1])

    return res

def part2(rows):
    res = 0
    on = True

    for memory in rows:

        muls = re.findall(r'(mul)\((\d+),(\d+)\)|(don?\'?t?)\(\)', memory)

        for mul in muls:
            if mul[0] == "mul" and on:
                res += int(mul[1]) * int(mul[2])
            elif mul[3] == "do":
                on = True
            elif mul[3] == "don't":
                on = False

    return res
    

print("Part 1")
print(f"Test : {part1(testData)}")
print(f"Actual : {part1(content)}")

print("Part 2")
print(f"Test : {part2(testData2)} ")
print(f"Actual : {part2(content)} ")
