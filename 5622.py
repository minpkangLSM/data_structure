words = input()
total = 0
base = ord("A")
time = [3, 3, 3, 4, 4,
        4, 5, 5, 5, 6,
        6, 6, 7, 7, 7,
        8, 8, 8, 8, 9,
        9, 9, 10, 10, 10, 10]
for word in words :
    num_asci = ord(word) - base
    total += time[num_asci]

print(total)