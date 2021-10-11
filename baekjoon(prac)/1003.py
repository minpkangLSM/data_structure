# 2021.10.12.
import sys
n = int(input())

fibo_dp = []
for n in range(0, 40):
    if n == 0:
        fibo_dp.append(n)
    elif n == 1 :
        fibo_dp.append(n)
    elif n == 2:
        fibo_dp.append(1)
    else :
        fibo_dp.append(fibo_dp[n-2]+fibo_dp[n-1])

for _ in range(n):

    test_case = int(sys.stdin.readline())
    def f_dp(n):
        if n==0 :
            print(1, 0)
            return
        elif n==1 :
            print(0, 1)
            return
        else :
            print(fibo_dp[n-2], fibo_dp[n])
            return
    f_dp(test_case)

