from adventofcode import load_content

content = load_content(5)

testData = [
    "47|53",
    "97|13",
    "97|61",
    "97|47",
    "75|29",
    "61|13",
    "75|53",
    "29|13",
    "97|29",
    "53|29",
    "61|53",
    "97|53",
    "61|29",
    "47|13",
    "75|47",
    "97|75",
    "47|61",
    "75|61",
    "47|29",
    "75|13",
    "53|13",
    "",
    "75,47,61,53,29",
    "97,61,53,29,13",
    "75,29,13",
    "75,97,47,61,53",
    "61,13,29",
    "97,13,75,29,47"
]

def parse_data(rows):

    rules = {}
    updates = []

    for row in rows:
        if "|" in row:
            pages = row.split("|")
            if not pages[0] in rules:
                rules[pages[0]] = []
            rules[pages[0]].append( pages[1])
        elif "," in row:
            updates.append(row.split(","))
    return rules, updates

def update_ok(rules, update):
    for page in update:
        if page in rules:
            if not page_ok(rules, update, page):
                    return False
    return True

def page_ok(rules, update, page):
    idx = update.index(page)
    for other_page in rules[page]:
        if other_page in update and update.index(other_page) < idx:
            return False
    return True

def part1(rows):

    rules, updates = parse_data(rows)

    res = 0
    for update in updates:
        if update_ok(rules, update):
            res += int(update[len(update)//2])

    return res

def sort_pages(rules, update):
    res = update[:]
    for page in update:
        if page in rules and not page_ok(rules, update, page):
            res.remove(page)
            positions = [ update.index(r) for r in rules[page] if r in update]
            res.insert(min(positions), page)
            return sort_pages(rules, res)
    return res

def part2(rows):
    rules, updates = parse_data(rows)

    res = 0
    for update in updates:
        if not update_ok(rules, update):
            sorted_update = sort_pages(rules, update)
            res += int(sorted_update[len(sorted_update)//2])

    return res

print("Part 1")
print(f"Test : {part1(testData)}")
print(f"Actual : {part1(content)}")

print("Part 2")
print(f"Test : {part2(testData)} ")
print(f"Actual : {part2(content)} ")
