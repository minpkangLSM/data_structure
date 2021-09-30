class binary_heap:
    def __init__(self, arr):
        self.arr = arr
        self.size = len(arr) - 1

    def insert(self, item):
        self.arr.append(item)
        self.size += 1
        self.upheap(self.size)

    def maximum(self):
        if self.size == 0:
            return 0
        maximum = self.arr[1]
        self.arr[1] = self.arr[-1]
        del self.arr[-1]
        self.size -= 1
        self.downheap(1)
        return maximum

    def upheap(self, j):
        while j > 1 and self.arr[j // 2] < self.arr[j]:
            temp = self.arr[j // 2]
            self.arr[j // 2] = self.arr[j]
            self.arr[j] = temp
            j = j // 2

    def downheap(self, i):
        while 2 * i <= self.size:
            child = 2 * i
            if child < self.size and self.arr[child] < self.arr[child + 1]:
                child += 1
            if self.arr[child] < self.arr[i]: break
            temp = self.arr[i]
            self.arr[i] = self.arr[child]
            self.arr[child] = temp
            i = child


n = int(input())
arr = [None] * 1
bh = binary_heap(arr)

for i in range(n):
    v = int(input())
    if v == 0:
        print(bh.maximum())
    else:
        bh.insert(v)