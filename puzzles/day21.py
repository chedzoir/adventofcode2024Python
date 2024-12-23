from adventofcode import load_content

content = load_content(21)

testData = [
    "029A",
    "980A",
    "179A",
    "456A",
    "379A"
]

direction_key_pad=  {
        "^": (1,0),
        "A": (2,0),
        "<": (0,1),
        "v": (1,1),
        ">": (2,1)
    }

def key_pad():
    key_pad_coors = {}
    for i in range(9) :
        x = i % 3
        y = 2 - (i // 3)
        key_pad_coors[f"{i+1}"] = (x,y)

    key_pad_coors["0"] = (1,3)
    key_pad_coors["A"] = (2,3)

    return key_pad_coors

def possible_paths(keypad):
    keys = list(keypad.keys())

    all_paths = {}
    for key_1 in keys:
        all_paths[key_1] = {}
        for key_2 in keys:
            all_paths[key_1][key_2] = create_path(key_1, key_2, keypad)

    return all_paths

def create_path(start, end, key_pad_coors):

    (s_x, s_y)  = key_pad_coors[start]
    (e_x, e_y)  = key_pad_coors[end]
    vert = "^" if s_y > e_y else "v"
    horiz = ">" if s_x < e_x else "<"

    x_path = "".join([ horiz for x in range(abs(e_x - s_x))])
    y_path = "".join([ vert for y in range(abs(e_y - s_y))])

    if end in ["0", "A"] and start in [ "7", "4", "1"]:
        return [x_path + y_path]

    if start in ["0", "A"] and end in [ "7", "4", "1"]:
        return [y_path + x_path]

    if start in ["<"] and end in ["^","A"]:
        return [x_path + y_path]

    if end in ["<"] and start in ["^","A"]:
        return [y_path + x_path]

    return set( [x_path + y_path,  y_path + x_path])

numberpad_paths = possible_paths(key_pad())

direction_pad_paths = possible_paths(direction_key_pad)

def calc_shortest_paths(value, keypad_paths):
    last_key = "A"

    key_pad_path = [[]]
    for key in value:
        next_key_pad_path = []
        path_to_next_key = keypad_paths[last_key][key]

        for path in key_pad_path:
            for next_step in path_to_next_key:
                next_key_pad_path.append(path.copy() + [next_step + "A"])

        last_key = key
        key_pad_path = next_key_pad_path

    return key_pad_path


def get_count_shortest_key_strokes(path, cache, robot_count, level = 0):
    full_path = "".join(path)

    if full_path in cache and level in cache[full_path]:
        return cache[full_path][level]
    
    if full_path not in cache:
        cache[full_path] = {}   

    res = count_shortest_key_strokes(path, cache, robot_count, level)

    cache[full_path][level] = res
    
    return res


def count_shortest_key_strokes(path, cache, robot_count, level = 0):

    if level == robot_count:
        return sum(len(p) for p in path)
    
    res = 0

    for p in path: 
        paths = calc_shortest_paths(p, direction_pad_paths)
        lengths = min(get_count_shortest_key_strokes(sub_path, cache, robot_count, level + 1) for sub_path in paths)
        res += lengths

    return res

def run_puzzle(rows, robot_count):

    cache = {}

    total = 0
    for row in rows:
        key_pad_path = calc_shortest_paths(row, numberpad_paths)
        strokes = [ get_count_shortest_key_strokes(path, cache, robot_count) for path in key_pad_path]
        total += min(strokes) * int(row[0:-1])

    return total

def part1(rows):
    return run_puzzle(rows, 2)


def part2(rows):
    return run_puzzle(rows, 25)

print("Part 1")
print(f"Test : {part1(testData)}")
print(f"Actual : {part1(content)}")

print("Part 2")
print(f"Test : {part2(testData)} ")
print(f"Actual : {part2(content)} ")
