def max_absolute_difference(t, test_cases):
    results = []

    for _ in range(t):
        n, weights = test_cases[_]
        
        # Sort the weights in descending order
        weights.sort(reverse=True)

        max_diff = 0

        for k in range(1, n + 1):
            # Calculate the total weights for the first k * i boxes
            total_first_part = sum(weights[:k * (n // k)])

            # Calculate the total weights for the remaining boxes
            total_remaining = sum(weights[k * (n // k):])

            # Calculate the absolute difference
            diff = abs(total_first_part - total_remaining)

            # Update the maximum absolute difference
            max_diff = max(max_diff, diff)

        results.append(max_diff)

    return results

# Input processing
t = int(input())
test_cases = []

for _ in range(t):
    n = int(input())
    weights = list(map(int, input().split()))
    test_cases.append((n, weights))

# Get the results
results = max_absolute_difference(t, test_cases)

# Print the results
for result in results:
    print(result)
