class Basics:

    def palindrome(self, s:str) -> bool:
        j = len(s) - 1
        i = 0
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
    # Time complexity is O(n)
    # Space complexity is O(1)

    def sortedTwoSum(self, nums: list[int], target: int) -> bool:
        i = 0
        j = len(nums) - 1
        while i < j :
            sum = nums[i] + nums[j]
            if sum == target:
                return True
            elif sum < target:
                i += 1
            else:
                j -= 1
        return False
    # Time complexity is O(n)
    # Space complexity is O(1)

    def sortedArraysFromTwoSorted(self, num1: list[int], num2: list[int]) -> list[int]:
        i = 0
        j = 0
        result = []
        
        while i < len(num1) and j < len(num2):
            if num1[i] < num2[j]:
                result.append(num1[i])
                i += 1
            else :
                result.append(num2[j])
                j += 1
        
        while i < len(num1):
            result.append(num1[i])
            i += 1
        
        while j < len(num2):
            result.append(num2[j])
            j += 1
        return result
    # Time complexity is O(n)
    # Space complexity is O(1) (not counting the result array)

    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        while i < len(s)and j < len(t):
            if s[i] == t[j]:
                i+=1
            j+=1
        return i == len(s)
    # Time complexity is O(n)
    # Space complexity is O(1)

    def reverseString(self, s: list[str]) -> None:
        i = 0
        j = len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return s
    # Time complexity is O(n)
    # Space complexity is O(1)
    def reverseWords(self, s: str) -> str:
        s = s.split()
        i = 0
        j = len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return ' '.join(s)  
    # Time complexity is O(n)
    # Space complexity is O(1)

    def sortedSquares(self, nums: list[int]) -> list[int]:
        nums = [n**2 for n in nums]
        sorted = [0]*len(nums)
        k = 0
        j = len(nums) - 1
        value = 0
        for i in range(len(nums)-1,-1,-1):
            if abs(nums[k]) > abs(nums[j]):
                value = nums[k]
                k += 1
            else:
                value = nums[j]
                j -= 1
            sorted[i] = value**2
        return sorted
    # Time complexity is O(n)
    # Space complexity is O(n)

    
b = Basics()
print(b.sortedSquares([-4,-2,-1,0,6,8,9,14,15]))