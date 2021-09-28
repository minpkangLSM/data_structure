class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next


def push(item):
    global top
    global size
    top = Node(item, top)
    size += 1


def pop():
    global top
    global size
    item = top.item
    top = top.next
    size -= 1
    return item


def main(order):
    if order[0] == "push":
        push(order[1])
    elif order[0] == "pop":
        if size == 0:
            print("-1")
        else:
            item = pop()
            print(item)
    elif order[0] == "top":
        if size == 0:
            print("-1")
        else:
            print(top.item)
    elif order[0] == "size":
        print(size)
    elif order[0] == "empty":
        if size == 0:
            print("1")
        else:
            print("0")

n = int(input())
top = None
size = 0
for i in range(n):
    order = input().split()
    main(order)