# Recursion(Fibonacci) : 21.09.27.
def fibonacci(n):
    if n==0 or n==1: return n
    else : return fibonacci(n-1)+fibonacci(n-2)

def fibonacci_for(n):
    if n<2 : return n
    else:
        temp=0
        current=1
        last=0
        for i in range(2, n+1):
            temp = current
            current = current+last
            last = temp
    return current
print(fibonacci_for(17))