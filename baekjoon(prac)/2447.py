# 21.09.28. 2447
def star_link(n):
    global star_map
    if n==3:
        for i in range(3):
            for j in range(3):
                if i==1 and j==1 : continue
                star_map[i][j] = 1
        return

    d = n//3
    star_link(n//3)
    for i in range(3):
        for j in range(3):
            if i==1 and j==1: continue
            for k in range(d):
                star_map[i*d+k][j*d:(j+1)*d] = star_map[k][0:d]
n = 243
star_map = [[0 for i in range(n)] for j in range(n)]
star_link(n)
for i in range(len(star_map)):
    for j in range(len(star_map)):
        if star_map[i][j]:
            print('*', end="")
        else :
            print(" ", end="")
    print("\n")