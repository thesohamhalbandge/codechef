N = int(input())
arr = list(map(int, input().split()))

even_count = sum(1 for i in arr if i % 2 == 0)

if even_count > (N - even_count):  
    print("READY FOR BATTLE")
else:
    print("NOT READY")