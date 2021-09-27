# Selection sort : 21.09.26.
# Descending
unsorted = [5, 1, 4, 2, 3]
for i in range(len(unsorted)-1):
    least = i
    for j in range(i+1, len(unsorted)):
        if unsorted[least] > unsorted[j] : least = j # find index of least number
    temp = unsorted[i]
    unsorted[i] = unsorted[least]
    unsorted[least] = temp
print(unsorted)

# Ascending
for i in range(0, len(unsorted)-1):
    biggest = i
    for j in range(i+1, len(unsorted)):
        if unsorted[j] > unsorted[biggest] : biggest=j
    temp = unsorted[i]
    unsorted[i] = unsorted[biggest]
    unsorted[biggest] = temp
print(unsorted)