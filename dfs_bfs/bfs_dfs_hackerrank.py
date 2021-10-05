from collections import deque, defaultdict

def bfs(g, s):
    visited = set()
    q = deque([s])
    while q:
        v = q.popleft()
        visited.add(v)
        for adj in g[v]:
            if adj not in visited and adj not in q:
                q.append(adj)
    return visited

def con_components(g):
    visited = set()
    components = []
    for s in g.keys():
        if s not in visited:
            nodes = bfs(g, s)
            visited |= nodes
            components.append(nodes)
    return components

if __name__ == '__main__':
    n = int(input())
    g = defaultdict(list)
    for _ in range(n):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)
    c = con_components(g)
    lens = list(map(len, c))
    print(min(lens), max(lens))