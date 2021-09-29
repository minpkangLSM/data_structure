class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

def push(item):
    global top
    global size
    top = Node(item, top)
    size+=1

def pop():
    global top
    global size
    top = top.next
    size-=1

def top_item():
    global top
    return top.item

n = int(input())
arr = list(map(int, input().split()))
res = [-1]*len(arr)
top = None
size = 0

for i in range(n):
    while size!=0 and arr[i]>arr[top_item()]:
        res[top_item()] = arr[i]
        pop()
    push(i)
for i in range(n) : print(res[i])