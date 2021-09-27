re_list = []
for i in range(10):
    a = int(input())
    re_num = a%42
    if re_num not in re : re_list.append(re_num)
print(len(re))