from collections import defaultdict

def bfs(start):
    index = True
    q = []
    q.append(start)
    visited[start]=True
    while len(q) != 0:
        v = q.pop(0)
        for n in linked[v]:
            if n in q : index = False
            if not visited[n]:
                q.append(n)
                visited[n]=True
    return index

case = 0
while True :
    case += 1
    n, m = map(int, input().split())
    if n==0 and m==0 : break
    visited = [False for _ in range(n + 1)]
    linked = defaultdict(list)
    for i in range(m):
        a, b = map(int, input().split())
        linked[a].append(b)
        linked[b].append(a)

    count = 0
    for i in range(1, n+1):
        if not visited[i] :
            ind = bfs(i)
            if ind :
                count += 1
            else:
                pass
    if count==0 :
        print("Case {0}: No trees.".format(case))
    elif count==1:
        print("Case {0}: There is one tree.".format(case))
    else:
        print("Case {0}: A forest of {1} trees.".format(case, count))