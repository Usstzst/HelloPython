# -*- coding: utf-8 -*-

'''
题目描述:
约瑟夫问题是一个著名的趣题。
这里我们稍稍修改一下规则。有n个人站成一列。
并从头到尾给他们编号，第一个人编号为1。
然后从头开始报数，第一轮依次报1，2，1，2...然后报到2的人出局。
接着第二轮再从上一轮最后一个报数的人开始依次报1，2，3，1，2，3...报到2，3的人出局。
以此类推直到剩下以后一个人。现在需要求的即是这个人的编号。

给定一个int n，代表游戏的人数。请返回最后一个人的编号

'''



class Joseph:
    def getResult(self, n):
        # write code here
        cons=[i for i in range(1,n+1)]
        # 控制cons 的长度
        res=n
        # 控制取余的基数
        round=2
        while res>1:
            for i in range(len(cons)):
                # 把所有对round 取余不等于1 的数赋值为-1
                if (i+1)%round!=1:
                    cons[i]=-1
                    res-=1
            cons=[i for i in cons if i!=-1]
            cons.insert(0,cons.pop())
            round+=1
        return cons[0]
        


#######################  拓展  ##################################

"""约瑟夫环问题：
已知n个人（以编号1，2，3...n分别表示）围坐在一张圆桌周围。
从编号为k的人开始报数，数到m的那个人出列；
他的下一个人又从1开始报数，数到m的那个人又出列；依此规律重复下去，
直到圆桌周围的人全部出列。
通常解决这类问题时我们把编号从0~n-1，
最后结果+1即为原问题的解。

算法原理：
1、一群人围在一起坐成环状（如：N）
2、从某个编号开始报数（如：K）
3、数到某个数（如：M）的时候，此人出列，下一个人重新报数
4、一直循环，直到所有人出列 [3]  ，约瑟夫环结束

"""          
        
#方法一
def func(count):
    l = list(range(1,count+1))
    n=0
    while len(l)>1:
        for i in l[:] :
            if n == 0:
                n+=1             
                continue            
            else:
                l.remove(i)
                n=0   
    print(l[0])
func(1000)
 
 
#方法二
def josephus(n,k):
    link=range(1,n+1)
    ind=0
    for loop_i in range(n-1):
        ind = (ind+k)%len(link)
        ind -= 1
        #print 'Kill:',link[ind]
        del link[ind]
        
        if ind == -1:#thelastelementoflink
            ind=0
    print'survice:',link[0]
     
 
if __name__=='__main__':
 
    josephus(1000,2)
    print'-'*30
    josephus(10,5)
    print'-'*30
    josephus(10,1)
 