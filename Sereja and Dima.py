n = int(input())
l = list(map(int, input().split()))

Sereja = 0
Dima = 0
left = 0
right = n - 1
turn = 0  # 0 for Sereja, 1 for Dima

while left <= right:
    if l[left] >= l[right]:
        chosen = l[left]
        left += 1
    else:
        chosen = l[right]
        right -= 1

    if turn % 2 == 0:
        Sereja += chosen  
    else:
        Dima += chosen  
    
    turn += 1

print(Sereja, Dima)