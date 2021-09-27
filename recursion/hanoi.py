# Recursion(hanoi) : 21.09.27.
def hanoi(n, fr, te, to):
    if n==1 :
        print("{0} {1}".format(fr, to))

    else :
        hanoi(n-1, fr, to, te)
        print("{0} {1}".format(fr, to))
        hanoi(n-1, te, fr, to)
hanoi(3, "1", "2", "3")