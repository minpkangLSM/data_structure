# 21.10.11.
import sys
from collections import defaultdict

link = defaultdict(list)

n = int(input())
for _ in range(n):
    info = list(map(int, sys.stdin.readline().split()))
    for idx in range(1, len(info)-2, 2):
        link[info[0]].append([info[idx], info[idx+1]])

def bfs(start):
    global n
    q = []
    length = [0 for _ in range(n+1)]
    q.append(start)
    while len(q)!=0 :
        v = q.pop(0)
        for node, weight in link[v]:
            if length[node] == 0 :
                length[node] = length[v] + weight
                q.append(node)
    return length

length = bfs(1)
length[1] = 0
length = bfs(length.index(max(length)))
length[length.index(max(length))] = 0
print(max(length))