#-*- coding: utf-8 -*-

# from pythonds.basic import Stack

class Solution:
    def isPopOrder(self, pushV, popV):
        stack = []
        j = 0
        for i in pushV:
            stack.append(i)
        while stack:
            if stack[-1] == popV[j]:
                stack.pop()
                j += 1
            else:
                break
                
        if stack:
            return False
        else:
            return True
            
            
s = Solution()
print s.isPopOrder([1,2,3,4,5], [5,4,3,2,1])
print s.isPopOrder([1,2,3,4,5], [5,4,3,1,2])