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

b = Basics()
print(b.sortedTwoSum([1,2,4,6,8,9,14,15], 13))