class DList :
    class Node :
        def __init__(self, item, prev, next):
            self.item = item
            self.prev = prev
            self.next = next

    def __init__(self):
        self.head = self.Node(None, None, None)
        self.tail = self.Node(None, self.head, None)
        self.head.next = self.tail
        self.size += 1

    def size(self):return self.size()
    def is_empty(self):return self.size==0

    def insert_before(self, item, p):
        t = p.prev
        n = self.Node(item, t, p)
        t.next = n
        p.prev = n
        self.size += 1

    def insert_after(self, item, p):
        t = p.next
        n = self.Node(item, p, t)
        t.prev = n
        p.next = n
        self.size += 1

    def delete(self, x):
        f = x.prev
        r = x.next
        f.next = r
        r.prev = f
        self.size -= 1
        return x.item

    def print_list(self):
        if self.is_empty():
            raise EmptyError
        else :
            p = self.head
            while p != self.tail:
                if p.next != self.tail:
                    print(p.item, "<=>", end="")
                else:
                    print(p.item)
                p = p.next

class EmptyError(Exception):
    pass