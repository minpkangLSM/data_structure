import sys

adj_list = [[2,1], [3,0], [3,0], [9,8,2,1],
            [5], [7,6,4], [7,5], [6,5], [3],[3]]
N = len(adj_list)
visited = [False]*N

def dfs(start):
    visited[start] = True
    print(start, ' ', end=' ')
    for i in adj_list[start]:
        if not visited[i] : dfs(i)