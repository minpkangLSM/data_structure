init = input()
new = init
cycle_len = 0
while True :
    if len(new)==1:
        new=new.zfill(2)
    add = str(int(new[0]) + int(new[1]))
    new = new[-1]+add[-1]
    cycle_len += 1
    if int(new)==int(init) : break
print(cycle_len)