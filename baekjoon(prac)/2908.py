nums = input().split()
for i in range(len(nums[0])-1, -1, -1):
    if int(nums[0][i]) > int(nums[1][i]) :
        for j in range(2,-1,-1) : print(nums[0][j], end="")
        break
    elif int(nums[0][i]) < int(nums[1][i]):
        for j in range(2, -1, -1): print(nums[1][j], end="")
        break
    else : continue