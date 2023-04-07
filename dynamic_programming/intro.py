from functools import cache

class Solution:

    #top down
    def fibbo(self,n):
        if n == 1:
            return 0
        if n == 2:
            return 1
        if n in memo:
            return memo[n]

        memo[n] = self.fibbo(n-1) + self.fibbo(n-2)
        return memo[n]
    
    # bottum up or tabulation
    def fibbo2(self,n):
        arr = [0] * (n+1)
        arr[2] = 1
        for i in range(3,n+1):
            arr[i] = arr[i-1] + arr[i-2]
        return arr[n]

    def minCostClimbingStairs(self, cost:list[int]) -> int:
        def dp(i):
            if i <= 1:
                return 0
            if i in memo:
                return memo[i]
            memo[i] = min(dp(i-1)+cost[i-1],dp(i-2)+cost[i-2])
            return memo[i]
            
        memo = {}
        return dp(len(cost))
    
    def minCostClimbingStairsBU(self, cost:list[int]) -> int:
        arr = [0]*(len(cost) + 1)
        for i in range(2,len(cost)+1):
            one_step = cost[i-1] + arr[i-1]
            two_step = cost[i-2] + arr[i-2]
            arr[i] = min(one_step,two_step)
        return arr[-1]

    def rob(self,nums:list[int]) -> int:
        if (len(nums) == 1):
            return nums[0]
        def dp(i):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0],nums[1])
            if i in memo:
                return memo[i]

            memo[i] = max(dp[i-1], dp[i-2]+nums[i])
            return memo[i]
        memo = {}
        return dp(len(nums)-1)
    
    def robBU(self,nums:list[int]) -> int:
        if (len(nums) == 1):
            return nums[0]
        arr = [0]*len(nums)
        arr[0] = nums[0]
        arr[1] = max(nums[0],nums[1])

        for i in range(2,len(nums)):
            arr[i] = max(arr[i-1], arr[i-2]+nums[i])
        return arr[len(nums)-1]

    def longestIncreasingSubsequence(self, nums: list[int]) -> int:
        @cache
        def dp(i):
            ans = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    ans = max(dp(j) + 1, ans)
            return ans
        return max(dp(i) for i in range(len(nums)))
    
    def longestISBU(self,nums: list[int]) -> int:
        dp = [1]*len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])
        return max(dp)

    def mostPoints(self, nums: list[list[int]]) -> int:
        @cache
        def dp(i):
            if i >= len(nums):
                return 0
            j = i + nums[i][1] + 1
            return max(dp(i+1),dp(j)+nums[i][0])
        return dp(0)
                
    def climbingStairs(self, nums: int) -> int:
        def dp(n):
            if n == 1:
                return 1
            if n == 2:
                return 2
            if n in memo:
                return memo[n]
            memo[n] = dp(n-1) + dp(n-2)
            return memo[n]
        memo = {}
        return dp(nums)

memo = {}      # for fibbo, top-down
s = Solution()
ans = s.climbingStairs(3)
print(ans)