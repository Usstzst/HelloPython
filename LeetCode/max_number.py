'''
题目描述:
给定一个十进制的正整数number，选择从里面去掉一部分数字，希望保留下来的数字组成的正整数最大。

输入描述:
输入为两行内容，第一行是正整数number，1 ≤ length(number) ≤ 50000。第二行是希望去掉的数字数量cnt 1 ≤ cnt < length(number)。

输出描述:
输出保留下来的结果。
'''



nums = list(input())
cnt = int(input())
n, j, i= len(nums), cnt, 0
while j > 0 and i < n-1:
    if nums[i]>= nums[i+1]:
        i += 1
    else:
        nums.pop(i)
        j -= 1
        n -= 1
        i = i-1 if i > 0 else 0
if j > 0:
    nums = nums[:-j]
print(''.join(nums))