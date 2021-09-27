a = input()
b = input()
total = 0
for idx, sub_b in enumerate(b[::-1]):
    print(a, sub_b)
    result = eval(a+"*"+sub_b)
    total += result*(10**(idx))
    print(result)
print(total)