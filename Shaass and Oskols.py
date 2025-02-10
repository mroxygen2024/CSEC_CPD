n = int(input())  
a = list(map(int, input().split()))  
m = int(input())
for _ in range(m):
    xi, yi = map(int, input().split())
    xi -= 1  
    left = yi - 1
    right = a[xi] - yi
    if xi > 0:  
        a[xi - 1] += left
    if xi < n - 1:  
        a[xi + 1] += right
    a[xi] = 0  
for birds in a:
    print(birds)