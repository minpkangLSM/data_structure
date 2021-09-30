# 21.09.30 : bst(binary_search_tree)
class Node:
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

class bst:
    def __init__(self):
        self.root = None

    # searching item
    def get(self, target):
        return self.get_item(self.root, target)
    def get_item(self, node, target):
        if node==None:
            return None
        elif node.item > target:
            return self.get_item(node.left, target)
        elif node.item < target:
            return self.get_item(node.right, target)
        else:
            return node.item

    # searching min
    def min(self):
        if self.root == None:
            return None
        return self.minimum(self.root)
    def minimum(self, node):
        if node.left==None:
            return node
        return self.minimum(node.left)

    # input item
    def input(self, item):
        self.root = self.input_item(self.root, item)
    def input_item(self, node, item):
        if node==None:
            return Node(item)
        elif node.item > item:
            node.left = self.input_item(node.left, item)
        elif node.item < item:
            node.right = self.input_item(node.right, item)
        else:
            node.item = item
        return node

    # delete min
    def delete_min(self):
        self.root = self.del_min(self.root)
    def del_min(self, node):
        if node.left==None:
            return node.right
        else:
            node.left = self.del_min(node.left)
        return node

    # delete
    def delete(self, item):
        self.root = self.del_item(self.root, item)
    def del_item(self, node, item):
        if node==None:
            return None
        elif node.item > item :
            node.left = self.del_item(node.left, item)
        elif node.item < item:
            node.right = self.del_item(node.right, item)
        else:
            if node.right==None:
                return node.left
            if node.left==None:
                return node.right
            target = node
            node = self.minimum(target.right)
            node.right = self.del_min(target.right)
            node.left = target.left
        return node

    def inorder(self, node):
        if node!=None:
            if node.left:
                self.inorder(node.left)
            print(node.item)
            if node.right:
                self.inorder(node.right)

if __name__ == "__main__":
    bst = bst()
    bst.input(10)
    bst.input(100)
    bst.input(50)
    bst.input(150)
    bst.input(20)
    bst.input(40)
    #bst.inorder(bst.root)
    bst.delete(40)
    bst.inorder(bst.root)
