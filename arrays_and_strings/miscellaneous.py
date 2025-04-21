class Solution:
    
    def removeElementInPlace(self,nums,val):
        while val in nums:
            nums.remove(val)
        return len(nums)
    
    def findIndexOfFirstOccuranceInString(self, haystack, needle):
        return haystack.index(needle) if needle in haystack else -1
    
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        ans = ""
        for i, word in enumerate(words):
            word = list(word)
            l = 0
            r = len(word)-1
            while l<r:
                word[l], word[r] = word[r], word[l]
                l += 1
                r -= 1
            if i == 0:
                ans = "".join(word)
            else:
                ans += " " + "".join(word)
        return ans
    
    def reverseWords2(self, s: str) -> str:
        words = s.split(" ")
        for i in range(len(words)):
            words[i] = words[i][::-1]
        return " ".join(words)
        # Time complexity is O(n)
        # Space complexity is O(n)
    
s = Solution()
ans = s.reverseWords('leetcode rules')
print(ans)
    