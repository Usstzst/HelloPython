# 一：斐波那契数列（Fibonacci sequence），又称黄金分割数列，
# 指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
# F0 = 0     (n=0)
# F1 = 1    (n=1)
# Fn = F[n-1]+ F[n-2](n=>2)

# first method:
# def fib(n):
#     if n==1 or n==2:
#         return 1
#     return fib(n-1)+fib(n-2)
#
# print(fib(10))



# 二： 输出九九乘法表

#  方法一：
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print("%d*%d=%d" % (i, j, i*j),'\t', end='')
#         if i == j:
#            # j=0
#             print('')

# 方法二:
# i=0
# j=0
# while i<9:
#     i+=1
#     while j<9:
#         j+=1
#         print(j,"x",i,"=",i*j,"\t",end="")
#         if i==j:
#             j=0
#             print("")
#             break


# 三： 暂停一秒输出

# import time
#
# myD = {1: 'a', 2: 'b'}
# for key, value in dict.items(myD):
#     print(key,value)
#     time.sleep(1)  # 暂停 1 秒


# 四：暂停一秒输出，并格式化当前时间


import time

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

# 暂停一秒
time.sleep(1)

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))