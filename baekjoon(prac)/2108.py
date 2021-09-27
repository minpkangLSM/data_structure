def merge_sort(array):
    if len(array) == 1:
        return array
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
            k += 1
        elif left[i] >= right[j]:
            array[k] = right[j]
            j += 1
            k += 1
    if i == len(left):
        while j < len(right):
            array[k] = right[j]
            k += 1
            j += 1
    elif j == len(right):
        while i < len(left):
            array[k] = left[i]
            k += 1
            i += 1
    return array


N = int(input())
int_list = []
count_list = [0] * 8001
for _ in range(N):
    a = int(input())
    int_list.append(a)
    if a == 0:
        count_list[4000] += 1
    elif a < 0:
        count_list[(a * -1) - 1] += 1
    else:
        count_list[a + 4000] += 1

    # mean
sum = 0
for elem in int_list:
    sum += elem
mean = round(sum / len(int_list))
print(mean)
# mid
arr = merge_sort(int_list)
mid = arr[len(arr) // 2]
print(mid)
# mode
mode_num = max(count_list)
mode_list = []
for i in range(len(count_list)):
    if count_list[i] == mode_num:
        mode_list.append(i)

if len(mode_list) == 1:
    if mode_list[0] <= 4000:
        print(-(mode_list[0] + 1))
    else:
        print(mode_list[0] - 4000)
else :
    if mode_list[1] <= 4000:
        print(-(mode_list[1] + 1))
    else:
        print(mode_list[1] - 4000)

# range
print(arr[-1] - arr[0])