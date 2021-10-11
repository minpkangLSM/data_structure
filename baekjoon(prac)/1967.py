# 21.10.11.
import sys
from collections import defaultdict

n = int(input())
link = defaultdict(list)
for _ in range(n-1):
    a, b, w = map(int, sys.stdin.readline().split())
    link[a].append([b, w])
    link[b].append([a, w])

def bfs(start):
    global n
    length = [0 for _ in range(n + 1)]
    q = []
    q.append(start)
    while len(q)!=0:
        v = q.pop(0)
        for x, w in link[v]:
            if length[x] == 0 :
                length[x] = length[v] + w
                q.append(x)
    return length

length = bfs(1)
length[1] = 0
max_index = length.index(max(length))
length = bfs(max_index)
length[max_index] = 0
print(max(length))