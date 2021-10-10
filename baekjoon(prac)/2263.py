import sys
sys.setrecursionlimit(10**8)

n = int(input())
inorder = list(map(int, sys.stdin.readline().split()))
postorder = list(map(int, sys.stdin.readline().split()))
pos = [0]*(n+1)

for i in range(n):
    pos[inorder[i]] = i

def preorder(i_start, i_end, p_start, p_end):

    if (i_start > i_end) or (p_start > p_end) : return

    root = postorder[p_end]

    left_num = pos[root]-i_start
    right_num = i_end-pos[root]

    print(root, end=" ")
    preorder(i_start, i_start+left_num-1, p_start, p_start+left_num-1)
    preorder(i_end-right_num+1, i_end, p_end-right_num, p_end-1)

preorder(0, len(inorder)-1, 0, len(postorder)-1)