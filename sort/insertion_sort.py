# Insertion-sort : 21.09.26.
# Descending
unsorted = [5, 1, 4, 2, 3]
for i in range(1, len(unsorted)):
    key = unsorted[i]
    for j in range(i-1, -2, -1):
        if j==-1 : break # 삽입 대상이 가장 작다는 의미.
        if unsorted[j] < key : break
        unsorted[j+1] = unsorted[j]
    unsorted[j+1] = key
print(unsorted)

# Ascending
for i in range(1, len(unsorted)):
    key = unsorted[i]
    for j in range(i-1, -2, -1):
        if j==-1:break
        if unsorted[j]>key:break
        unsorted[j+1] = unsorted[j]
    unsorted[j+1] = key
print(unsorted)