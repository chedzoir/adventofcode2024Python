from adventofcode import load_content
from functools import reduce

content = load_content(7)

testData = [
    "190: 10 19",
    "3267: 81 40 27",
    "83: 17 5",
    "156: 15 6",
    "7290: 6 8 6 15",
    "161011: 16 10 13",
    "192: 17 8 14",
    "21037: 9 7 18 13",
    "292: 11 6 16 20",
]

def parse_row(row):
    [target, rest] = row.split(":")
    values = [ int(v) for v in rest.strip().split(' ')]
    return int(target), values


def target_possible(target, values, with_concat = False):

    vals = [ values[0]]

    for i in range(1, len(values)):
        new_vals = []

        for val in vals:
            v1 = val + values[i]
            v2 = val * values[i]

            if v1 <= target:
                new_vals.append(v1)
            if v2 <= target:
                new_vals.append(v2)

            if with_concat:
                v3 = int(str(val) + str(values[i]))
                if v3 <= target:
                    new_vals.append(v3)

        vals = new_vals

    return target in vals

def find_possible_value_sum(rows, with_concat = False):
    ok_count = 0
    for row in rows:
        target, values = parse_row(row)

        if target_possible(target, values, with_concat):
            ok_count += target
    
    return ok_count

def part1(rows):
    return find_possible_value_sum(rows)

def part2(rows):
    return find_possible_value_sum(rows, True)


print("Part 1")
print(f"Test : {part1(testData)}")
print(f"Actual : {part1(content)}")

print("Part 2")
print(f"Test : {part2(testData)} ")
print(f"Actual : {part2(content)} ")
