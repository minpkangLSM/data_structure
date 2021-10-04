import sys

class b_heap:
    def __init__(self, arr):
        self.arr = arr
        self.num_elem = len(arr) - 1

    def insert(self, i):
        self.arr.append(i)
        self.num_elem += 1
        self.upheap(self.num_elem)

    def upheap(self, i):
        while i > 1:
            if self.arr[i] > self.arr[i // 2]: break
            temp = self.arr[i // 2]
            self.arr[i // 2] = self.arr[i]
            self.arr[i] = temp
            i = i//2

    def delete(self):
        if self.num_elem==0:
            return 0
        min = self.arr[1]
        self.arr[1] = self.arr[-1]
        del self.arr[-1]
        self.num_elem -= 1
        self.downheap(1)
        return min

    def downheap(self, i):
        while (2 * i <= self.num_elem):
            child = 2 * i
            if child < self.num_elem and self.arr[child] > self.arr[child + 1]:
                child += 1
            if self.arr[child] > self.arr[i]: break
            temp = self.arr[child]
            self.arr[child] = self.arr[i]
            self.arr[i] = temp
            i = child


n = int(input())
arr = [None] * 1
bh = b_heap(arr)

for _ in range(n):
    a = int(sys.stdin.readlin())
    if a == 0:
        print(bh.delete())
    else:
        bh.insert(a)