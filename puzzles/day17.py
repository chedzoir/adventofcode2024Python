from adventofcode import load_content
import math

content = load_content(17)

testData = """Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0""".split("\n")

testData2 = """Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0""".split("\n")

def combo(register, val):
    if val == 4:
        return register["A"]
    if val == 5:
        return register["B"]
    if val == 6:
        return register["C"]
    return val


def get_combo(val):
    if val == 4:
        return "A"
    if val == 5:
        return "B"
    if val == 6:
        return "C"
    return val


def parse(rows):
    register = {}
    program = []

    for row in rows:
        if "Register" in row:
            vals = row.split(" ")
            register[vals[1][0]] = int(vals[2])
        elif "Program" in row:
            program = [int(t) for t in (row.split(" ")[1]).split(",")]

    return register, program

def run_program(register, program):

    ptr = 0
    output = []

    while ptr < len(program):
        inst = program[ptr]
        operand = program[ptr+1]

        jump = 2
        if inst == 0:
            register["A"] =  register["A"] // ( 2 ** combo(register,operand))
        elif inst == 1:
            register["B"] = register["B"] ^ operand
        elif inst == 2:
            register["B"] = combo(register, operand) % 8
        elif inst == 3:
            if register["A"] != 0:
                ptr = operand
                jump = 0
        elif inst == 4:
            register["B"] =  register["B"] ^ register["C"]
        elif inst == 5:
            output.append(combo(register, operand) % 8)
        elif inst == 6:
            register["B"] =  register["A"] // ( 2 ** combo(register,operand))
        elif inst == 7:
            register["C"] =  register["A"] // ( 2 ** combo(register,operand))
            
        ptr += jump
   
    return output

def part1(rows):
    register, program = parse(rows)
    output = run_program(register, program)
    return ",".join([str(o) for o in output])


# The trick with part 2 is to note that we a is divided by 8 with every loop 
# so we can work backwards and find all possible values that give the result 
# then take the min at the end
def part2(rows):
    _register, program = parse(rows)

    rev_program = program.copy();
    rev_program.reverse()

    pos_reg_a = [0]

    expected = []
    for r in rev_program:

        expected = [r] + expected
        new_reg_a = []

        for reg_a in pos_reg_a:
            for pos_a in range(8):
                a_val = reg_a * 8 + pos_a
                result = run_program({"A":a_val, "B":0,"C":0}, program)
                if result == expected and a_val not in new_reg_a:
                    new_reg_a.append(a_val)

        pos_reg_a = new_reg_a        


    return min(pos_reg_a)

    
print("Part 1")
print(f"Test : {part1(testData)}")
print(f"Actual : {part1(content)}")

print("Part 2")
print(f"Test : {part2(testData2)} ")
print(f"Actual : {part2(content)} ")
