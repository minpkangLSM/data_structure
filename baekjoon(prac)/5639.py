#21.10.09 : RuntimeError
# class Node:
# #     def __init__(self, item, left=None, right=None):
# #         self.item = item
# #         self.left = left
# #         self.right = right
# #
# # class bst:
# #     def __init__(self):
# #         self.root = None
# #
# #     def input(self, target):
# #         self.root = self.input_item(self.root, target)
# #     def input_item(self, node, target):
# #         if node==None:
# #             return Node(target)
# #         elif node.item > target:
# #             node.left = self.input_item(node.left, target)
# #         elif node.item < target:
# #             node.right = self.input_item(node.right, target)
# #         return node
# #
# #     def postorder(self, node):
# #         if node!=None:
# #             self.postorder(node.left)
# #             self.postorder(node.right)
# #             print(node.item)
# #
# # preorder = []
# # while True :
# #     try:
# #         preorder.append(int(input()))
# #     except:
# #         break
# #
# # bst = bst()
# # for factor in preorder:
# #     bst.input(factor)
# #
# # bst.postorder(bst.root)

import sys
sys.setrecursionlimit(10**6)

def postorder(start, end):

    if start > end :
        return
    root = preorder[start]
    idx = start+1
    while idx <= end:
        if preorder[idx] > root :
            break
        idx+=1
    #left subtree
    postorder(start+1, idx-1)
    #right subtree
    postorder(idx, end)
    print(root)

preorder = []
while True :
    try:
        preorder.append(int(input()))
    except:
        break
postorder(0, len(preorder)-1)