# -*- coding:utf-8 -*-
'''
题目描述:
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。

思路：

栈： 先进后出
队列： 先进先出

所以入栈顺序不变，出栈顺序倒序pop(即：pop(0)出栈) 实现先进先出


'''



class Solution:
    def __init__(self):
        self.arr = []
    def push(self, node):
        # write code here
        self.arr.append(node)
    def pop(self):
        # return xx
        return self.arr.pop(0)
        
