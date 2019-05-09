
# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

# # 方法一：
# for i in range(1, 5):
#     for j in range(1, 5):
#         for k in range(1, 5):
#             if (i!=k)and(i!=j)and(j!=k):
#                 print(i,j,k)



# #  方法二：
# from itertools import permutations
#
# for i in permutations([1,2,3,4],3):
#     print(i)

# #  方法三：
line = []
for i in range(123, 433):
    a = i%10
    b = (i/10)%10
    c = (i/100)%10
    if a != b and a != c and b != c and 0<a<5 and 0<b<5 and 0<c<5:
        print(i)
    line.append(i)
print("the total is :", len(line))


# d=[]
# for a in range(1,5):
#     for b in range(1,5):
#         for c in range(1,5):
#             if (a!=b) and (a!=c) and (c!=b):
#                 d.append([a,b,c])
# print("总数量：", len(d))
# print(d)
