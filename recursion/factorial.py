# Recursion : 21.09.27.
def factorial(n):
    if n<=0 : return 1
    else : return n*factorial(n-1)

def factorial_for(n):
    f = 1
    for i in range(n):
        f *= (i+1)
    return f
print(factorial(5))
print(factorial_for(5))