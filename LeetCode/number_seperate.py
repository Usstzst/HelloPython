#-*- coding: utf-8 -*-
'''
题目描述
继MIUI8推出手机分身功能之后，MIUI9计划推出一个电话号码分身的功能：
首先将电话号码中的每个数字加上8取个位，然后使用对应的大写字母代替 
（"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"）， 
然后随机打乱这些字母，所生成的字符串即为电话号码对应的分身。

输入描述:
第一行是一个整数T（1 ≤ T ≤ 100)表示测试样例数；接下来T行，每行给定一个分身后的电话号码的分身（长度在3到10000之间）。
输出描述:
输出T行，分别对应输入中每行字符串对应的分身前的最小电话号码（允许前导0）。

'''


num=int(raw_input())
n=[0]*10
for i in range(num):
    instr=raw_input()
    #统计各位数字次数
    n[0]=instr.count('Z')
    n[2]=instr.count('W')
    n[4]=instr.count('U')
    n[6]=instr.count('X')
    n[8]=instr.count('G')
    n[1]=instr.count('O')-n[0]-n[2]-n[4]
    n[3]=instr.count('T')-n[2]-n[8]
    n[5]=instr.count('F')-n[4]
    n[7]=instr.count('S')-n[6]
    n[9]=instr.count('I')-n[5]-n[6]-n[8]
    #对应数字位-8
    m=n[8:]+n[0:8]
    s=''
    for i in range(len(m)):
        s += str(i)*m[i]
    print s