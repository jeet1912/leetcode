class PrefixSum:
    
    def answerQueries(self, nums: list[int], queries: list[int], limit: int) -> list[bool]:
        prefix = [nums[0]]
        for i in range(len(nums)):
            prefix.append(nums[i]+prefix[-1])
        # Time complexity is O(n)
        result = []
        for query in queries:
            i , j = query
            sum = prefix[j] - prefix[i] + nums[i]
            if sum > limit:
                result.append(False)
            else:
                result.append(True)
        return result
        # Time complexity is O(m)

        # Net time complexity is O(n+m)
    
ps = PrefixSum()
print(ps.answerQueries([1,2,3,4], [[0,1],[1,2],[2,3]], 3))