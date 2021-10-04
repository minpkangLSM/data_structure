import sys

adj_list = [[2,1], [3,0], [3,0], [9,8,2,1],
            [5], [7,6,4], [7,5], [6,5], [3],[3]]
N = len(adj_list)
visited = [False]*N

def bfs(start):
    q=[]
    q.append(start)
    visited[start]=True
    print(start, ' ', end="")
    while len(q) > 0 :
        t = q.pop(0)
        for i in adj_list[t]:
            if not visited[i] :
                q.append(i)
                visited[i] = True
                print(i, ' ', end="")

if __name__ == "__main__":
    for i in range(N):
        if not visited[i]:
            bfs(i)