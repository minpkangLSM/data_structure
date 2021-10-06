class Node :
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

def preorder(tree, item):
    if item != None:
        print(tree[item].item, end="")
        preorder(tree, tree[item].left)
        preorder(tree, tree[item].right)

def inorder(tree, item):
    if item != None:
        inorder(tree, tree[item].left)
        print(tree[item].item, end="")
        inorder(tree, tree[item].right)

def postorder(tree, item):
    if item != None:
        postorder(tree, tree[item].left)
        postorder(tree, tree[item].right)
        print(tree[item].item, end="")

tree = {}
n = int(input())
for _ in range(n):
    item, left, right = input().split()
    if left=="." : left=None
    if right=="." : right=None
    tree[item] = Node(item, left, right)

preorder(tree, "A")
print()
inorder(tree, "A")
print()
postorder(tree, "A")
