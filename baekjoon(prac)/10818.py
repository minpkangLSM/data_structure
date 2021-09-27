N = int(input())
A = input().split()
max = A[0]
min = A[0]
for i in range(1, N) :
    if int(max)<int(A[i]):max=A[i]
    if int(min)>int(A[i]):min=A[i]
print(max, min)