
'''
    题目描述： 写一个程序实现前缀表达式，例如`(2 + 3) * 4`写成`* + 2 3 4`，这样就能避免使用括号了。
    
    输入包含多组数据，每组数据包含两行。

    第一行为正整数n（3≤n≤50），紧接着第二行包含n个由数值和运算符组成的列表。

    “+-*/”分别为加减乘除四则运算，其中除法为整除，即“5/3=1”。
'''


def clac(arr):
    for i, v in enumerate(arr):
        if v in ["+", "-", "*", "/"]:
            if arr[i+1].isnumeric() and arr[i+1].isnumeric():
                return calc(arr[:i] + [str(int(eval(arr[i+1] + v + arr[i+2])))] + arr[i+3:])
    return arr[0]


while True:
        try:
            a, b = input(), input().split()
            print(calc(b))
        except:
            break
        
    