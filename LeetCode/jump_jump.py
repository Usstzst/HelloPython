

N=int(input())
num=list(map(int,input().split()))
#print(num)
mindp=[0,]#第一个桩的最小跳一定是0次
for i in range(1,N+1):#初始化每个桩的最小跳次数
    mindp.append(10001)
    #print(mindp)
for i in range(1,N+1):#依次计算跳到每个桩需要的最小跳次数
    for j in range(1,i+1):#遍历前面所有的桩，找到一个可以跳到当前桩的位置
        if num[i-j]==0:#如果弹力为零，则当前树桩无用，继续下一个
            continue
        if (i-j)+num[i-j]>=i:
            mindp[i]=min(mindp[i],mindp[i-j]+1)
            #print(mindp[i])
if mindp[N]==10001:#统计完所有树桩的最小跳次数后，输出结果
    print(-1)
else:
    print(mindp[N])