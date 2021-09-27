# Bubble sort : 21.09.26.
# Descending
unsorted = [5, 1, 4, 2, 3]
for i in range(len(unsorted)-1, 0, -1):
    for j in range(0, i):
        if unsorted[j] > unsorted[j+1]:
            temp = unsorted[j]
            unsorted[j] = unsorted[j+1]
            unsorted[j+1] = temp

# Ascending
unsorted = [2, 5, 1, 6, 3, 4]
for i in range(len(unsorted)-1, 0, -1):
    for j in range(0, i):
        if unsorted[j] < unsorted[j+1] :
            temp = unsorted[j+1]
            unsorted[j+1] = unsorted[j]
            unsorted[j] = temp
print(unsorted)