class Solution:
    
    def permute(self, nums: list[int]) -> list[list[int]]:
        def backtrack(curr):
            #print('Backtrack call ',curr)
            if len(curr) == len(nums):
                ans.append(curr[:])
                #print('Gonna return')
                return
        
            for num in nums:
                if num not in curr:
                    curr.append(num)
            #        print('Curr ',curr)
                    backtrack(curr)
                    y = curr.pop()
            #        print('y ',y)
                    
        ans = []
        backtrack([])
        return ans
    
    def subset(self, nums: list[int]) -> list[list[int]]:
        def backtrack(curr, i):
            if i > len(nums):
                return
            ans.append(curr[:])
            for j in range(i,len(nums)):
                curr.append(nums[j])
                backtrack(curr,j+1)
                curr.pop()
        ans = []
        backtrack([],0)
        return ans

    def combine(self,n:int,k:int) -> list[list[int]]:
        def backtrack(curr,i):
            if len(curr) == k:
                ans.append(curr[:])
                return
            
            for num in range(i,n+1):
                curr.append(num)
                backtrack(curr,num+1)
                curr.pop()
        
        ans = []
        backtrack([],1)
        return ans

            
    
s = Solution()
ans = s.combine(n=4, k = 2)
print(ans)