def min_teleports(t, test_cases):
    results = []

    for _ in range(t):
        n = test_cases[_][0]
        sequence = test_cases[_][1]

        min_teleports_count = 0
        prev_value = 0

        for i in range(n):
            min_teleports_count = max(min_teleports_count, sequence[i] - prev_value)
            prev_value = sequence[i]

        results.append(min_teleports_count)

    return results

# Input reading
t = int(input())
test_cases = []

for _ in range(t):
    n = int(input())
    sequence = list(map(int, input().split()))
    test_cases.append((n, sequence))

# Calculate and print the results
results = min_teleports(t, test_cases)
for result in results:
    print(result)
