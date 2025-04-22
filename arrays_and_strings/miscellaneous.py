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
    
    def reversePrefix(self, word: str, ch: str) -> str:
        l = r = 0
        word = list(word)
        for i in range(len(word)):
            if word[r] == ch:
                while l<r:
                    word[l], word[r] = word[r], word[l]
                    l += 1
                    r -= 1
                break 
            r += 1
        return "".join(word)
    
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        l = r = i = 0
        s = list(s)
        t = list(t)
        cost = 0
        maxLength = 0      
        for r in range(len(t)):
            cost += abs(ord(s[r])-ord(t[i]))    
            while cost > maxCost:
                cost -= abs(ord(s[l])-ord(t[l]))
                l+=1
            maxLength = max(maxLength,i-l+1)    
            i+=1
        return maxLength

    def pivotIndex(self, nums: list[int]) -> int:
        n = len(nums)
        prefix = [0]*(n+1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]

        leftSum = rightSum = 0
        for i in range(n):
            leftSum = prefix[i]
            rightSum = prefix[n] - prefix[i+1]
            if leftSum == rightSum:
                return i
        return -1
   
    
s = Solution()
ans = s.pivotIndex([1,2,3])
print(ans)
    