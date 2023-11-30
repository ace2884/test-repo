def game_winner(n):
    # Check if the current integer is divisible by 3
    if n % 3 == 0:
        return "First"
    
    # If not divisible by 3, calculate the remaining moves
    remaining_moves = 10 - (n % 3 + 2) // 3
    
    # If there are an even number of remaining moves, Vova wins; otherwise, Vanya wins
    if remaining_moves % 2 == 0:
        return "Second"
    else:
        return "First"

def main():
    t = int(input())  # Number of test cases
    for _ in range(t):
        n = int(input())  # Integer for each test case
        result = game_winner(n)
        print(result)

if __name__ == "__main__":
    main()
