n = int(input())  # Number of magnets
magnet_orientation = [input().strip() for _ in range(n)]  # List to store the magnet orientations

groups = 1  # At least one group exists because there is at least one magnet

# Traverse through the magnet orientations and count the groups
for i in range(1, n):
    if magnet_orientation[i] != magnet_orientation[i - 1]:
        groups += 1

print(groups)