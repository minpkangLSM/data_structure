# counting sort : 21.09.27.
def counting_sort(A, B, M):
    C = [0]*(M+1)
    for i in A:
        C[i] += 1
    for i in range(1, len(C)):
        C[i] += C[i-1]
    for i in range(len(A)-1, -1, -1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1
    return B
A = [0, 1, 4, 2, 3, 3, 0]
B = [-1]*len(A)
M=4
# s = counting_sort(A, B, M)
# print(s)
