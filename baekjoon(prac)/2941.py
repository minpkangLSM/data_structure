a = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
word = input()
for cro in a :
    word = word.replace(cro, "?")
print(len(word))