#-*- coding: utf-8 -*-


# import sys



# def getWXFnumber(num1, num2):
    # res = []
    # if num1<0 or num2>999:
        # return 0
    # if num1 >=0 and num2 <= 999:
        # for i in range(num1, num2):
            # tmp = []
            # if len(str(i)) < 3 or len(str(i)) > 3:
                # continue
            # for j in range(str(i)):
                # tmp.append(i//pow(10,j)%10)
            # getSum = pow(tmp[0],3)+ pow(tmp[1],3)+pow(tmp[2],3)
            # if getSum == i:
                # res.append(i)
            # del tmp
    # return res

 
 
# if __name__ == '__main__':
    # try:
        # while True:
            # arr1 = [int(t) for t in sys.stdin.readline().split()]
            # res1 = getWXFnumber(arr1[0], arr1[1])
            # if len(res1) >= 1:
                # print(" ".join(str(i) for i in res1))
            # if len(res1) == 0:
                # print('no')
    # except:
        # pass
        
        
import sys

arr = [int(t) for t in sys.stdin.readline().split()]
res = []
# if arr[0]<0 or arr[1]>999:
    # print '输入不符合条件'
if arr[0] >=0 and arr[1] <= 999:
    for i in range(arr[0], arr[1]):
        tmp = []
        if len(str(i)) < 3 or len(str(i)) > 3:
            continue
        for j in range(len(str(i))):
            tmp.append(i//pow(10,j)%10)
        getSum = pow(tmp[0],3)+ pow(tmp[1],3)+pow(tmp[2],3)
        if getSum == i:
            res.append(i)
            del tmp
    print res