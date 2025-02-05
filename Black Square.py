a = list(map(int, input().split()))
s = input()

total = sum(a[int(c) - 1] for c in s)
print(total)
