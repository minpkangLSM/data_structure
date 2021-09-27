a, b = map(int, input().split())
b -= 45
if b > 0 : print(a, b)
elif a > 0 : print(a-1, b+60)
elif a == 0 : print(23, b+60)