# -*- coding:utf-8 -*-
'''
��Ŀ����:
������ջ��ʵ��һ�����У���ɶ��е�Push��Pop������ �����е�Ԫ��Ϊint���͡�

˼·��

ջ�� �Ƚ����
���У� �Ƚ��ȳ�

������ջ˳�򲻱䣬��ջ˳����pop(����pop(0)��ջ) ʵ���Ƚ��ȳ�


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
        
