n = int(input())
l = list(map(int, input().split()))

untreated = 0
police = 0  

for i in range(n):
    if l[i] == -1:  
        if police > 0:
            police -= 1  
        else:
            untreated += 1
    else:
        police += l[i]

print(untreated)
