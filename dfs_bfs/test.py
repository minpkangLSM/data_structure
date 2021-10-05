def merge_sort(array):
    if len(array) == 1: return
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            k += 1
            i += 1
        else:
            array[k] = right[j]
            k += 1
            j += 1

    if i == len(left):
        while j < len(right):
            array[k] = right[j]
            k += 1
            j += 1
    elif j == len(right):
        while i < len(left):
            array[k] = right[j]
            k += 1
            j += 1

    return array


if __name__ == "__main__":
    n, k = map(int, input().split())
    prices = list(map(int, input().split()))
    prices = merge_sort(prices)
    total = 0
    count = 0

    for cost in prices:
        total = total + cost
        if total <= k:
            count += 1
        else:
            break
    print(count)