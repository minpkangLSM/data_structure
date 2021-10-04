# 21.09.30 1920
import sys

class Node:
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right
class bs:
    def __init__(self):
        self.root = None

    def insert(self, item):
        self.root = self.insert_sub(self.root, item)

    def insert_sub(self, node, item):
        if node == None:
            return Node(item)
        if node.item > item :
            node.left = self.insert_sub(node.left, item)
        elif node.item < item :
            node.right = self.insert_sub(node.right, item)
        else :
            node.item = item
        return node

    def search(self, target):
        return self.search_sub(self.root, target)

    def search_sub(self, node, target):
        if node==None:
            return 0
        if node.item == target:
            return 1
        if node.item > target :
            return self.search_sub(node.left, target)
        elif node.item < target :
            return self.search_sub(node.right, target)

bs = bs()
n1 = int(input())
n_list1 = list(map(int, input().split()))
for i in range(n1):
    bs.insert(n_list1[i])

n2 = int(input())
n_list2 = list(map(int, input().split()))
for i in range(n2):
    print(bs.search(n_list2[i]))