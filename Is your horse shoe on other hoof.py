colors = list(map(int, input().split()))
distinct_colors = len(set(colors))
print(4 - distinct_colors)