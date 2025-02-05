n = int(input())  
magnet_orientation = [input().strip() for _ in range(n)] 

groups = 1  


for i in range(1, n):
    if magnet_orientation[i] != magnet_orientation[i - 1]:
        groups += 1

print(groups)
