from adventofcode import load_content
import math 

content = load_content(13)

testData = [
    "Button A: X+94, Y+34",
"Button B: X+22, Y+67",
"Prize: X=8400, Y=5400",
"",
"Button A: X+26, Y+66",
"Button B: X+67, Y+21",
"Prize: X=12748, Y=12176",
"",
"Button A: X+17, Y+86",
"Button B: X+84, Y+37",
"Prize: X=7870, Y=6450",
"",
"Button A: X+69, Y+23",
"Button B: X+27, Y+71",
"Prize: X=18641, Y=10279"
]

def parse(rows):

    insts = []

    curr_inst = []
    insts.append(curr_inst)
    for row in rows:
        if ":" in row:
            [_item, rest] = row.split(":")
            delim = "+" if "+" in rest else "="
            [x,y] = [ int(r.strip().split(delim)[1]) for r in rest.split(",")]
            curr_inst.append((x,y))
        else:
            curr_inst = []
            insts.append(curr_inst)

    return insts

def token_count(but_a, but_b, prize, prize_adjust = 0):
    (a_x, a_y) = but_a
    (b_x, b_y) = but_b
    (p_x, p_y) = prize

    p_x += prize_adjust
    p_y += prize_adjust

    a_moves = (p_x * b_y - p_y * b_x) / (a_x * b_y - a_y * b_x)
    b_moves = ( p_x - a_moves * a_x ) / b_x

    if a_moves.is_integer() and b_moves.is_integer():
        return math.floor(a_moves * 3 + b_moves)
    
    return 0

def run_puzzle(rows, delta):
    instructions = parse(rows)

    tokens = 0
    for instruction in instructions:
        [but_a, but_b, prize] = instruction
        tokens += token_count(but_a, but_b, prize,delta)

    return tokens

def part1(rows):
    return run_puzzle(rows, 0)

def part2(rows):
    return run_puzzle(rows, 10000000000000)


print("Part 1")
print(f"Test : {part1(testData)}")
print(f"Actual : {part1(content)}")

print("Part 2")
print(f"Test : {part2(testData)} ")
print(f"Actual : {part2(content)} ")
