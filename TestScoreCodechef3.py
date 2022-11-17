t = int(input())
while t > 0:
    n, x, y = map(int, input().split())
    if y % x == 0 and y / x <= n:
        print("YES")
    else:
        print("NO")
    t = t - 1
