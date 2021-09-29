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
        size = -1
    else:
        item = top.item
        top = top.next
        size -= 1
        return item


p_dict = {")":"("}
k = int(input())
for _ in range(k):

    top = None
    size = 0

    p_set = input()
    switch=False
    for p_sub in p_set:
        if p_sub in p_dict.values():
            push(p_sub)
        else:
            pop()
            if size < 0:
                switch=True
                break
    if switch :
        print("NO")
    elif size!=0:
        print("NO")
    elif size==0:
        print("YES")