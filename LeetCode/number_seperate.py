#-*- coding: utf-8 -*-

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