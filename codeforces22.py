import sys

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        weights = list(map(int, sys.stdin.readline().split()))
        max_diff = 0
        for k in range(1, n + 1):
            truck_loads = [weights[i:i + k] for i in range(0, n, k)]
            truck_weights = list(map(sum, truck_loads))
            diff = max(truck_weights) - min(truck_weights)
            max_diff = max(max_diff, diff)
        print(max_diff)

if _name_ == "_main_":
    main()
