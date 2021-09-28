# bracket paring : 21.09.28.
# bracket_dict = {")" : "(", "]" : "[", "}" : "{"}
# a = "{[]}[]()(({[]})){}{}()([])"
# b = "{[[])}"
#
# def push(stack, item):
#     return stack.append(item)
#
# def pop(stack):
#     if len(stack)!=0:
#         top = stack.pop(-1)
#         return top
#     else:
#         return None
#
# stack = []
# for i in b :
#     if i in bracket_dict.values():
#         stack.append(i)
#     else :
#         if bracket_dict[i]==stack.pop(-1):pass
#         else:
#             break
#
# if len(stack) == 0 : print("Pass")
# else : raise SyntaxError("Syntax")

# Palindrome : 21.09.28.
pal = "RACECAR"
stack = []
def palindrome(pal):
    mid = (len(pal)-1)/2
    for idx, letter in enumerate(pal) :
        if idx < mid :
            stack.append(letter)
        elif idx > mid :
            if letter == stack.pop(-1) : pass
            else : raise SyntaxError
        elif idx == mid : pass
    print("PASS")
palindrome(pal)