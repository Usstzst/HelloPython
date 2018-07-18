
'''
题目描述：
现有一个字典，同时给定字典中的两个字符串s和t，给定一个变换，每次可以改变字符串中的任意一个字符，
请设计一个算法，计算由s变换到t所需的最少步数，同时需要满足在变换过程中的每个串都是字典中的串。

给定一个string数组dic，同时给定数组大小n，串s和串t，请返回由s到t变换所需的最少步数。
若无法变换到t则返回-1。保证字符串长度均小于等于10，且字典中字符串数量小于等于500。

测试样例：
["abc","adc","bdc","aaa”],4,”abc","bdc"
返回：2

解题思路：
BFS:依次找到与目标字符串差一个字符的字符串
1.初始化队列que，将s加入队列，设定一个result作为初始置为1
2.读取对头元素，遍历dic，找到与dic中与对头元素相差一个字符的字符串，将其加入队列,如果是t,则直接返回result，结束
3.将对头元素出队,继续第2步
4.执行完一次以上两步，把result+1

注：没有考虑找不到路径的情况，可以对result进行限制来解决。

'''

class Change:
   def countChanges(self, dic, n, s, t):
       # 初始化
       que = [s]
       target = s
       used = [s]
       result = 1
       while True:
           qlenth = len(que)
           for index in range(qlenth):
               for item in dic:
                   # 找到与目标字符串差一个字符的字符串
                   next = [0 for a, b in zip(target, item) if a != b and len(target)==len(item)]
                   if len(next) == 1 and item not in used:
                       # 找到目标字符串，结束
                       if item == t:
                           return result
                       que.append(item)
                       used.append(item)
               que.pop(0)
               target = que[0]
           result+=1