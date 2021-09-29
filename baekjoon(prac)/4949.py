# baekjoon : 21.09.29.
class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

def push(item):
    global top
    global size
    top = Node(item, top)
    size += 1

def pop():
    global top
    global size
    if size==0:
        return -1
    t_item = top.item
    top = top.next
    size -= 1
    return t_item

if __name__ == "__main__":

    test_case = "So when I die (the [first] I will see in (heaven) is a score list)." \
                "[ first in ] ( first out )." \
                "Half Moon tonight (At least it is better than no Moon at all]." \
                "A rope may form )( a trail in a maze." \
                "Help( I[m being held prisoner in a fortune cookie factory)]." \
                "([ (([( [ ] ) ( ) (( ))] )) ])." \
                " ." \
                "."
    p_dict = {")" : "(", "]" : "["}
    top = None
    size = 0
    dot_switch = False

    for i in test_case :
        if i=="." : dot_switch=True
        if dot_switch==False:
            if i in p_dict.values():
                push(i)
                continue
            if i in p_dict.keys():
                pop_item = pop()
                if pop_item==p_dict[i]:
                    continue
                else:
                    size=-100
        else:
            if size==0:
                print("YES")
            else:
                print("NO")
            dot_switch=False
            top=None
            size=0
