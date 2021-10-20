# 21.10.20.
import sys
sys.setrecursionlimit(10**8)

case = int(input())
y_val = [2, 2, -2, -2, -1, 1, -1, 1]
x_val = [-1, 1, -1, 1, 2, 2, -2, -2]

def bfs(start, target):
    q = []
    count = 0
    q.append(start)
    visited[start[0]][start[1]] = True
    if start == target : return 0
    while len(q) != 0 :
        length = len(q)
        for _ in range(length):
            v = q.pop(0)
            for idx in range(len(y_val)):
                new_y = v[0] + y_val[idx]
                new_x = v[1] + x_val[idx]
                if new_y >= 0 and new_y <= size-1 and new_x >= 0 and new_x <= size-1:
                    if not visited[new_y][new_x] :
                        if [new_y, new_x] == target :
                            count+=1
                            return count
                        q.append([new_y, new_x])
                        visited[new_y][new_x] = True

        count += 1

    return -1

for _ in range(case):

    size = int(input())
    visited = [[False for _ in range(size)] for _ in range(size)]
    start = list(map(int, input().split()))
    target = list(map(int, input().split()))

    count = dfs(start, target, 0)
    # count = bfs(start, target)
    print(count)