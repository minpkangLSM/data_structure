n = int(input())
word_list = []
count = 0
for i in range(n):
    word_list.append(input())

for word in word_list:
    check_list = []
    s = False
    for idx, alpha in enumerate(word):
        if idx == 0 :
            check_list.append(alpha)
            continue
        if alpha == word[idx-1] : continue
        else :
            if alpha in check_list :
                s = True
                break
            else :
                check_list.append(alpha)

    if s : continue
    else :
        count += 1

print(count)