from adventofcode import load_content

content = load_content(24)

testData = """x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj""".split("\n")

def get_values(wire, values, rules, loop_detect = []):
    if wire in loop_detect:
        return None

    if wire in values:
        return values[wire]
    
    rule = rules[wire]

    wire_1_val = get_values(rule[0], values, rules, loop_detect + [wire])
    wire_2_val = get_values(rule[2], values, rules, loop_detect + [wire])

    if wire_1_val is None or wire_2_val is None:
        return None
    
    res = wire_1_val ^ wire_2_val if rule[1] == "XOR" else wire_1_val & wire_2_val if rule[1] == "AND" else wire_1_val | wire_2_val

    values[wire] = res

    return res

def get_inputs(wire, rules):
    if wire not in rules:
        return [int(wire[1:])]

    rule = rules[wire]

    return get_inputs(rule[0],rules) + get_inputs(rule[2],rules)

def parse(rows):
    values = {}
    rules = {}

    for row in rows:
        if ":" in row:
            [wire, initial_value] = row.split(":")
            values[wire] = int(initial_value.strip())
        if "->" in row:
            [wire1, logic, wire2, _arrow, target] = row.split(" ")
            rules[target] = (wire1, logic, wire2)

    return values, rules

def find_result(values, rules):
    z_wires = [k for k in rules.keys() if k[0] == 'z']
    z_wires.sort(reverse=True)

    res = ""

    for z_wire in z_wires:
        wire_values = get_values(z_wire, values, rules)
        if wire_values is None:
            return None
        res += f"{wire_values}"

    return int(res,2)

def part1(rows):
    values, rules = parse(rows)

    return find_result(values, rules)

def part2(rows):
    values, rules = parse(rows)

    simple_swap = []

    # Find the items that don't meet the simple rules    
    for r, txt in rules.items():
        if r[0] == 'z' and txt[1] != 'XOR' and r != "z45":
            simple_swap.append(r)
        elif r[0] != 'z' and txt[1] == 'XOR' and txt[0][0] not in ["x","y"]:
            simple_swap.append(r)

    swaps = {}
    for i in simple_swap:
        ident = max(get_inputs(i, rules))
        if ident not in swaps:
            swaps[ident] = []
        swaps[ident].append(i)

    for swap in swaps.values():
        (r1, r2) = swap
        r = rules[r1]
        rules[r1] = rules[r2]
        rules[r2] = r

    x_wires = [ r for r in values if r[0] == "x"]
    x_wires.sort(reverse=True)

    y_wires = [ r for r in values if r[0] == "y"]
    y_wires.sort(reverse=True)

    x_val = "".join([str(values[x]) for x in x_wires])
    y_val = "".join([str(values[y]) for y in y_wires])

    expected = int(x_val,2) + int(y_val,2)
    res = find_result(values.copy(), rules)

    error_part = list(f"{res ^ expected:b}")
    error_part.reverse()

    rule_with_error = f"z{error_part.index('1')+1}"

    possible_swaps = get_rules_to_swap(rule_with_error, rules)
    
    for i, rule_1 in enumerate(possible_swaps):
        for rule_2 in possible_swaps[i+1:]:
            mod_rules = rules.copy()
            mod_rules[rule_1] = rules[rule_2]
            mod_rules[rule_2] = rules[rule_1]

            next_res = find_result(values.copy(), mod_rules)

            if next_res is not None:
                if next_res ^ expected == 0:
                    simple_swap.append(rule_1)
                    simple_swap.append(rule_2)

    simple_swap.sort()

    return(",".join(simple_swap))


def get_rules_to_swap(rule, rules):
    if rule not in rules:
        return []
       
    rule_1, op, rule_2 = rules[rule]

    res = []

    if rule_1[0] not in ["x","y"]:
        res.append(rule_1)
    if rule_2[0] not in ["x","y"]:
        res.append(rule_2)
        

    return res + get_rules_to_swap(rule_1, rules) + get_rules_to_swap(rule_2, rules)

print("Part 1")
print(f"Test : {part1(testData)}")
print(f"Actual : {part1(content)}")

print("Part 2")
# print(f"Test : {part2(testData)} ")
print(f"Actual : {part2(content)} ")
