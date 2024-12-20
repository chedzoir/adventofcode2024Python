from adventofcode import load_content

content = load_content(19)

testData = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb""".split('\n')


def count_combos(pattern, towels, pattern_cache):

    if pattern in pattern_cache:
        return pattern_cache[pattern]

    res = 0
    for towel in towels:
        if pattern == towel:
            res += 1
        elif pattern.startswith(towel):
            res += count_combos(pattern[len(towel):], towels, pattern_cache)

    pattern_cache[pattern] = res
    return res

def count_towel_combos(rows):
    available = [t.strip() for t in rows[0].split(",")]
    patterns = rows[2:]
    pattern_cache = {}
    return [ count_combos(pattern, available, pattern_cache) for pattern in patterns]

def part1(rows):
    counts = count_towel_combos(rows)
    return len([ c for c in counts if c != 0])

def part2(rows):
    counts = count_towel_combos(rows)
    return sum(counts)

print("Part 1")
print(f"Test : {part1(testData)}")
print(f"Actual : {part1(content)}")

print("Part 2")
print(f"Test : {part2(testData)} ")
print(f"Actual : {part2(content)} ")
