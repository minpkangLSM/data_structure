import sys
sys.setrecursionlimit(10**9)

n = int(input())
tree = [[] for _ in range(n+1)]
parents = [0]*(n+1)

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(start, tree, parents):
    for idx in tree[start]:
        if parents[idx] == 0:
            parents[idx] = start  # 재귀에서 먼저 들어온 값이 부모가 된다.
            dfs(idx, tree, parents)

dfs(1, tree, parents)

for i in range(2, n+1):
    print(parents[i])