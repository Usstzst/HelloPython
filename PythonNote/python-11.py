"""
一、古典问题
有一对兔子，从出生后第3个月起每个月都生一对兔子
小兔子长到第三个月后每个月又生一对兔子
假如兔子都不死，问每个月的兔子总数为多少？

"""

# 方法一
f1=1
f2=1
for i in range(1,22):
    print('%12ld %12ld' %(f1,f2))
    if (i%3)==0:
        print('\n')
    f1=f1+f2
    f2=f1+f2


# 方法二：

def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print fib(36)


# 二、判断101-200之间有多少个素数，并输出所有素数。

# 方法一：
# l=[]
# for i in range (101,201):
#     for k in range(2,i-1):
#         if i%k==0:
#             break
#     else:
#         l.append(i)
# print(l)
# print('总数为：%d' %len(l))

#方法二：

# from math import sqrt
#
# l=[]
# for x in range(101,201):
#     l.append(x)
#     for i in range(2,int(sqrt(x))+1):
#         if x%i==0:
#             l.pop()
#             break
#
# n=len(l)
# print(l)
#
# print('总数为：',n)


# 三、打印出所有的"水仙花数"
# 所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
# 方法一：
# for i in range(100,1000):
#     a = i/100
#     b = (i/10) % 10
#     c = i % 10
#     if i == a**3+b**3+c**3:
#         print(i)


# 方法二：
# for i in range(100, 1000):
#     s = str(i)
#     if int(s[0]) ** 3 + int(s[1]) ** 3 + int(s[2]) ** 3 == i:
#         print(i)


# 四：输出指定格式的日期。使用 datetime 模块。

# import datetime
#
# if __name__ == '__main__':
#     # 输出今日日期，格式为 dd/mm/yyyy。更多选项可以查看 strftime() 方法
#     print(datetime.date.today().strftime('%d/%m/%Y'))
#
#     # 创建日期对象
#     BirthDate = datetime.date(1941, 1, 5)
#
#     print(BirthDate.strftime('%d/%m/%Y'))
#
#     # 日期算术运算
#     BirthNextDay = BirthDate + datetime.timedelta(days=1)
#
#     print(BirthNextDay.strftime('%d/%m/%Y'))
#
#     # 日期替换
#     FirstBirthday = BirthDate.replace(year=BirthDate.year + 1)
#
#     print(FirstBirthday.strftime('%d/%m/%Y'))
#


# 五、输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

# import string
#
# s=input('请输入一行字符：\n')
# letters=0
# space=0
# digit=0
# others=0
# i=0
# while i<len(s):
#     c=s[i]
#     i +=1
#     if c.isalpha():
#         letters +=1
#     elif c.isspace():
#         space +=1
#     elif c.isdigit():
#         digit +=1
#     else:
#         others +=1
# print('char=%d,space=%d,digit=%d,others=%d'%(letters,space,digit,others))
#


# 六、求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。几个数相加由键盘控制。

# Tn =0
# Sn = []
# n=int(input('n=：\n'))
# a=int(input('a='))
# for count in range(n):
#     Tn=Tn+a
#     a=a*10
#     Sn.append(Tn)
#     print(Tn)
#
# sum=sum(Sn)
# print('计算和为：',sum)

# 七、一个数如果恰好等于它的因子之和，这个数就称为"完数"。
#     例如6=1＋2＋3.编程找出1000以内的所有完数。

# for i in range(1, 1001):
#     m = []
#     for j in range(1, i):
#         if i % j == 0:
#             m.append(j)
#     if sum(m) == i:
#         print(i)
#         print(m)


# 八、一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，
# 求它在第10次落地时，共经过多少米？第10次反弹多高？

# tour=[]
# height=[]
# hei=100.0
#
# for i in range(1,11):
#     if i==1:
#         tour.append(hei)
#     else:
#         tour.append(2*hei)
#     hei/=2
#     height.append(hei)
#
# print('总高度： tour={0}'.format(sum(tour)))
# print('第十次反弹高度：height={0}'.format(height[-1]))

# 九、猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个
# 第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
# 以后每天早上都吃了前一天剩下的一半零一个。
# 到第10天早上想再吃时，见只剩下一个桃子了。
# 求第一天共摘了多少。

# 逆向思维，从后往前推


# 十、两个乒乓球队进行比赛，各出三人# 。
#  甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。
# 有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，
# 请编程序找出三队赛手的名单。

# for a in ['x', 'y', 'z']:
#     for b in ['x', 'y','z']:
#         for c in ['x', 'y','z']:
#             if (a!=b) and (b!=c) and (a!=c)and (a!= 'x')and (c!= 'x')and(c!='z'):
#                 print('三队赛手名单： a--%s,b--%s,c--%s'%(a,b,c))

# 十一、打印图形：菱形
# from sys import stdout
#
# for i in range(4):
#     for j in range(2 - i + 1):
#         stdout.write(' ')
#     for k in range(2 * i + 1):
#         stdout.write('*')
#     print('\n')
#
# for i in range(3):
#     for j in range(i + 1):
#         stdout.write(' ')
#     for k in range(4 - 2 * i + 1):
#         stdout.write('*')
#     print('\n')


# 十二、有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...
# 求出这个数列的前20项之和。

#  方法一
# a=2.0
# b=1.0
# s=0
# for i in range(1,21):
#     s +=a/b
#     # t = a
#     # a = a + b
#     # b = t
#     b,a=a,a+b
# print(s)

# 方法二：
# a=2.0
# b=1.0
# l=[]
# l.append(a/b)
# for n in range(1,20):
#     b,a=a,a+b
#     l.append(a/b)
# print(sum(l))


# 十三、求1+2!+3!+...+20!的和。

# n=0
# s=0
# t=1
# for n in range(1,21):
#     t *=n
#     s +=t
# print('1!+2!+3!+4!+...+20! = %d'%s)

# 函数
# class Employee:
#     empCount = 0
#
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#         Employee.empCount +=1
#     def displayCount(self):
#         print('Total Employee %d' %Employee.empCount)
#
#     def displayEmployee(self):
#         print('Name: ',self.name,'  , Salary : ',self.salary)
#
# emp1=Employee('Zara',2000)
# emp2=Employee('Manni',5000)
# emp1.displayEmployee()
# emp2.displayEmployee()
# print('Total Employee %d ' %Employee.empCount)


#  析构函数 __del__ 在对象销毁时被调用，当对象不再被使用时，__del__方法运行
# class Point:
#     def __init__(self,x=0,y=0):
#         self.x=x
#         self.y=y
#     def __del__(self):
#         class_name=self.__class__.__name__
#         print(class_name,'销毁')
#
# pt1=Point()
# pt2=pt1
# pt3=pt1
# print(id(pt1),id(pt2),id(pt3))
# del pt1
# del pt2
# del pt3

# 继承
# class Parent:
#     parentAttr = 100
#     def __init__(self):
#         print('调用父类构造函数')
#     def parentMethod(self):
#         print('调用父类方法')
#     def setAttr(self,attr):
#         Parent.parentAttr=attr
#     def getAttr(self):
#         print('父类属性：',Parent.parentAttr)
#
# class Child(Parent):
#     def __init__(self):
#         print('调用子类构造函数')
#     def childMethod(self):
#         print('调用子类方法')
#
# c=Child()
# c.childMethod()
# c.parentMethod()
# c.setAttr(200)
# c.getAttr()


# 正则表达式： 帮助你方便的检查一个字符串是否与某种模式匹配
# re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；
# 而re.search匹配整个字符串，直到找到一个匹配。

# import re
# print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
# print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配
# print(re.search('www', 'www.runoob.com').span())
# print(re.search('com', 'www.runoob.com').span())



# pass 语句 不做任何事情，一般用作占位语句

# for letter in 'python':
#     if letter =='h':
#         pass
#         print('这是pass 块')
#     print('当前字母： ',letter)

# 日期和时间
# Python 提供了一个 time 和 calendar 模块可以用于格式化日期和时间。
# 时间间隔是以秒为单位的浮点小数。
# 每个时间戳都以自从1970年1月1日午夜（历元）经过了多长时间来表示。
# 函数time.time()用于获取当前时间戳

import time

#1、获取当前时间戳
ticks = time.time()
print('当前时间戳为：', ticks)

# 2、获取当前时间元组
# localtime = time.localtime(time.time())
# print('本地时间为：', localtime)

# 3、获取格式化时间
# localtime = time.asctime(time.localtime(time.time()))
# print('本地时间为：', localtime)

# 4、格式化时期

# print(time.strftime('%Y-%m-%d  %H:%M:%S',time.localtime()))
# print(time.strftime('%a %b %d %H:%M:%S %Y'),time.localtime())
# # 将格式字符串转换为时间戳
# a='Sat Mar 28 22:24:24 2016'
# print(time.mktime(time.strptime(a,'%a %b %d %H:%M:%S %Y')))



# 十三、利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。

# def output(s,l):
#     if l==0:
#         return
#     print(s[l-1])
#     output(s,l-1)
#
# s= input('Input a string:')
# l=len(s)
# output(s,l)

# 十四、计算年龄
# def age(n):
#     if n==1:
#         c=10
#     else:
#         c=age(n-1)+2
#     return c
# print(age(5))

