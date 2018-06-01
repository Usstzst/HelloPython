'''
   对于每组测试数据，第一行是一个正整数 n，0<n<=10000(n=0 结束)。
   而后的 n 行，每行的第一个字符可能是'P’或者'O’或者'A’；
   如果是'P’，后面还会跟着一个整数，表示把这个数据压入堆栈；
   如果是'O’，表示将栈顶的值 pop 出来，如果堆栈中没有元素时，忽略本次操作；
   如果是'A’，表示询问当前栈顶的值，如果当时栈为空，则输出'E'。
   堆栈开始为空。

'''


while True:
    try:
        a=int(input())
        if a==0:
            break
        stack=[]
        for i in range(a):
            string=input()
            if string.startswith("P"):
                stack.append(string.split()[-1])
            elif string=="A":
                print(stack[-1] if stack else "E")
            else:
                if stack:
                    stack.pop()
        print(stack)
    except:
        break