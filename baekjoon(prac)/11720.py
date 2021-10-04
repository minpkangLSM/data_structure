sum = 0
n = int(input())
num = list(map(int, input()))
for i in range(n):
    sum += num[i]

print(sum)