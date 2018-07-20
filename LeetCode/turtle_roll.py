# -*- coding : utf-8 -*-

'''
龟图形。
我们将使用 turtle 模块递归绘制螺旋。 
导入 turtle 模块后，我们创建一个乌龟。当乌龟被创建时，它也创建一个窗口来绘制。
接下来我们定义 drawSpir​​al 函数。
这个简单函数的基本情况是当我们想要绘制的线的长度（由 len 参数给出）减小到零或更小时。
如果线的长度大于零，我们让乌龟以len 单位前进，然后向右转 90 度。当我们再次调用 drawSpir​​al 并缩短长度时递归。

'''



import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle,lineLen-5)
        
drawSpiral(myTurtle,100)
myWin.exitonclick()
