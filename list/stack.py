# Simple version : Python list
def push(stack, item):
    stack.append(item)
    return stack

def peek(stack):
    if len(stack)!=0:
        return stack[-1]

def pop(stack):
    if len(stack)!=0:
        item = stack.pop(-1)
        return item

# stack = []
# stack = push(stack, "apple")
# stack = push(stack, "orange")
# stack = push(stack, "cherry")
# pe = peek(stack)
# po = pop(stack)
# print(po)
# pe = peek(stack)
# print(pe)

# Singlylinkedlist
class Node :
    def __init__(self, item, next):
        self.item = item
        self.next = next

def push(item):
    global top
    global size
    top = Node(item, top)
    size += 1

def peek():
    if size != 0:
        return top.item

def pop():
    global top
    global size
    if size!=0:
        top_item = top.item
        top = top.next
        size -= 1
        return top_item

def print_stack():
    p = top
    while p:
        if p.next!=None:
            print(p.item,"->",end="")
        else:
            print(p.item)
        p = p.next

top = None
size = 0
push("apple")
push("oragne")
push("cherry")
print_stack()
pop()
print_stack()