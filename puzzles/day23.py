from adventofcode import load_content

content = load_content(23)

testData = """kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn""".split("\n")


def get_network(rows):
    network = {}

    for row in rows:
        [c1,c2] = row.split("-")
        if c1 not in network:
            network[c1] = []
        if c2 not in network:
            network[c2] = []
        network[c1].append(c2)
        network[c2].append(c1)

    return network

def part1(rows):

    network = get_network(rows)

    computers, adj_matrix = create_adjacency_matrix(network)

    interconnected = []
    for i, c_i in enumerate(computers):
        for j in range(i+1, len(computers)):
            if adj_matrix[i][j] == 1:
                for k in range(j+1, len(computers)):
                    if adj_matrix[i][k] == 1 and adj_matrix[j][k] == 1:
                        interconnected.append([c_i, computers[j], computers[k]])
    
    with_a_t = [ ic for ic in interconnected if ic[0].startswith('t') or ic[1].startswith('t') or ic[2].startswith('t')]

    return len(with_a_t)

def swap(matrix, c1, c2):
    temp_row = matrix[c1]
    matrix[c1] = matrix[c2]
    matrix[c2] = temp_row

    for row in matrix:
        temp_cell = row[c1]
        row[c1] = row[c2]
        row[c2] = temp_cell

def arrange_matrix(matrix, computers):
    row = 0
    
    while row < len(matrix):
        col = row + 1
        while col < len(matrix[row]):
            if matrix[row][col] == 1 and 0 in matrix[row][row+1:col]:
                swap_col_from = col
                swap_col_to = row + 1 + matrix[row][row+1:col].index(0)
                swap(matrix, swap_col_to, swap_col_from)
                tc = computers[swap_col_to]
                computers[swap_col_to] = computers[swap_col_from]
                computers[swap_col_from] = tc

            col += 1
        row += 1
    
def good(computers, network):
    for c in computers:
        neighbours = network[c]
        for c2 in computers:
            if c2 != c and c2 not in neighbours:
                return False
    return True

def create_adjacency_matrix(network):
    computers = list(network.keys())
    computers.sort()

    adj_matrix = [ [ 0 for _i in range(len(computers))] for _j in range(len(computers))]

    for idx, c in enumerate(computers):
        for c2 in network[c]:
            idx_2 = computers.index(c2)
            adj_matrix[idx][idx_2] = 1
            adj_matrix[idx_2][idx] = 1

    return computers, adj_matrix


def part2(rows):

    network = get_network(rows)

    computers, adj_matrix = create_adjacency_matrix(network)

    arrange_matrix(adj_matrix, computers)

    lan_size = []

    for i, row in enumerate(adj_matrix):
        j = i + 1
        while j < len(row) and row[j] != 0:
            j += 1
        lan_size.append(j-i)

    max_value = max(lan_size)


    res = ""
    for idx, value in enumerate(lan_size):
        if value == max_value:
            possible_computers = set([ computers[idx + i] for i in range(max_value)])

            if good(possible_computers, network):
                l = list(possible_computers)
                l.sort()
                res = ",".join(l)
        
    return res

print("Part 1")
print(f"Test : {part1(testData)}")
print(f"Actual : {part1(content)}")

print("Part 2")
print(f"Test : {part2(testData)} ")
print(f"Actual : {part2(content)} ")
