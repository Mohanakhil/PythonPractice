t = int(input())
for i in range(t):
    x, y = map(int, input().split())
    if (x * 2) > (y * 5):
        print("Chocolate\n")
    elif (y * 5) > (x * 2):
        print("Candy\n")
    else:
        print("Either\n")
