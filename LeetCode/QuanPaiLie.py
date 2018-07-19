

def perm(list, stack):
    if not list:
        print(stack)
    else:
        for i in range(len(list)):
            stack.append(list[i])
            del list[i]
            perm(list, stack)
            list.insert(i, stack.pop())
            
list = ['A', 'B', 'C', 'D']
stack = []
perm(list, stack)
