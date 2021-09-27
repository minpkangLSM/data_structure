multi = 1
count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(3):
    a = int(input())
    multi *= a
for num in str(multi):
    count[int(num)] += 1
for i in count :
    print(i)