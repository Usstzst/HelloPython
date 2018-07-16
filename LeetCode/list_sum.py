'''

题目描述:数列的第一项为n，以后各项为前一项的平方根，求数列的前m项的和。
输入描述:输入数据有多组，每组占一行，由两个整数n（n < 10000）和m(m < 1000)组成，n和m的含义如前所述。
输出描述:对于每组输入数据，输出该数列的和，每个测试实例占一行，要求精度保留2位小数。

'''

import sys
import math


def sqlrt(n, m):
    sum = 0
    while m > 0:
        m -= 1
        sum += n
        n = math.sqrt(n)
    return "{0:.2f}".format(sum)

if __name__ =='__main__':
    a = sys.stdin.readlines()
    for i in a:
        n = int(i.split(" ")[0])
        m = int(i.split(" ")[1])
        print(sqlrt(n, m))