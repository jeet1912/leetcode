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
    
    def allPathsFromSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        
        def backtracking(curr_node,path):
            print('Curr ',curr_node)
            if curr_node == l:
                ans.append(list(path))
                return
            
            for next_node in graph[curr_node]:
                path.append(next_node)
                print('Path ',path)
                backtracking(next_node,path)
                c = path.pop()
                print('Popped ',c)
            
        l = len(graph) - 1    
        ans = []
        path = [0]
        backtracking(0,path)
        return ans

    def letterCombinations(self, digits:str) -> list[str]:

        if len(digits) == 0:
            return []
        
        digits_to_letters = {"2" : "abc","3" : "def", "4": "ghi", "5": "jkl","6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        def backtracking(index,path):
            if len(path) == len(digits):
                ans.append(''.join(path))
                return
            
            possible_letters = digits_to_letters[digits[index]]
            for letter in possible_letters:
                path.append(letter)
                #print('Path ',path)
                backtracking(index+1,path)
                path.pop()

        ans = []
        backtracking(0,[])
        return ans
    
    #def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:


s = Solution()
ans = s.letterCombinations("23")
print(ans)