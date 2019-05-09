
# # 输入某年某月某日，判断这一天是这一年的第几天？


# 方法一：
# year = int(input('year:\n'))
# month = int(input('month:\n'))
# day = int(input('day: \n'))
#
# months = (0,31,59,90,120,151,181,212,243,273,304,334)
# if 0 < month <= 12:
#     sum= months[month-1]
# else:
#     print('data error')
#
# sum +=day
# leap = 0
# if (year % 400 ==0 ) or (year %4 ==0) and (year % 100 !=0):
#     leap=1
# if (leap ==1) and (month>2):
#     sum +=1
# print('this is the ',sum, 'th day!')


# 方法二:

# year = int(input('year:\n'))
# month = int(input('month:\n'))
# day = int(input('day: \n'))
# days = [31,28,31,30,31,30,31,31,30,31,30,31]
# if year % 400 ==0 or (year %4 ==0 and year %100 !=0):
#     days[2] +=1
#
# now =sum(days[0:month-1])+day
# print('this is the ',now, 'th day!')

# 方法三：加入异常处理

import time

while 1:
    try:
        a=input('请输入日期yyyy-mm-dd:')
        b=time.strptime(a,'%Y-%m-%d')
    except ValueError:
        print('请输入正确的日期格式！')
    else:
        b=time.strptime(a,'%Y-%m-%d')
        dd=time.strftime('%j',b)
        yy=time.strftime('%Y',b)
        print('this is the ', dd, 'th day!')
        break



