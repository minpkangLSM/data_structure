n = int(input())
data_list = []
for i in range(n):
    data_list.append(input().split())

for i in range(n):
    data_sub = data_list[i]
    for j in data_sub[1]:
        print(j*int(data_sub[0]), end="")
    print("")