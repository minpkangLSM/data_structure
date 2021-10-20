# 21.10.21. DP : Memoization

MAX = 21
memoization = [[MAX*[0] for _ in range(MAX)] for _ in range(MAX)]

def w(a,b,c):

    if a <= 0 or b <= 0 or c <= 0 :
        return 1
    elif a > 20 or b > 20 or c > 20 :
        return w(20, 20, 20)

    if memoization[a][b][c] :
        return memoization[a][b][c]

    if a < b < c :
        memoization[a][b][c]=w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return memoization[a][b][c]

    memoization[a][b][c]=w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return memoization[a][b][c]

while True :
    a, b, c = map(int, input().split())
    if a==-1 and b==-1 and c==-1:
        break
    results = w(a, b, c)
    print("w({0}, {1}, {2}) = {3}".format(a, b, c, results))