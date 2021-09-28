class SList :
    # base node
    class Node :
        def __init__(self, item, link):
            self.item = item
            self.next = link

    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self): return self.size==0
    def size(self): return self.size

    # Insertion
    def insert_front(self, item):
        if self.is_empty():
            self.head = self.Node(item, None)
        else:
            self.head = self.Node(item, self.head)
        self.size+=1

    def insert_after(self, item, p):
        p.next = self.Node(item, p.next)
        self.size+=1

    # Removal
    def remove_front(self):
        if self.is_empty():
            raise EmptyError
        else :
            self.head = self.head.next
            self.size-=1

    def remove_after(self, p):
        if self.is_empty():
            raise EmptyError
        t = p.next
        p.next = t.next
        self.size -= 1

    # search
    def search(self, target):
        p = self.head
        for i in range(self.size):
            if target==p.item : return i
            p = p.next
        return None

    def print_list(self):
        p = self.head
        while p :
            if p.next != None :
                print(p.item,"-> ", end="")
            else :
                print(p.item)
            p = p.next

class EmptyError(Exception):
    pass

if __name__ == "__main__" :
    s = SList()
    s.insert_front("orange")
    s.insert_front("apple")
    s.insert_after("cherry", s.head.next)
    s.insert_front("pear")
    s.print_list()
    s.remove_after(s.head)
    s.print_list()