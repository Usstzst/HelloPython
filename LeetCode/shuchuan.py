#-*- coding: utf-8 -*-
"""
牛客网 数串

问题描述:

设有n个正整数，将他们连接成一排，组成一个最大的多位整数。

如:n=3时，3个整数13,312,343,连成的最大整数为34331213。

如:n=4时,4个整数7,13,4,246连接成的最大整数为7424613。

"""

def cmp(a,b):
    ab = int(a+b)
    ba = int(b+a)
    return 1 if ab > ba else -1

num = input('')
l = raw_input().split()
l.sort(cmp,reverse= True)
print(int(''.join(l)))