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
        # Space complexity is O(n)]

    def reverseOnlyLetters(self, s: str) -> str:
        l = 0
        r = len(s) - 1
        s = list(s)
        while l < r:
            if not s[l].isalpha():
                l+= 1
            elif not s[r].isalpha():
                r-=1
            else:        
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        return "".join(s)
    
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        l = 0
        r = 0 
        while l < len(nums1) and r < len(nums2):
            if nums1[l] == nums2[r]:
                return nums1[l]
            elif nums1[l] < nums2[r]:
                l += 1
            elif nums1[l] > nums2[r]:
                r += 1
        return -1
    
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = temp = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                temp = nums[r]
                nums[r] = nums[l]
                nums[l] = temp
                l += 1
        return nums
            
   
    
s = Solution()
ans = s.moveZeroes([0,1,0,3,12])
print(ans)
    