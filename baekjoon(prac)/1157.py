word = input()
count = [0]*26
base = ord("A")
max = 0
switch = False

for i in word:
    asci = ord(i)
    if asci >= 97 and asci <=122 :
        asci -= 32
    count[asci-base] += 1

for i in range(26) :
    if max != 0 and max == count[i] :
        switch = False
    elif max < count[i] :
        max = count[i]
        idx = i
        switch = True

if not switch : print("?")
else : print(chr(base+idx))