
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in range(len(nums)):
            x = nums[i]
            if target-x in dict:
                print(dict)
                return (dict[target-x]+1, i+1)
            dict[x] = i
            
s = Solution()
print(s.twoSum([11,23,2,4],9))



# class Solution:
    # def twoSum(self, num, target):
        # index = []
        # numtosort = num[:]
        # numtosort.sort()
        # i = 0
        # j = len(numtosort) - 1
        # while i < j:
            # if numtosort[i] + numtosort[j] == target:
                # for k in range(0, len(num)):
                    # if num[k] == numtosort[i]:
                        # index.append(k)
                        # break
                # for k in range(len(num)-1, -1, -1):
                    # if num[k] == numtosort[j]:
                        # index.append(k)
                        # break
                # index.sort()
                # break
                
            # elif numtosort[i] + numtosort[j] < target:
                # i = i + 1
            # elif numtosort[i] + numtosort[j] > target:
                # j = j-1
        # return (index[0]+1, index[i]+1)
