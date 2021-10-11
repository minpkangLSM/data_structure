# 2021.10.12.
fibo_dp = []
for n in range(0, 41):
    if n==0:
        fibo_dp.append(n)
    elif n==1:
        fibo_dp.append(n)
    elif n==2:
        fibo_dp.append(1)
    else:
        fibo_dp.append(fibo_dp[n-2]+fibo_dp[n-1])

def f_dp(num):
    if num==0 :
        print(1, 0)
    elif num==1:
        print(0, 1)
    else:
        print(fibo_dp[num-1], fibo_dp[num])

n = int(input())
tc = []
for _ in range(n):
    tc.append(int(input()))

for i in tc :
    f_dp(i)

