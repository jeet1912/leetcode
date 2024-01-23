class Solution:
    
    def removeElementInPlace(self,nums,val):
        while val in nums:
            nums.remove(val)
        return len(nums)
    
    def findIndexOfFirstOccuranceInString(self, haystack, needle):
        return haystack.index(needle) if needle in haystack else -1
            
    
s = Solution()
ans = s.findIndexOfFirstOccuranceInString('leetcode','code')
print(ans)
    