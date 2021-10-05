import sys

n = int(input())
city_map = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
print(city_map)
print(visited)
print(city_map[0][0])