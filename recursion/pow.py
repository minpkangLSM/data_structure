# Recursion(pow) : 21.09.27.
def pow(x, n):
    if n==0 : return 1
    elif n%2==0: return pow(x*x, n//2)
    elif n%2==1: return x*pow(x*x, (n-1)//2)
