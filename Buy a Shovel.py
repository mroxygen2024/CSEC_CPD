def min_shovels(k, r):
    x = 1
    while True:
        total_cost = k * x
        if total_cost % 10 == 0 or total_cost % 10 == r:
            return x
        x += 1
k, r = map(int, input().split())
print(min_shovels(k, r))
