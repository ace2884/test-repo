for _ in range(int(input())):
    x=int(input())
    if ((x+1)%3==0)or((x-1)%3==0):
        print("First")
    else:
        print("Second")
