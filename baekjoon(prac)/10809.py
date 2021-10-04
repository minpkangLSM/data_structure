a = input()
l = len(a)
count = [-1]*26
base = ord("a")

for i in range(l):
    asci = ord(a[i])
    if count[asci-base] == -1:
        count[asci-base] = i

for i in range(26) : print("{0} ".format(count[i]), end="")