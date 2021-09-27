# Recursion(pow) : 21.09.27.
def pow(x, n):
    if n==0 : return 1
    elif n%2==0: return pow(x*x, n//2)
    elif n%2==1: return x*pow(x*x, (n-1)//2)

def remains(x, n, d):
    if n==1 :
        return x%d
    else:
        temp = remains(x, n//2, d)
        if n%2==0:
            return temp*temp%d
        else :
            return temp*temp*x%d
