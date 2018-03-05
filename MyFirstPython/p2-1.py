"""  第一个小程序  """

import random

secret = random.randint(1,10)
temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
guess = int(temp)

while guess != secret:
              temp = input("哎呀，猜错了，请重新输入吧：")
              guess = int(temp);
              
if guess == secret:
              print ("你是小甲鱼心里的蛔虫吗？")
              print ("哼，猜中了也没有奖励！")
else:
              if guess > secret :
                            print("哥，大了大了~~~")
              
              else:
                            print("嘿，小了小了")
                            
print("游戏结束，不玩啦！")





""" 第二个小程序   """"

score=input("请输入一个分数：")
if 100 >= score >=90:
              print("A")
elif 90 > score >= 80:
              print("B")
elif 80 > score >=60:
              print("C")
elif 60 > score >= 0:
              print("D")
else:
              print("输入有误！")




"""  第三个小程序 """

for i in range(10):
              if i %2 !=0:
                            print(i)
                            continue
              i +=2
print(i)



              
              
