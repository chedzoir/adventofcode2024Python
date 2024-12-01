from adventofcode import load_content

content = load_content(1)

testData = [
    "3   4",
"4   3",
"2   5",
"1   3",
"3   9",
"3   3"
]

def parse(rows):
    left_list = []
    right_list = []
    for row in rows:
        vals = row.split("  ")
        left_list.append(int(vals[0]))
        right_list.append(int(vals[1]))

    return (left_list, right_list)

def part1(rows):

    (left_list, right_list) = parse(rows)

    left_list.sort()
    right_list.sort()

    dist = 0
    for i, val in enumerate(left_list):
        dist += abs(val - right_list[i])
    return dist


def part2(rows):
    
    (left_list, right_list) = parse(rows)

    similarity_score = 0
    for val in left_list:
        count = len([r for r in right_list if r == val])
        similarity_score += val * count

    return similarity_score


print("Part 1")
print(f"Test : {part1(testData)}")
print(f"Actual : {part1(content)}")

print("Part 2")
print(f"Test : {part2(testData)} ")
print(f"Actual : {part2(content)} ")
