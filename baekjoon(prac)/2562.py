max_num = 0
max_idx = -1
for i in range(9):
    a = int(input())
    if a >= max_num :
        max_num = a
        max_idx=i+1
print(max_num, max_idx)