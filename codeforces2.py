def max_absolute_difference(t, test_cases):
    results = []
    for i in range(t):
        n, weights = test_cases[i]
        weights.sort()

        # Create a prefix sum array
        prefix_sum = [0] * (n + 1)
        for j in range(n):
            prefix_sum[j + 1] = prefix_sum[j] + weights[j]

        # Calculate the maximum absolute difference
        max_diff = 0
        for k in range(1, n):
            diff = abs(prefix_sum[k] - (prefix_sum[n] - prefix_sum[k]))
            max_diff = max(max_diff, diff)

        results.append(max_diff)

    return results

def main():
    t = int(input())  # Number of test cases
    test_cases = []
    
    for _ in range(t):
        n = int(input())  # Number of boxes
        weights = list(map(int, input().split()))  # Weights of the boxes
        test_cases.append((n, weights))
    
    results = max_absolute_difference(t, test_cases)

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
