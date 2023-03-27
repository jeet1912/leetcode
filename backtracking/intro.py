class Solution:
    
    def permute(self, nums: list[int]) -> list[list[int]]:
        def backtrack(curr):
            print('Backtrack call ',curr)
            if len(curr) == len(nums):
                ans.append(curr[:])
                return
        
            for num in nums:
                if num not in curr:
                    curr.append(num)
                    print('Curr ',curr)
                    backtrack(curr)
                    y = curr.pop()
                    print('y ',y)
                    
        ans = []
        backtrack([])
        return ans
    
s = Solution()
ans = s.permute(nums=[1,2,3])