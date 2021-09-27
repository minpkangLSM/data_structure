N, X = map(int, input().split())
A = input().split()
print(A)
print(filter(lambda x : int(x) < X, A))