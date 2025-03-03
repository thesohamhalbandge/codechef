t = int(input())
for i in range(t):
    n, x = map(int, input().split())
    if n < 6:
        subs_no = 1
    elif n % 6 == 0:
        subs_no = n // 6
    else:
        subs_no = (n // 6) + 1
    print(subs_no * x)