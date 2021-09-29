import sys

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
    if size == 0:
        return
    top = top.next
    size -= 1

def total_sum():
    global top
    global size
    if size == 0:
        return 0
    else:
        sum = 0
        p = top
        while p:
            item = p.item
            sum += item
            p = p.next
        return sum

k = int(input())
top = None
size = 0
for _ in range(k):
    n = int(sys.stdin.readline())
    if n == 0:
        pop()
    else:
        print(n)
        push(n)
sum = total_sum()
print(sum)


