from adventofcode import load_content

content = load_content(22)

testData = [ "1","10","100","2024"]

testData2 = [ "1","2","3","2024"]

def mix(val, secret):
    return val ^ secret

def prune(secret):
    return secret % 16777216

def calculate(secret):
    res = prune(mix(secret * 64 , secret))
    res = prune(mix(res // 32, res))
    return prune(mix(res * 2048, res))

def find_secret(initial_secret, count):

    secret = initial_secret
    secret_array = [ secret ]
    for _i in range(count):
        secret = calculate(secret)
        secret_array.append(secret)

    return secret_array

def part1(rows):

    total = 0
    for secret in rows:
        mm_secret = find_secret(int(secret),2000)
        total += mm_secret[-1]

    return total

def part2(rows):

    all_possible = []
    sequences = set()
    for secret in rows:
        mm_secret = find_secret(int(secret), 2000)
        prices = [ a % 10 for a in mm_secret]
        
        diffs = [ prices[i+1] -prices[i] for i in range(len(prices) -1)]

        possible_prices = {}
        for i in range(len(diffs) - 3):
            sequence = tuple(diffs[i:i+4])
            if sequence not in possible_prices:
                possible_prices[sequence] = prices[i+4]
                sequences.add(sequence)

        all_possible.append(possible_prices)

    bananas = {}

    for sequence in sequences:
        total = 0
        for poss in all_possible:
            if sequence in poss:
                total += poss[sequence]
        bananas[sequence] = total

    max_banana = max(bananas.values())
    return max_banana

print("Part 1")
print(f"Test : {part1(testData)}")
print(f"Actual : {part1(content)}")

print("Part 2")
print(f"Test : {part2(testData2)} ")
print(f"Actual : {part2(content)} ")
