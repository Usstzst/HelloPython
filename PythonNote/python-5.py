# 输入三个整数x,y,z，请把这三个数由小到大输出。

# 列表
l=[]
for i in range(3):
    x=int(input('integer:\n'))
    l.append(x)
l.sort()
print(l)

# 字典
x = int(input("x:"))
y = int(input("y:"))
z = int(input("z:"))
a = {"x": x, "y": y, "z": z}
print('--------分割线--------')
for w in sorted(a, key=a.get):
    print(w, a[w])
