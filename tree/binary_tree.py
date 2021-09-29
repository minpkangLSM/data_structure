# Tree : binary tree, 21.09.29.
class qNode :
    def __init__(self, item, next):
        self.item = item
        self.next = next

def insert(item):
    global front
    global rear
    global size
    node = qNode(item, None)
    if size==0:
        front = node
    else:
        rear.next = node
    rear = node
    size+=1

def remove():
    global front
    global rear
    global size
    if size!=0:
        item = front.item
        front = front.next
        size-=1
        if size==0:
            rear=None
        return item

class Node:
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

class binary_tree:
    def __init__(self):
        self.root = None
    # preorder : VLR, memory stack(recursion)
    def preorder(self, n):
        if n!=None:
            print(str(n.item)) # Visit
            if n.left: # left
                self.preorder(n.left)
            if n.right:
                self.preorder(n.right)
    # inorder : LVR, memory stack(recursion)
    def inorder(self, n):
        if n!=None:
            if n.left:
                self.inorder(n.left)
            print(str(n.item))
            if n.right:
                self.inorder(n.right)
    # postorder : LRV, memory stack(recursion)
    def postorder(self, n):
        if n!=None:
            if n.left:
                self.postorder(n.left)
            if n.right:
                self.postorder(n.right)
            print(str(n.item))
    # levelorder : queue(no memory stack) but dynamic memory allocation.
    def levelorder(self, n):
        q=[]
        q.append(n)
        while len(q)!=0:
            t = q.pop(0)
            print(str(t.item))
            if t.left!=None:
                q.append(t.left)
            if t.right!=None:
                q.append(t.right)

    # levelorder : queue(no memory stack, no dynamic memory allocation
    def levelorder_q(self, root):
        global front
        global rear
        global size
        insert(root)
        while size!=0:
            t = remove()
            print(str(t.item))
            if t.left:
                insert(t.left)
            if t.right:
                insert(t.right)

    def height(self, root):
        if root == None:
            return 0
        return max(self.height(root.left), self.height(root.right))+1

if __name__ == "__main__":
    t = binary_tree()
    front = None
    rear = None
    size = 0

    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)

    t.root = n1
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7

    t.levelorder(t.root)