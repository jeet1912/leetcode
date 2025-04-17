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

b = Basics()
print(b.sortedTwoSum([1,2,4,6,8,9,14,15], 13))