class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = [-1]*256
        count = 0
        first = -1
        for i in range(len(s)):
            if a[ord(s[i])] > first:
                first = a[ord(s[i])]
            a[ord(s[i])] = i
            count = max(count,(i-first))
        return count
        
        
s = Solution()
print(s.lengthOfLongestSubstring('abcabcdsa'))


# class Solution2(object):
    # def lengthOfLongestSubstring(self, s):
        # """
        # :type s: str
        # :rtype: int
        # """
        # a={}
        # count = 0
        # first=-1
        # for i in range(len(s)):
            # if s[i] in a and a[s[i]]>first:
                # first=a[s[i]]
                # print('first:', first)
            # a[s[i]]=i
            # print('i:',i)
            # count=max(count,(i-first))
            # print('count:', count)
        # return count
        
# s = Solution2()
# print(s.lengthOfLongestSubstring('abcabcdsa'))