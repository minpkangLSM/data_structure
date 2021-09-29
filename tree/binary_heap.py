# binary heap : 21.09.29.
class binary_heap :
    def __init__(self, array):
        self.array = array
        self.num_elem = len(array)-1

    def downheap(self, i):
        while 2*i<=self.num_elem:
            child=2*i
            if child<self.num_elem and self.array[child] > self.array[child+1]:
                child+=1
            if self.array[i] < self.array[child]:
                break
            temp = self.array[i]
            self.array[i] = self.array[child]
            self.array[child] = temp
            i = child

    def upheap(self, j):
        while j>1 and self.array[j] < self.array[j//2]:
            temp = self.array[j//2]
            self.array[j//2] = self.array[j]
            self.array[j] = temp
            j = j//2

    def create_heap(self):
        for idx in range(self.num_elem//2, 0, -1):
            self.downheap(idx)

    def insert(self, key_value):
        self.array.append(key_value)
        self.num_elem += 1
        self.upheap(self.num_elem)

    def delete_min(self):
        if self.num_elem == 0:
            print("EMPTY.")
            return
        min = self.array[1]
        self.array[1] = self.array[-1]
        del self.array[-1]
        self.num_elem -= 1
        self.downheap(1)
        return min

    def print_heap(self):
        for i in range(1, self.num_elem+1):
            print(self.array[i])
        print("SIZE : ", self.num_elem)

if __name__ == "__main__":

    a = [None]
    a.append(90)
    a.append(80)
    a.append(70)
    a.append(20)
    a.append(35)
    a.append(10)
    a.append(15)
    a.append(45)
    a.append(40)
    print(a)
    bh = binary_heap(a)
    bh.print_heap()
    bh.create_heap()
    bh.print_heap()
    bh.insert(7)
    bh.print_heap()
    bh.delete_min()
    bh.print_heap()
    bh.delete_min()
    bh.print_heap()