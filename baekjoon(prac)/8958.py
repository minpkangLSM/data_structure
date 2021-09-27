N = int(input())
input_list = []
for i in range(N):
    a = input().split("X")
    input_list.append(a)
for sub_list in input_list :
    sum = 0
    for i in sub_list :
        sum += len(i)*(len(i)+1)/2
    print(int(sum))