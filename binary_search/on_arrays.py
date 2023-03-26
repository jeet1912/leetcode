class Solution:

    # Given an array of integers nums which is sorted in ascending order, 
    # and an integer target, write a function to search target in nums. 
    # If target exists, then return its index. Otherwise, return -1.
    # implement in O(log(n))

    def search(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l<=r:
            mid = (l+r)//2
            num = nums[mid]
            if num == target:
                return mid
            if num < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1
    
    # Each row is sorted in non-decreasing order.
    # The first integer of each row is greater than the last integer of the previous row.
    # based on the conditions, we treat the entire matrix as an array of size m*n
    def search2D(self, matrix: list[list[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l = 0
        r = m*n-1
        while l<=r:
            mid = (l+r)//2
            row = mid // n
            col = mid % n
            num = matrix[row][col]
            if num == target:
                return True
            if num < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
    # Time complexity - log(m*n)

    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        
        def binarySearch(arr,target):
            l = 0
            r = len(arr)-1
            while l<=r:
               mid = (l+r)//2
               if arr[mid] < target:
                   l = mid + 1
               else:
                   r = mid - 1
            return l
        
        potions.sort() #mlogm
        m = len(potions)
        ans = []
        for spell in spells:
            i = binarySearch(potions,success/spell) #nlogm
            ans.append(m-i) 
        return ans
    # (m+n)logm
       
       
                   
    
s = Solution()
ans = s.successfulPairs(spells = [3,1,2], potions = [8,5,8], success = 16)
print(ans)