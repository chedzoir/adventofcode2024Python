from adventofcode import load_content

content = load_content(9)

testData = [
    "2333133121414131402"
]

def parse(disk):
    disk_map = []
    cnt = 0
    start = 0
    for idx, val in enumerate(disk):
        if idx % 2 == 1:
            disk_map.append((int(val), -1))
        else:
            disk_map.append((int(val), cnt))
            cnt += 1
        start += int(val)
    return disk_map

def calc_check_sum(defrag):
    start = 0
    chk_sum = 0
    for t in defrag:
        (size, file_id) = t
        n_start = start
        n_end = start + size - 1
        if file_id >= 0:
            chk = ( n_end * (n_end + 1 ) - n_start * (n_start - 1)) // 2
            chk_sum += chk * file_id
        start = n_end + 1

    return chk_sum

def part1(rows):

    disk_map = parse(rows[0])
        
    left = 0
    right = len(disk_map) -1

    defrag = []
    while left <= right:
        left_val = disk_map[left]
        right_val = disk_map[right]
        if left_val[1] != -1:
            defrag.append(left_val)
        else:
            gap = left_val[0]
            added = 0
            while added < left_val[0]:
                to_add = min(gap, right_val[0])
                defrag.append((to_add, right_val[1]))
                added += to_add
                gap -= to_add
                disk_map[right] = (right_val[0] - to_add, right_val[1])

                if disk_map[right][0] == 0:
                    right -= 2
                right_val = disk_map[right]
        
        left += 1

    return calc_check_sum(defrag)

def find_pos (disk_map, loc, file_id):
    new_loc = min(loc, len(disk_map) - 1)
    while disk_map[new_loc][1] != file_id:
        new_loc -= 1

    return new_loc

def part2(rows):

    disk_map = parse(rows[0])
    
    file_id = disk_map[-1][1]

    loc = len(disk_map)-1

    while file_id > 0:
        item_to_move = disk_map[loc]

        new_loc = -1
        cntr = 0
        while cntr < loc:
            if disk_map[cntr][1] == -1 and disk_map[cntr][0] >= item_to_move[0]:
                new_loc = cntr
                break
            cntr += 1

        if new_loc > -1:
            to_replace = disk_map[new_loc]
            val_val2 = (to_replace[0] - item_to_move[0], -1)

            disk_map[new_loc] = item_to_move
            disk_map[loc]  = (item_to_move[0], -1)
            if (val_val2[0] > 0):
                disk_map.insert(new_loc + 1, val_val2)
                loc += 1

        file_id -= 1

        loc = find_pos(disk_map, loc, file_id)


    return calc_check_sum(disk_map)

print("Part 1")
print(f"Test : {part1(testData)}")
print(f"Actual : {part1(content)}")

print("Part 2")
print(f"Test : {part2(testData)} ")
print(f"Actual : {part2(content)} ")
