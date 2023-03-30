class Solution:
    def fibbo(self,n):
        if n == 1:
            return 0
        if n == 2:
            return 1
        if n in memo:
            return memo[n]

        memo[n] = self.fibbo(n-1) + self.fibbo(n-2)
        return memo[n]

memo = {}   
s = Solution()
ans = s.fibbo(4)
print(ans)