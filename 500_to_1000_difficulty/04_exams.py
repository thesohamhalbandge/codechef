t = int(input())

for i in range(t):
    x, y, z = map(int, input().split())
    # print(x, y, z)
    if (z > (x * y / 2)):
        print("YES")
    else:
        print("NO")